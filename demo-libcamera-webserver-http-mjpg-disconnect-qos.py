#!/usr/bin/env python3

"""
export PYTHONPATH=$HOME/libcamera/build/src/py:$PYTHONPATH
python demo-libcamera-webserver-http-mjpg-disconnect-qos.py
"""

import io
import mmap
import socket
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import libcamera
import numpy as np
from PIL import Image

# For a robust, dependency-free WebSocket side-channel
import hashlib
import base64
import struct
import json

SIZE_W = 1640
SIZE_H = 1232
WARMUP_FRAMES = 5

state_lock = threading.Lock()
current_client_id = None  
active_generation = 0    

# -------------------------------------------------
# Global Latency Telemetry Matrix
# -------------------------------------------------
# Key: Frame Index (0-99 rolling) -> Value: [capture_ts, send_ts]
telemetry_lock = threading.Lock()
telemetry_registry = {}


# -------------------------------------------------
# LibCameraCapture class
# -------------------------------------------------
class LibCameraCapture:
    def __init__(self, width=SIZE_W, height=SIZE_H):
        self.width = width
        self.height = height
        self.cm = libcamera.CameraManager.singleton()
        self.cam = self.cm.cameras[0]
        self.latest_frame = None
        self.frame_counter = 0
        self.frame_lock = threading.Lock()
        self.frame_event = threading.Event()
        self.running = False
        self.latest_capture_ts = 0.0

    def start(self):
        self.cam.acquire()
        config = self.cam.generate_configuration([libcamera.StreamRole.Viewfinder])
        stream_cfg = config.at(0)
        stream_cfg.pixel_format = libcamera.PixelFormat("RGB888")
        stream_cfg.size = libcamera.Size(self.width, self.height)
        self.cam.configure(config)
        self.stream = stream_cfg.stream
        self.stream_cfg = stream_cfg

        self.allocator = libcamera.FrameBufferAllocator(self.cam)
        self.allocator.allocate(self.stream)
        self.buffers = self.allocator.buffers(self.stream)
        self.cam.start()

        for i in range(WARMUP_FRAMES):
            _ = self.grab()
            print(f"[warmup] frame {i} done")

        self.running = True
        threading.Thread(target=self._capture_loop, daemon=True).start()

    def stop(self):
        self.running = False
        try:
            self.cam.stop()
        finally:
            self.cam.release()

    def grab(self):
        req = self.cam.create_request()
        req.add_buffer(self.stream, self.buffers[0])
        self.cam.queue_request(req)

        ready = []
        while not ready:
            ready = self.cm.get_ready_requests()
            if not ready:
                time.sleep(0.002)

        completed = ready[0]
        fb = completed.buffers[self.stream]
        plane = fb.planes[0]

        with mmap.mmap(plane.fd, plane.length, mmap.MAP_SHARED, mmap.PROT_READ, offset=plane.offset) as mm:
            data = mm.read(plane.length)

        stride_bytes = self.stream_cfg.stride
        stride_pixels = stride_bytes // 3
        frame = np.frombuffer(data, dtype=np.uint8)
        frame = frame[:stride_bytes * self.height]
        frame = frame.reshape(self.height, stride_pixels, 3)
        frame = frame[:, :self.width, :]
        return frame

    def _capture_loop(self):
        global current_client_id
        while self.running:
            with state_lock:
                has_active_client = current_client_id is not None
            if not has_active_client:
                time.sleep(0.1)
                continue

            frame = self.grab()
            ts = time.perf_counter()  # Record hardware capture completion profile

            with self.frame_lock:
                self.latest_frame = frame
                self.frame_counter += 1
                self.latest_capture_ts = ts
                print(f"[capture] frame #{self.frame_counter}")
            self.frame_event.set()
            self.frame_event.clear()

camera = LibCameraCapture()


# -------------------------------------------------
# HTTP and WebSocket Handler
# -------------------------------------------------
class MultiProtocolHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        return  

    def do_GET(self):
        if self.headers.get("Upgrade", "").lower() == "websocket":
            self._handle_websocket()
        elif self.path == "/":
            self._serve_index()
        elif self.path == "/mjpg":
            self._serve_mjpg()
        else:
            self.send_error(404, "Not found")

    def _serve_index(self):
        body = b"""
        <!DOCTYPE html>
        <html>
        <body style="background:#111; color:white; text-align:center; font-family:sans-serif;">
            <h1>Raspberry Pi Performance Stream</h1>
            <canvas id="videoCanvas" style="width:90%; border:2px solid #444; background:#000;"></canvas>
            <div id="status" style="margin-top:10px; color:#aaa;">Connecting telemetry...</div>

            <script>
                const canvas = document.getElementById('videoCanvas');
                const ctx = canvas.getContext('2d');
                const statusDiv = document.getElementById('status');

                const BOUNDARY_BYTES = new Uint8Array([45, 45, 102, 114, 97, 109, 101, 13, 10]); 
                const HEADER_SEP = new Uint8Array([13, 10, 13, 10]);                            
                const INDEX_MARKER = new Uint8Array([88, 45, 70, 114, 97, 109, 101, 45, 73, 110, 100, 101, 120, 58]); 
                const LENGTH_MARKER = new Uint8Array([67, 111, 110, 116, 101, 110, 116, 45, 76, 101, 110, 103, 116, 104, 58]); 

                const ws = new WebSocket('ws://' + window.location.host + '/ws');
                ws.onopen = () => { statusDiv.innerText = "Telemetry linked. Performance engines live."; };
                ws.onclose = () => { statusDiv.innerText = "Control channel disconnected."; };

                async function startStream() {
                    const response = await fetch('/mjpg');
                    const reader = response.body.getReader();
                    let buffer = new Uint8Array(0);

                    while (true) {
                        const { value, done } = await reader.read();
                        if (done) break;

                        const newBuffer = new Uint8Array(buffer.length + value.length);
                        newBuffer.set(buffer);
                        newBuffer.set(value, buffer.length);
                        buffer = newBuffer;

                        while (true) {
                            const boundaryIdx = findSequence(buffer, BOUNDARY_BYTES);
                            if (boundaryIdx === -1) break;

                            const remaining = buffer.subarray(boundaryIdx + BOUNDARY_BYTES.length);
                            const nextBoundaryIdx = findSequence(remaining, BOUNDARY_BYTES);
                            if (nextBoundaryIdx === -1) break;

                            const totalFrameLength = BOUNDARY_BYTES.length + nextBoundaryIdx;
                            const frameData = buffer.subarray(boundaryIdx, boundaryIdx + totalFrameLength);
                            buffer = buffer.subarray(boundaryIdx + totalFrameLength);

                            processMultipartFrame(frameData);
                        }
                    }
                }

                function findSequence(haystack, needle) {
                    for (let i = 0; i <= haystack.length - needle.length; i++) {
                        let match = true;
                        for (let j = 0; j < needle.length; j++) {
                            if (haystack[i + j] !== needle[j]) { match = false; break; }
                        }
                        if (match) return i;
                    }
                    return -1;
                }

                function extractHeaderValue(bytes, markerBytes) {
                    const pos = findSequence(bytes, markerBytes);
                    if (pos === -1) return null;
                    let start = pos + markerBytes.length;
                    while (start < bytes.length && bytes[start] === 32) { start++; }
                    let end = start;
                    while (end < bytes.length && bytes[end] !== 13) { end++; }
                    return new TextDecoder('ascii').decode(bytes.subarray(start, end)).trim();
                }

                function processMultipartFrame(bytes) {
                    const headerEndOffset = findSequence(bytes, HEADER_SEP);
                    if (headerEndOffset === -1) return;

                    const headerBlock = bytes.subarray(0, headerEndOffset);
                    const lengthStr = extractHeaderValue(headerBlock, LENGTH_MARKER);
                    const indexStr = extractHeaderValue(headerBlock, INDEX_MARKER);
                    if (!lengthStr || !indexStr) return;

                    const len = parseInt(lengthStr, 10);
                    const frameIndex = parseInt(indexStr, 10);

                    const imgStart = headerEndOffset + 4;
                    const imgBytes = bytes.subarray(imgStart, imgStart + len);

                    const blob = new Blob([imgBytes], { type: 'image/jpeg' });
                    const img = new Image();
                    img.onload = () => {
                        canvas.width = img.naturalWidth;
                        canvas.height = img.naturalHeight;
                        ctx.drawImage(img, 0, 0);
                        URL.revokeObjectURL(img.src);

                        if (ws.readyState === WebSocket.OPEN) {
                            ws.send(JSON.stringify({ event: "rendered", index: frameIndex }));
                        }
                    };
                    img.src = URL.createObjectURL(blob);
                }

                startStream();
            </script>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_mjpg(self):
        global current_client_id, active_generation
        client_id = id(self)
        my_generation = 0

        with state_lock:
            active_generation += 1
            my_generation = active_generation
            if current_client_id is not None:
                print(f"\n[DEBUG][http] NEW REQUEST from {client_id}. Evicting lingering stream thread {current_client_id}...")
            current_client_id = client_id
            print(f"[DEBUG][client {client_id}] ===== Granted Camera Ownership (Gen {my_generation}) =====")

        self.connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        try:
            self.send_response(200)
            self.send_header("Content-Type", "multipart/x-mixed-replace; boundary=frame")
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
            self.end_headers()
        except Exception as e:
            print(f"[DEBUG][client {client_id}] Failed during header negotiation: {e}")
            self._cleanup_client(client_id, my_generation)
            return

        sent = 0
        try:
            while True:
                with state_lock:
                    if active_generation != my_generation:
                        print(f"[DEBUG][client {client_id}] Loop stopped: Evicted/Disconnected by state change.")
                        break

                self.connection.setblocking(False)
                try:
                    if self.connection.recv(1, socket.MSG_PEEK) == b"":
                        break
                except BlockingIOError:
                    pass
                except Exception:
                    break
                finally:
                    self.connection.setblocking(True)

                flag_triggered = camera.frame_event.wait(timeout=0.2)
                if not flag_triggered:
                    continue

                with camera.frame_lock:
                    if camera.latest_frame is None:
                        continue
                    frame = camera.latest_frame.copy()
                    raw_idx = camera.frame_counter  
                    capture_ts = camera.latest_capture_ts

                # Normalize index to a strict sliding window of 0 to 99
                rolling_idx = raw_idx % 100

                img = Image.fromarray(frame, "RGB")
                buf = io.BytesIO()
                img.save(buf, format="JPEG", quality=80)
                jpg = buf.getvalue()

                payload = (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n"
                    b"X-Frame-Index: " + str(rolling_idx).encode() + b"\r\n"
                    b"Content-Length: " + str(len(jpg)).encode() + b"\r\n\r\n"
                    + jpg
                    + b"\r\n"
                )

                try:
                    self.connection.sendall(payload)
                    send_ts = time.perf_counter()  # Log time stamps right as kernel takes over
                except Exception:
                    break

                # Store timestamps before tracking receipt
                with telemetry_lock:
                    telemetry_registry[rolling_idx] = {
                        "capture_ts": capture_ts,
                        "send_ts": send_ts
                    }

                sent += 1
                print(f"[client {client_id}] sent frame #{sent} (Rolling Index: {rolling_idx})")

        finally:
            self._cleanup_client(client_id, my_generation)

    def _cleanup_client(self, client_id, my_generation):
        global current_client_id
        with state_lock:
            if current_client_id == client_id and active_generation == my_generation:
                current_client_id = None
                print(f"[DEBUG][client {client_id}] ===== Camera cleanly released =====")

    # -------------------------------------------------
    # Cross-Linked WebSocket Channel Implementation
    # -------------------------------------------------
    def _handle_websocket(self):
        global active_generation, current_client_id
        client_id = id(self)
        
        key = self.headers.get("Sec-WebSocket-Key")
        guid = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
        accept_key = base64.b64encode(hashlib.sha1((key + guid).encode()).digest()).decode()

        self.wfile.write(b"HTTP/1.1 101 Switching Protocols\r\n")
        self.wfile.write(b"Upgrade: websocket\r\n")
        self.wfile.write(b"Connection: Upgrade\r\n")
        self.wfile.write(f"Sec-WebSocket-Accept: {accept_key}\r\n\r\n".encode())
        self.wfile.flush()

        with state_lock:
            my_ws_generation = active_generation

        while True:
            try:
                header = self.rfile.read(2)
                if not header or len(header) < 2:
                    break
                
                b1, b2 = header[0], header[1]
                opcode = b1 & 0x0F
                if opcode == 0x8:
                    break

                payload_len = b2 & 0x7F
                if payload_len == 126:
                    payload_len = struct.unpack(">H", self.rfile.read(2))[0]
                elif payload_len == 127:
                    payload_len = struct.unpack(">Q", self.rfile.read(8))[0]

                mask_key = self.rfile.read(4)
                masked_data = self.rfile.read(payload_len)
                
                unmasked = bytearray(payload_len)
                for i in range(payload_len):
                    unmasked[i] = masked_data[i] ^ mask_key[i % 4]

                message = unmasked.decode("utf-8", errors="ignore")
                recv_ts = time.perf_counter()  # Snap frame rendering confirmation arrival timestamp

                # Process the message telemetry payload
                try:
                    data = json.loads(message)
                    if data.get("event") == "rendered":
                        target_idx = int(data.get("index"))
                        
                        # Match receipt against rolling table registry
                        with telemetry_lock:
                            record = telemetry_registry.get(target_idx)
                        
                        if record:
                            cap_ts = record["capture_ts"]
                            snd_ts = record["send_ts"]
                            
                            # Convert system perf markers to precise millisecond intervals
                            latency_total = (recv_ts - cap_ts) * 1000.0
                            latency_network = (recv_ts - snd_ts) * 1000.0
                            
                            print(
                                f"[Telemetry][Frame #{target_idx}] "
                                f"Timestamps -> Cap: {cap_ts:.4f}, Snd: {snd_ts:.4f}, Recv: {recv_ts:.4f} | "
                                f"Total Latency (Capture->Render): {latency_total:.2f}ms | "
                                f"Network Latency (Send->Render): {latency_network:.2f}ms"
                            )
                except Exception as e:
                    print(f"[Telemetry Error] Parsing failure: {e}")

            except Exception:
                break

        with state_lock:
            if active_generation == my_ws_generation:
                active_generation += 1  
                current_client_id = None  
                print(f"[WebSocket Control] Active generation advanced to {active_generation}. Camera capture halted.")

        print(f"[WebSocket] Channel teardown complete for client {client_id}")


# -------------------------------------------------
# Main entry point
# -------------------------------------------------
if __name__ == "__main__":
    print("[main] starting camera")
    camera.start()

    server = ThreadingHTTPServer(("0.0.0.0", 8000), MultiProtocolHandler)
    print("[server] running multiprotocol stream server on port 8000")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[server] shutting down")
    finally:
        server.server_close()
        camera.stop()