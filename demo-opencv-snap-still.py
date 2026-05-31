import cv2

# Open /dev/video0
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Could not open /dev/video0")

# Grab one frame
ret, frame = cap.read()
if not ret:
    raise RuntimeError("Failed to capture image")

# Save to file
cv2.imwrite("test.jpg", frame)

cap.release()
print("Saved test.jpg")
