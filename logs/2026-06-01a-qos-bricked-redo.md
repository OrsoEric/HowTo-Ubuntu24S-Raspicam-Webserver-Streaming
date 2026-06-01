The QoS bricked

Why webserver_timestamp doesn't work? It's not there... Yesterday it worked

Anyway redone on 
python demo-libcamera-webserver-http-mjpg-disconnect.py

I implemented the part where it sends frame index to client, and client sends message back when it's drawn.

It stops stream when page closes

It restarts.

<details>
<summary>Log</summary>

```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ python demo-libcamera-webserver-http-mjpg-disconnect.py
[1:13:03.897109836] [5932]  INFO Camera camera_manager.cpp:340 libcamera v0.7.1+rpt20260429
[1:13:03.897890612] [5936]  INFO IPAManager ipa_manager.cpp:148 libcamera is not installed. Adding '/home/sona/libcamera/build/src/ipa' to the IPA search path
[1:13:03.961865125] [5936]  INFO IPAProxy ipa_proxy.cpp:73 libcamera is not installed. Loading IPA configuration from '/home/sona/libcamera/src/ipa/rpi/vc4/data'
[1:13:03.961960900] [5936]  INFO IPAProxy ipa_proxy.cpp:184 Using tuning file /home/sona/libcamera/src/ipa/rpi/vc4/data/imx219.json
[1:13:03.969931079] [5936]  INFO Camera camera_manager.cpp:223 Adding camera '/base/soc/i2c0mux/i2c@1/imx219@10' for pipeline handler rpi/vc4
[1:13:03.970023872] [5936]  INFO RPI vc4.cpp:445 Registered camera /base/soc/i2c0mux/i2c@1/imx219@10 to Unicam device /dev/media0 and ISP device /dev/media2
[main] starting camera
[1:13:03.971060882] [5932]  INFO Camera camera.cpp:1216 configuring streams: (0) 1640x1232-RGB888/sRGB
[1:13:03.971639978] [5936]  INFO RPI vc4.cpp:620 Sensor: /base/soc/i2c0mux/i2c@1/imx219@10 - Selected sensor format: 1640x1232-SBGGR10_1X10/RAW - Selected unicam format: 1640x1232-pBAA/RAW
[warmup] frame 0 done
[warmup] frame 1 done
[warmup] frame 2 done
[warmup] frame 3 done
[warmup] frame 4 done
[server] running multiprotocol stream server on port 8000
[DEBUG][client 281472809156576] ===== Granted Camera Ownership (Gen 1) =====
[capture] frame #1
[WebSocket] Incoming handshake negotiation request from client 281472809457168
[WebSocket] Connection channel up and upgraded successfully for client 281472809457168
[capture] frame #2
[capture] frame #3
[capture] frame #4
[capture] frame #5
[capture] frame #6
[client 281472809156576] sent frame #1 (App Index: 1)
[capture] frame #7
[capture] frame #8
[client 281472809156576] sent frame #2 (App Index: 7)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":1}
[capture] frame #9
[client 281472809156576] sent frame #3 (App Index: 9)
[capture] frame #10
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":7}
[client 281472809156576] sent frame #4 (App Index: 10)
[capture] frame #11
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":9}
[client 281472809156576] sent frame #5 (App Index: 11)
[capture] frame #12
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":10}
[client 281472809156576] sent frame #6 (App Index: 12)
[capture] frame #13
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":11}
[client 281472809156576] sent frame #7 (App Index: 13)
[capture] frame #14
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":12}
[client 281472809156576] sent frame #8 (App Index: 14)
[capture] frame #15
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":13}
[client 281472809156576] sent frame #9 (App Index: 15)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":14}
[capture] frame #16
[client 281472809156576] sent frame #10 (App Index: 16)
[capture] frame #17
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":15}
[client 281472809156576] sent frame #11 (App Index: 17)
[capture] frame #18
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":16}
[client 281472809156576] sent frame #12 (App Index: 18)
[capture] frame #19
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":17}
[client 281472809156576] sent frame #13 (App Index: 19)
[capture] frame #20
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":18}
[client 281472809156576] sent frame #14 (App Index: 20)
[capture] frame #21
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":19}
[client 281472809156576] sent frame #15 (App Index: 21)
[capture] frame #22
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":20}
[client 281472809156576] sent frame #16 (App Index: 22)
[capture] frame #23
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":21}
[client 281472809156576] sent frame #17 (App Index: 23)
[capture] frame #24
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":22}
[client 281472809156576] sent frame #18 (App Index: 24)
[capture] frame #25
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":23}
[client 281472809156576] sent frame #19 (App Index: 25)
[capture] frame #26
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":24}
[client 281472809156576] sent frame #20 (App Index: 26)
[capture] frame #27
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":25}
[client 281472809156576] sent frame #21 (App Index: 27)
[capture] frame #28
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":26}
[client 281472809156576] sent frame #22 (App Index: 28)
[capture] frame #29
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":27}
[client 281472809156576] sent frame #23 (App Index: 29)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":28}
[capture] frame #30
[client 281472809156576] sent frame #24 (App Index: 30)
[capture] frame #31
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":29}
[client 281472809156576] sent frame #25 (App Index: 31)
[capture] frame #32
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":30}
[client 281472809156576] sent frame #26 (App Index: 32)
[capture] frame #33
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":31}
[client 281472809156576] sent frame #27 (App Index: 33)
[capture] frame #34
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":32}
[client 281472809156576] sent frame #28 (App Index: 34)
[capture] frame #35
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":33}
[client 281472809156576] sent frame #29 (App Index: 35)
[capture] frame #36
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":34}
[client 281472809156576] sent frame #30 (App Index: 36)
[capture] frame #37
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":35}
[client 281472809156576] sent frame #31 (App Index: 37)
[capture] frame #38
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":36}
[client 281472809156576] sent frame #32 (App Index: 38)
[capture] frame #39
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":37}
[client 281472809156576] sent frame #33 (App Index: 39)
[capture] frame #40
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":38}
[client 281472809156576] sent frame #34 (App Index: 40)
[capture] frame #41
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":39}
[client 281472809156576] sent frame #35 (App Index: 41)
[capture] frame #42
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":40}
[client 281472809156576] sent frame #36 (App Index: 42)
[capture] frame #43
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":41}
[client 281472809156576] sent frame #37 (App Index: 43)
[capture] frame #44
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":42}
[client 281472809156576] sent frame #38 (App Index: 44)
[capture] frame #45
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":43}
[client 281472809156576] sent frame #39 (App Index: 45)
[capture] frame #46
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":44}
[client 281472809156576] sent frame #40 (App Index: 46)
[capture] frame #47
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":45}
[client 281472809156576] sent frame #41 (App Index: 47)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":46}
[capture] frame #48
[client 281472809156576] sent frame #42 (App Index: 48)
[capture] frame #49
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":47}
[client 281472809156576] sent frame #43 (App Index: 49)
[capture] frame #50
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":48}
[client 281472809156576] sent frame #44 (App Index: 50)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":49}
[capture] frame #51
[client 281472809156576] sent frame #45 (App Index: 51)
[capture] frame #52
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":50}
[client 281472809156576] sent frame #46 (App Index: 52)
[capture] frame #53
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":51}
[client 281472809156576] sent frame #47 (App Index: 53)
[capture] frame #54
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":52}
[client 281472809156576] sent frame #48 (App Index: 54)
[capture] frame #55
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":53}
[client 281472809156576] sent frame #49 (App Index: 55)
[capture] frame #56
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":54}
[client 281472809156576] sent frame #50 (App Index: 56)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":55}
[capture] frame #57
[client 281472809156576] sent frame #51 (App Index: 57)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":56}
[capture] frame #58
[client 281472809156576] sent frame #52 (App Index: 58)
[capture] frame #59
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":57}
[client 281472809156576] sent frame #53 (App Index: 59)
[capture] frame #60
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":58}
[client 281472809156576] sent frame #54 (App Index: 60)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":59}
[capture] frame #61
[client 281472809156576] sent frame #55 (App Index: 61)
[capture] frame #62
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":60}
[client 281472809156576] sent frame #56 (App Index: 62)
[capture] frame #63
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":61}
[client 281472809156576] sent frame #57 (App Index: 63)
[capture] frame #64
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":62}
[client 281472809156576] sent frame #58 (App Index: 64)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":63}
[capture] frame #65
[client 281472809156576] sent frame #59 (App Index: 65)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":64}
[capture] frame #66
[client 281472809156576] sent frame #60 (App Index: 66)
[capture] frame #67
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":65}
[client 281472809156576] sent frame #61 (App Index: 67)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":66}
[capture] frame #68
[client 281472809156576] sent frame #62 (App Index: 68)
[capture] frame #69
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":67}
[client 281472809156576] sent frame #63 (App Index: 69)
[capture] frame #70
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":68}
[client 281472809156576] sent frame #64 (App Index: 70)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":69}
[capture] frame #71
[client 281472809156576] sent frame #65 (App Index: 71)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":70}
[capture] frame #72
[client 281472809156576] sent frame #66 (App Index: 72)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":71}
[capture] frame #73
[client 281472809156576] sent frame #67 (App Index: 73)
[capture] frame #74
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":72}
[client 281472809156576] sent frame #68 (App Index: 74)
[capture] frame #75
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":73}
[client 281472809156576] sent frame #69 (App Index: 75)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":74}
[capture] frame #76
[client 281472809156576] sent frame #70 (App Index: 76)
[capture] frame #77
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":75}
[client 281472809156576] sent frame #71 (App Index: 77)
[capture] frame #78
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":76}
[client 281472809156576] sent frame #72 (App Index: 78)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":77}
[capture] frame #79
[client 281472809156576] sent frame #73 (App Index: 79)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":78}
[capture] frame #80
[client 281472809156576] sent frame #74 (App Index: 80)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":79}
[capture] frame #81
[client 281472809156576] sent frame #75 (App Index: 81)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":80}
[capture] frame #82
[client 281472809156576] sent frame #76 (App Index: 82)
[capture] frame #83
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":81}
[client 281472809156576] sent frame #77 (App Index: 83)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":82}
[capture] frame #84
[client 281472809156576] sent frame #78 (App Index: 84)
[capture] frame #85
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":83}
[client 281472809156576] sent frame #79 (App Index: 85)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":84}
[capture] frame #86
[client 281472809156576] sent frame #80 (App Index: 86)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":85}
[capture] frame #87
[client 281472809156576] sent frame #81 (App Index: 87)
[capture] frame #88
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":86}
[client 281472809156576] sent frame #82 (App Index: 88)
[capture] frame #89
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":87}
[client 281472809156576] sent frame #83 (App Index: 89)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":88}
[capture] frame #90
[client 281472809156576] sent frame #84 (App Index: 90)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":89}
[capture] frame #91
[client 281472809156576] sent frame #85 (App Index: 91)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":90}
[capture] frame #92
[client 281472809156576] sent frame #86 (App Index: 92)
[capture] frame #93
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":91}
[client 281472809156576] sent frame #87 (App Index: 93)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":92}
[capture] frame #94
[client 281472809156576] sent frame #88 (App Index: 94)
[capture] frame #95
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":93}
[client 281472809156576] sent frame #89 (App Index: 95)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":94}
[capture] frame #96
[client 281472809156576] sent frame #90 (App Index: 96)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":95}
[capture] frame #97
[client 281472809156576] sent frame #91 (App Index: 97)
[capture] frame #98
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":96}
[client 281472809156576] sent frame #92 (App Index: 98)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":97}
[capture] frame #99
[client 281472809156576] sent frame #93 (App Index: 99)
[capture] frame #100
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":98}
[client 281472809156576] sent frame #94 (App Index: 100)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":99}
[capture] frame #101
[client 281472809156576] sent frame #95 (App Index: 101)
[capture] frame #102
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":100}
[client 281472809156576] sent frame #96 (App Index: 102)
[capture] frame #103
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":101}
[client 281472809156576] sent frame #97 (App Index: 103)
[capture] frame #104
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":102}
[client 281472809156576] sent frame #98 (App Index: 104)
[capture] frame #105
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":103}
[client 281472809156576] sent frame #99 (App Index: 105)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":104}
[capture] frame #106
[client 281472809156576] sent frame #100 (App Index: 106)
[capture] frame #107
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":105}
[client 281472809156576] sent frame #101 (App Index: 107)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":106}
[capture] frame #108
[client 281472809156576] sent frame #102 (App Index: 108)
[capture] frame #109
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":107}
[client 281472809156576] sent frame #103 (App Index: 109)
[capture] frame #110
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":108}
[client 281472809156576] sent frame #104 (App Index: 110)
[capture] frame #111
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":109}
[client 281472809156576] sent frame #105 (App Index: 111)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":110}
[capture] frame #112
[client 281472809156576] sent frame #106 (App Index: 112)
[capture] frame #113
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":111}
[client 281472809156576] sent frame #107 (App Index: 113)
[capture] frame #114
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":112}
[client 281472809156576] sent frame #108 (App Index: 114)
[capture] frame #115
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":113}
[client 281472809156576] sent frame #109 (App Index: 115)
[capture] frame #116
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":114}
[client 281472809156576] sent frame #110 (App Index: 116)
[capture] frame #117
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":115}
[client 281472809156576] sent frame #111 (App Index: 117)
[capture] frame #118
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":116}
[client 281472809156576] sent frame #112 (App Index: 118)
[capture] frame #119
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":117}
[client 281472809156576] sent frame #113 (App Index: 119)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":118}
[capture] frame #120
[client 281472809156576] sent frame #114 (App Index: 120)
[capture] frame #121
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":119}
[client 281472809156576] sent frame #115 (App Index: 121)
[capture] frame #122
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":120}
[client 281472809156576] sent frame #116 (App Index: 122)
[capture] frame #123
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":121}
[client 281472809156576] sent frame #117 (App Index: 123)
[capture] frame #124
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":122}
[client 281472809156576] sent frame #118 (App Index: 124)
[capture] frame #125
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":123}
[client 281472809156576] sent frame #119 (App Index: 125)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":124}
[capture] frame #126
[client 281472809156576] sent frame #120 (App Index: 126)
[capture] frame #127
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":125}
[client 281472809156576] sent frame #121 (App Index: 127)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":126}
[capture] frame #128
[client 281472809156576] sent frame #122 (App Index: 128)
[capture] frame #129
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":127}
[client 281472809156576] sent frame #123 (App Index: 129)
[capture] frame #130
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":128}
[client 281472809156576] sent frame #124 (App Index: 130)
[capture] frame #131
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":129}
[client 281472809156576] sent frame #125 (App Index: 131)
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":130}
[capture] frame #132
[client 281472809156576] sent frame #126 (App Index: 132)
[capture] frame #133
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":131}
[client 281472809156576] sent frame #127 (App Index: 133)
[capture] frame #134
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":132}
[client 281472809156576] sent frame #128 (App Index: 134)
[capture] frame #135
[WebSocket Feedback][client 281472809457168] -> RECEIVED: {"event":"rendered","index":133}
[client 281472809156576] sent frame #129 (App Index: 135)
[capture] frame #136
[WebSocket] Client 281472809457168 sent graceful socket close frame.
[WebSocket Control] Active generation advanced to 2. Camera capture halted.
[WebSocket] Channel teardown complete for client 281472809457168
[client 281472809156576] sent frame #130 (App Index: 136)
[DEBUG][client 281472809156576] Loop stopped: Evicted/Disconnected by state change.
[capture] frame #137
[DEBUG][client 281472809458416] ===== Granted Camera Ownership (Gen 3) =====
[capture] frame #138
[WebSocket] Incoming handshake negotiation request from client 281472765855552
[WebSocket] Connection channel up and upgraded successfully for client 281472765855552
[capture] frame #139
[capture] frame #140
[client 281472809458416] sent frame #1 (App Index: 138)
[capture] frame #141
[capture] frame #142
[capture] frame #143
[client 281472809458416] sent frame #2 (App Index: 142)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":138}
[capture] frame #144
[client 281472809458416] sent frame #3 (App Index: 144)
[capture] frame #145
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":142}
[client 281472809458416] sent frame #4 (App Index: 145)
[capture] frame #146
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":144}
[client 281472809458416] sent frame #5 (App Index: 146)
[capture] frame #147
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":145}
[client 281472809458416] sent frame #6 (App Index: 147)
[capture] frame #148
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":146}
[client 281472809458416] sent frame #7 (App Index: 148)
[capture] frame #149
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":147}
[client 281472809458416] sent frame #8 (App Index: 149)
[capture] frame #150
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":148}
[client 281472809458416] sent frame #9 (App Index: 150)
[capture] frame #151
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":149}
[client 281472809458416] sent frame #10 (App Index: 151)
[capture] frame #152
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":150}
[client 281472809458416] sent frame #11 (App Index: 152)
[capture] frame #153
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":151}
[client 281472809458416] sent frame #12 (App Index: 153)
[capture] frame #154
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":152}
[client 281472809458416] sent frame #13 (App Index: 154)
[capture] frame #155
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":153}
[client 281472809458416] sent frame #14 (App Index: 155)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":154}
[capture] frame #156
[client 281472809458416] sent frame #15 (App Index: 156)
[capture] frame #157
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":155}
[client 281472809458416] sent frame #16 (App Index: 157)
[capture] frame #158
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":156}
[client 281472809458416] sent frame #17 (App Index: 158)
[capture] frame #159
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":157}
[client 281472809458416] sent frame #18 (App Index: 159)
[capture] frame #160
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":158}
[client 281472809458416] sent frame #19 (App Index: 160)
[capture] frame #161
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":159}
[client 281472809458416] sent frame #20 (App Index: 161)
[capture] frame #162
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":160}
[client 281472809458416] sent frame #21 (App Index: 162)
[capture] frame #163
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":161}
[client 281472809458416] sent frame #22 (App Index: 163)
[capture] frame #164
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":162}
[client 281472809458416] sent frame #23 (App Index: 164)
[capture] frame #165
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":163}
[client 281472809458416] sent frame #24 (App Index: 165)
[capture] frame #166
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":164}
[client 281472809458416] sent frame #25 (App Index: 166)
[capture] frame #167
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":165}
[client 281472809458416] sent frame #26 (App Index: 167)
[capture] frame #168
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":166}
[client 281472809458416] sent frame #27 (App Index: 168)
[capture] frame #169
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":167}
[client 281472809458416] sent frame #28 (App Index: 169)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":168}
[capture] frame #170
[client 281472809458416] sent frame #29 (App Index: 170)
[capture] frame #171
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":169}
[client 281472809458416] sent frame #30 (App Index: 171)
[capture] frame #172
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":170}
[capture] frame #173
[client 281472809458416] sent frame #31 (App Index: 173)
[capture] frame #174
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":171}
[client 281472809458416] sent frame #32 (App Index: 174)
[capture] frame #175
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":173}
[client 281472809458416] sent frame #33 (App Index: 175)
[capture] frame #176
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":174}
[client 281472809458416] sent frame #34 (App Index: 176)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":175}
[capture] frame #177
[client 281472809458416] sent frame #35 (App Index: 177)
[capture] frame #178
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":176}
[client 281472809458416] sent frame #36 (App Index: 178)
[capture] frame #179
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":177}
[client 281472809458416] sent frame #37 (App Index: 179)
[capture] frame #180
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":178}
[client 281472809458416] sent frame #38 (App Index: 180)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":179}
[capture] frame #181
[client 281472809458416] sent frame #39 (App Index: 181)
[capture] frame #182
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":180}
[client 281472809458416] sent frame #40 (App Index: 182)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":181}
[capture] frame #183
[client 281472809458416] sent frame #41 (App Index: 183)
[capture] frame #184
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":182}
[client 281472809458416] sent frame #42 (App Index: 184)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":183}
[capture] frame #185
[client 281472809458416] sent frame #43 (App Index: 185)
[capture] frame #186
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":184}
[client 281472809458416] sent frame #44 (App Index: 186)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":185}
[capture] frame #187
[client 281472809458416] sent frame #45 (App Index: 187)
[capture] frame #188
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":186}
[client 281472809458416] sent frame #46 (App Index: 188)
[capture] frame #189
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":187}
[client 281472809458416] sent frame #47 (App Index: 189)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":188}
[capture] frame #190
[client 281472809458416] sent frame #48 (App Index: 190)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":189}
[capture] frame #191
[client 281472809458416] sent frame #49 (App Index: 191)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":190}
[capture] frame #192
[client 281472809458416] sent frame #50 (App Index: 192)
[capture] frame #193
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":191}
[client 281472809458416] sent frame #51 (App Index: 193)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":192}
[capture] frame #194
[client 281472809458416] sent frame #52 (App Index: 194)
[capture] frame #195
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":193}
[client 281472809458416] sent frame #53 (App Index: 195)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":194}
[capture] frame #196
[client 281472809458416] sent frame #54 (App Index: 196)
[capture] frame #197
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":195}
[client 281472809458416] sent frame #55 (App Index: 197)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":196}
[capture] frame #198
[client 281472809458416] sent frame #56 (App Index: 198)
[capture] frame #199
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":197}
[client 281472809458416] sent frame #57 (App Index: 199)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":198}
[capture] frame #200
[client 281472809458416] sent frame #58 (App Index: 200)
[capture] frame #201
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":199}
[client 281472809458416] sent frame #59 (App Index: 201)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":200}
[capture] frame #202
[client 281472809458416] sent frame #60 (App Index: 202)
[capture] frame #203
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":201}
[client 281472809458416] sent frame #61 (App Index: 203)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":202}
[capture] frame #204
[client 281472809458416] sent frame #62 (App Index: 204)
[capture] frame #205
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":203}
[client 281472809458416] sent frame #63 (App Index: 205)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":204}
[capture] frame #206
[client 281472809458416] sent frame #64 (App Index: 206)
[capture] frame #207
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":205}
[client 281472809458416] sent frame #65 (App Index: 207)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":206}
[capture] frame #208
[client 281472809458416] sent frame #66 (App Index: 208)
[capture] frame #209
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":207}
[client 281472809458416] sent frame #67 (App Index: 209)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":208}
[capture] frame #210
[client 281472809458416] sent frame #68 (App Index: 210)
[capture] frame #211
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":209}
[client 281472809458416] sent frame #69 (App Index: 211)
[capture] frame #212
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":210}
[client 281472809458416] sent frame #70 (App Index: 212)
[capture] frame #213
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":211}
[client 281472809458416] sent frame #71 (App Index: 213)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":212}
[capture] frame #214
[client 281472809458416] sent frame #72 (App Index: 214)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":213}
[capture] frame #215
[client 281472809458416] sent frame #73 (App Index: 215)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":214}
[capture] frame #216
[client 281472809458416] sent frame #74 (App Index: 216)
[capture] frame #217
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":215}
[client 281472809458416] sent frame #75 (App Index: 217)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":216}
[capture] frame #218
[client 281472809458416] sent frame #76 (App Index: 218)
[capture] frame #219
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":217}
[client 281472809458416] sent frame #77 (App Index: 219)
[capture] frame #220
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":218}
[client 281472809458416] sent frame #78 (App Index: 220)
[capture] frame #221
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":219}
[client 281472809458416] sent frame #79 (App Index: 221)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":220}
[capture] frame #222
[client 281472809458416] sent frame #80 (App Index: 222)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":221}
[capture] frame #223
[client 281472809458416] sent frame #81 (App Index: 223)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":222}
[capture] frame #224
[client 281472809458416] sent frame #82 (App Index: 224)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":223}
[capture] frame #225
[client 281472809458416] sent frame #83 (App Index: 225)
[capture] frame #226
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":224}
[client 281472809458416] sent frame #84 (App Index: 226)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":225}
[capture] frame #227
[client 281472809458416] sent frame #85 (App Index: 227)
[capture] frame #228
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":226}
[client 281472809458416] sent frame #86 (App Index: 228)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":227}
[capture] frame #229
[client 281472809458416] sent frame #87 (App Index: 229)
[capture] frame #230
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":228}
[client 281472809458416] sent frame #88 (App Index: 230)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":229}
[capture] frame #231
[client 281472809458416] sent frame #89 (App Index: 231)
[capture] frame #232
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":230}
[client 281472809458416] sent frame #90 (App Index: 232)
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":231}
[capture] frame #233
[client 281472809458416] sent frame #91 (App Index: 233)
[capture] frame #234
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":232}
[client 281472809458416] sent frame #92 (App Index: 234)
[capture] frame #235
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":233}
[client 281472809458416] sent frame #93 (App Index: 235)
[capture] frame #236
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":234}
[client 281472809458416] sent frame #94 (App Index: 236)
[capture] frame #237
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":235}
[client 281472809458416] sent frame #95 (App Index: 237)
[capture] frame #238
[WebSocket Feedback][client 281472765855552] -> RECEIVED: {"event":"rendered","index":236}
[client 281472809458416] sent frame #96 (App Index: 238)
[capture] frame #239
[WebSocket] Client 281472765855552 sent graceful socket close frame.
[WebSocket Control] Active generation advanced to 4. Camera capture halted.
[WebSocket] Channel teardown complete for client 281472765855552
[client 281472809458416] sent frame #97 (App Index: 239)
[DEBUG][client 281472809458416] Loop stopped: Evicted/Disconnected by state change.
[capture] frame #240
^C
[server] shutting down
```

</details>

# QoS

 now let's do latency detection.


first, app frame index is 0 to 99 and resets.


then there is a dictionary that stores frame index as key, and three numbers. capture timestamp. client send timestamp. client receive timestamp.


app debug now shows the three timestamp, and twhen a frame index receive is gotten, it prints latency from capture to receive, and from send to receive 

<details>
<summary>Log</summary>

```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ python demo-libcamera-webserver-http-mjpg-disconnect-qos.py
[1:20:27.739432617] [6135]  INFO Camera camera_manager.cpp:340 libcamera v0.7.1+rpt20260429
[1:20:27.740246009] [6139]  INFO IPAManager ipa_manager.cpp:148 libcamera is not installed. Adding '/home/sona/libcamera/build/src/ipa' to the IPA search path
[1:20:27.801085642] [6139]  INFO IPAProxy ipa_proxy.cpp:73 libcamera is not installed. Loading IPA configuration from '/home/sona/libcamera/src/ipa/rpi/vc4/data'
[1:20:27.801181196] [6139]  INFO IPAProxy ipa_proxy.cpp:184 Using tuning file /home/sona/libcamera/src/ipa/rpi/vc4/data/imx219.json
[1:20:27.809114518] [6139]  INFO Camera camera_manager.cpp:223 Adding camera '/base/soc/i2c0mux/i2c@1/imx219@10' for pipeline handler rpi/vc4
[1:20:27.809186980] [6139]  INFO RPI vc4.cpp:445 Registered camera /base/soc/i2c0mux/i2c@1/imx219@10 to Unicam device /dev/media0 and ISP device /dev/media2
[main] starting camera
[1:20:27.810201589] [6135]  INFO Camera camera.cpp:1216 configuring streams: (0) 1640x1232-RGB888/sRGB
[1:20:27.810836780] [6139]  INFO RPI vc4.cpp:620 Sensor: /base/soc/i2c0mux/i2c@1/imx219@10 - Selected sensor format: 1640x1232-SBGGR10_1X10/RAW - Selected unicam format: 1640x1232-pBAA/RAW
[warmup] frame 0 done
[warmup] frame 1 done
[warmup] frame 2 done
[warmup] frame 3 done
[warmup] frame 4 done
[server] running multiprotocol stream server on port 8000
[DEBUG][client 281472943008192] ===== Granted Camera Ownership (Gen 1) =====
[capture] frame #1
[capture] frame #2
[capture] frame #3
[capture] frame #4
[capture] frame #5
[client 281472943008192] sent frame #1 (Rolling Index: 1)
[capture] frame #6
[capture] frame #7
[client 281472943008192] sent frame #2 (Rolling Index: 6)
[Telemetry][Frame #1] Timestamps -> Cap: 4832.0466, Snd: 4832.2260, Recv: 4832.3424 | Total Latency (Capture->Render): 295.74ms | Network Latency (Send->Render): 116.33ms
[capture] frame #8
[client 281472943008192] sent frame #3 (Rolling Index: 8)
[capture] frame #9
[Telemetry][Frame #6] Timestamps -> Cap: 4832.2478, Snd: 4832.3122, Recv: 4832.4336 | Total Latency (Capture->Render): 185.84ms | Network Latency (Send->Render): 121.42ms
[client 281472943008192] sent frame #4 (Rolling Index: 9)
[capture] frame #10
[Telemetry][Frame #8] Timestamps -> Cap: 4832.3427, Snd: 4832.4137, Recv: 4832.5045 | Total Latency (Capture->Render): 161.84ms | Network Latency (Send->Render): 90.85ms
[client 281472943008192] sent frame #5 (Rolling Index: 10)
[capture] frame #11
[Telemetry][Frame #9] Timestamps -> Cap: 4832.4141, Snd: 4832.4813, Recv: 4832.5714 | Total Latency (Capture->Render): 157.32ms | Network Latency (Send->Render): 90.12ms
[client 281472943008192] sent frame #6 (Rolling Index: 11)
[capture] frame #12
[Telemetry][Frame #10] Timestamps -> Cap: 4832.4824, Snd: 4832.5305, Recv: 4832.6196 | Total Latency (Capture->Render): 137.18ms | Network Latency (Send->Render): 89.06ms
[client 281472943008192] sent frame #7 (Rolling Index: 12)
[capture] frame #13
[Telemetry][Frame #11] Timestamps -> Cap: 4832.5446, Snd: 4832.5890, Recv: 4832.6855 | Total Latency (Capture->Render): 140.89ms | Network Latency (Send->Render): 96.41ms
[client 281472943008192] sent frame #8 (Rolling Index: 13)
[Telemetry][Frame #12] Timestamps -> Cap: 4832.6099, Snd: 4832.6529, Recv: 4832.7453 | Total Latency (Capture->Render): 135.38ms | Network Latency (Send->Render): 92.42ms
[capture] frame #14
[client 281472943008192] sent frame #9 (Rolling Index: 14)
[capture] frame #15
[Telemetry][Frame #13] Timestamps -> Cap: 4832.6747, Snd: 4832.7175, Recv: 4832.8178 | Total Latency (Capture->Render): 143.10ms | Network Latency (Send->Render): 100.34ms
[client 281472943008192] sent frame #10 (Rolling Index: 15)
[capture] frame #16
[Telemetry][Frame #14] Timestamps -> Cap: 4832.7456, Snd: 4832.7863, Recv: 4832.8848 | Total Latency (Capture->Render): 139.18ms | Network Latency (Send->Render): 98.52ms
[client 281472943008192] sent frame #11 (Rolling Index: 16)
[capture] frame #17
[Telemetry][Frame #15] Timestamps -> Cap: 4832.8113, Snd: 4832.8545, Recv: 4832.9519 | Total Latency (Capture->Render): 140.66ms | Network Latency (Send->Render): 97.46ms
[client 281472943008192] sent frame #12 (Rolling Index: 17)
[capture] frame #18
[Telemetry][Frame #16] Timestamps -> Cap: 4832.8777, Snd: 4832.9206, Recv: 4833.0240 | Total Latency (Capture->Render): 146.32ms | Network Latency (Send->Render): 103.40ms
[client 281472943008192] sent frame #13 (Rolling Index: 18)
[Telemetry][Frame #17] Timestamps -> Cap: 4832.9430, Snd: 4832.9869, Recv: 4833.0808 | Total Latency (Capture->Render): 137.79ms | Network Latency (Send->Render): 93.85ms
[capture] frame #19
[client 281472943008192] sent frame #14 (Rolling Index: 19)
[capture] frame #20
[Telemetry][Frame #18] Timestamps -> Cap: 4833.0115, Snd: 4833.0540, Recv: 4833.1582 | Total Latency (Capture->Render): 146.77ms | Network Latency (Send->Render): 104.20ms
[client 281472943008192] sent frame #15 (Rolling Index: 20)
[capture] frame #21
[Telemetry][Frame #19] Timestamps -> Cap: 4833.0811, Snd: 4833.1236, Recv: 4833.2177 | Total Latency (Capture->Render): 136.69ms | Network Latency (Send->Render): 94.11ms
[client 281472943008192] sent frame #16 (Rolling Index: 21)
[capture] frame #22
[Telemetry][Frame #20] Timestamps -> Cap: 4833.1448, Snd: 4833.1881, Recv: 4833.2843 | Total Latency (Capture->Render): 139.48ms | Network Latency (Send->Render): 96.22ms
[client 281472943008192] sent frame #17 (Rolling Index: 22)
[Telemetry][Frame #21] Timestamps -> Cap: 4833.2100, Snd: 4833.2524, Recv: 4833.3503 | Total Latency (Capture->Render): 140.32ms | Network Latency (Send->Render): 97.91ms
[capture] frame #23
[client 281472943008192] sent frame #18 (Rolling Index: 23)
[capture] frame #24
[Telemetry][Frame #22] Timestamps -> Cap: 4833.2777, Snd: 4833.3207, Recv: 4833.4310 | Total Latency (Capture->Render): 153.26ms | Network Latency (Send->Render): 110.24ms
[client 281472943008192] sent frame #19 (Rolling Index: 24)
[capture] frame #25
[Telemetry][Frame #23] Timestamps -> Cap: 4833.3506, Snd: 4833.3928, Recv: 4833.4844 | Total Latency (Capture->Render): 133.85ms | Network Latency (Send->Render): 91.61ms
[client 281472943008192] sent frame #20 (Rolling Index: 25)
[capture] frame #26
[Telemetry][Frame #24] Timestamps -> Cap: 4833.4092, Snd: 4833.4541, Recv: 4833.5578 | Total Latency (Capture->Render): 148.56ms | Network Latency (Send->Render): 103.65ms
[client 281472943008192] sent frame #21 (Rolling Index: 26)
[capture] frame #27
[Telemetry][Frame #25] Timestamps -> Cap: 4833.4830, Snd: 4833.5249, Recv: 4833.6295 | Total Latency (Capture->Render): 146.49ms | Network Latency (Send->Render): 104.66ms
[client 281472943008192] sent frame #22 (Rolling Index: 27)
[Telemetry][Frame #26] Timestamps -> Cap: 4833.5433, Snd: 4833.5889, Recv: 4833.6784 | Total Latency (Capture->Render): 135.06ms | Network Latency (Send->Render): 89.45ms
[capture] frame #28
[client 281472943008192] sent frame #23 (Rolling Index: 28)
[capture] frame #29
[Telemetry][Frame #27] Timestamps -> Cap: 4833.6087, Snd: 4833.6527, Recv: 4833.7522 | Total Latency (Capture->Render): 143.49ms | Network Latency (Send->Render): 99.56ms
[client 281472943008192] sent frame #24 (Rolling Index: 29)
[capture] frame #30
[Telemetry][Frame #28] Timestamps -> Cap: 4833.6787, Snd: 4833.7218, Recv: 4833.8148 | Total Latency (Capture->Render): 136.12ms | Network Latency (Send->Render): 93.03ms
[client 281472943008192] sent frame #25 (Rolling Index: 30)
[capture] frame #31
[Telemetry][Frame #29] Timestamps -> Cap: 4833.7446, Snd: 4833.7882, Recv: 4833.8854 | Total Latency (Capture->Render): 140.89ms | Network Latency (Send->Render): 97.28ms
[client 281472943008192] sent frame #26 (Rolling Index: 31)
[Telemetry][Frame #30] Timestamps -> Cap: 4833.8127, Snd: 4833.8548, Recv: 4833.9485 | Total Latency (Capture->Render): 135.82ms | Network Latency (Send->Render): 93.69ms
[capture] frame #32
[client 281472943008192] sent frame #27 (Rolling Index: 32)
[capture] frame #33
[Telemetry][Frame #31] Timestamps -> Cap: 4833.8770, Snd: 4833.9198, Recv: 4834.0251 | Total Latency (Capture->Render): 148.11ms | Network Latency (Send->Render): 105.38ms
[client 281472943008192] sent frame #28 (Rolling Index: 33)
[capture] frame #34
[Telemetry][Frame #32] Timestamps -> Cap: 4833.9488, Snd: 4833.9907, Recv: 4834.0865 | Total Latency (Capture->Render): 137.78ms | Network Latency (Send->Render): 95.83ms
[client 281472943008192] sent frame #29 (Rolling Index: 34)
[capture] frame #35
[Telemetry][Frame #33] Timestamps -> Cap: 4834.0109, Snd: 4834.0546, Recv: 4834.1582 | Total Latency (Capture->Render): 147.33ms | Network Latency (Send->Render): 103.59ms
[client 281472943008192] sent frame #30 (Rolling Index: 35)
[capture] frame #36
[Telemetry][Frame #34] Timestamps -> Cap: 4834.0822, Snd: 4834.1250, Recv: 4834.2161 | Total Latency (Capture->Render): 133.90ms | Network Latency (Send->Render): 91.17ms
[client 281472943008192] sent frame #31 (Rolling Index: 36)
[capture] frame #37
[Telemetry][Frame #35] Timestamps -> Cap: 4834.1424, Snd: 4834.1882, Recv: 4834.2815 | Total Latency (Capture->Render): 139.07ms | Network Latency (Send->Render): 93.22ms
[client 281472943008192] sent frame #32 (Rolling Index: 37)
[capture] frame #38
[Telemetry][Frame #36] Timestamps -> Cap: 4834.2096, Snd: 4834.2527, Recv: 4834.3504 | Total Latency (Capture->Render): 140.81ms | Network Latency (Send->Render): 97.72ms
[client 281472943008192] sent frame #33 (Rolling Index: 38)
[Telemetry][Frame #37] Timestamps -> Cap: 4834.2783, Snd: 4834.3198, Recv: 4834.4148 | Total Latency (Capture->Render): 136.52ms | Network Latency (Send->Render): 95.01ms
[capture] frame #39
[client 281472943008192] sent frame #34 (Rolling Index: 39)
[capture] frame #40
[Telemetry][Frame #38] Timestamps -> Cap: 4834.3454, Snd: 4834.3870, Recv: 4834.4906 | Total Latency (Capture->Render): 145.14ms | Network Latency (Send->Render): 103.58ms
[client 281472943008192] sent frame #35 (Rolling Index: 40)
[capture] frame #41
[Telemetry][Frame #39] Timestamps -> Cap: 4834.4151, Snd: 4834.4599, Recv: 4834.5512 | Total Latency (Capture->Render): 136.12ms | Network Latency (Send->Render): 91.34ms
[client 281472943008192] sent frame #36 (Rolling Index: 41)
[capture] frame #42
[Telemetry][Frame #40] Timestamps -> Cap: 4834.4763, Snd: 4834.5198, Recv: 4834.6193 | Total Latency (Capture->Render): 142.99ms | Network Latency (Send->Render): 99.48ms
[client 281472943008192] sent frame #37 (Rolling Index: 42)
[capture] frame #43
[Telemetry][Frame #41] Timestamps -> Cap: 4834.5466, Snd: 4834.5883, Recv: 4834.6860 | Total Latency (Capture->Render): 139.45ms | Network Latency (Send->Render): 97.74ms
[client 281472943008192] sent frame #38 (Rolling Index: 43)
[capture] frame #44
[Telemetry][Frame #42] Timestamps -> Cap: 4834.6119, Snd: 4834.6549, Recv: 4834.7514 | Total Latency (Capture->Render): 139.44ms | Network Latency (Send->Render): 96.45ms
[client 281472943008192] sent frame #39 (Rolling Index: 44)
[capture] frame #45
[Telemetry][Frame #43] Timestamps -> Cap: 4834.6772, Snd: 4834.7198, Recv: 4834.8147 | Total Latency (Capture->Render): 137.51ms | Network Latency (Send->Render): 94.88ms
[client 281472943008192] sent frame #40 (Rolling Index: 45)
[capture] frame #46
[Telemetry][Frame #44] Timestamps -> Cap: 4834.7456, Snd: 4834.7875, Recv: 4834.8811 | Total Latency (Capture->Render): 135.55ms | Network Latency (Send->Render): 93.61ms
[client 281472943008192] sent frame #41 (Rolling Index: 46)
[capture] frame #47
[Telemetry][Frame #45] Timestamps -> Cap: 4834.8096, Snd: 4834.8522, Recv: 4834.9482 | Total Latency (Capture->Render): 138.52ms | Network Latency (Send->Render): 95.94ms
[client 281472943008192] sent frame #42 (Rolling Index: 47)
[capture] frame #48
[Telemetry][Frame #46] Timestamps -> Cap: 4834.8774, Snd: 4834.9196, Recv: 4835.0161 | Total Latency (Capture->Render): 138.72ms | Network Latency (Send->Render): 96.48ms
[client 281472943008192] sent frame #43 (Rolling Index: 48)
[capture] frame #49
[Telemetry][Frame #47] Timestamps -> Cap: 4834.9463, Snd: 4834.9882, Recv: 4835.0850 | Total Latency (Capture->Render): 138.70ms | Network Latency (Send->Render): 96.78ms
[client 281472943008192] sent frame #44 (Rolling Index: 49)
[capture] frame #50
[Telemetry][Frame #48] Timestamps -> Cap: 4835.0155, Snd: 4835.0570, Recv: 4835.1448 | Total Latency (Capture->Render): 129.31ms | Network Latency (Send->Render): 87.87ms
[client 281472943008192] sent frame #45 (Rolling Index: 50)
[capture] frame #51
[Telemetry][Frame #49] Timestamps -> Cap: 4835.0769, Snd: 4835.1192, Recv: 4835.2196 | Total Latency (Capture->Render): 142.67ms | Network Latency (Send->Render): 100.34ms
[client 281472943008192] sent frame #46 (Rolling Index: 51)
[capture] frame #52
[Telemetry][Frame #50] Timestamps -> Cap: 4835.1443, Snd: 4835.1862, Recv: 4835.2803 | Total Latency (Capture->Render): 135.98ms | Network Latency (Send->Render): 94.06ms
[client 281472943008192] sent frame #47 (Rolling Index: 52)
[capture] frame #53
[Telemetry][Frame #51] Timestamps -> Cap: 4835.2112, Snd: 4835.2538, Recv: 4835.3540 | Total Latency (Capture->Render): 142.84ms | Network Latency (Send->Render): 100.15ms
[client 281472943008192] sent frame #48 (Rolling Index: 53)
[capture] frame #54
[Telemetry][Frame #52] Timestamps -> Cap: 4835.2794, Snd: 4835.3213, Recv: 4835.4252 | Total Latency (Capture->Render): 145.82ms | Network Latency (Send->Render): 103.88ms
[client 281472943008192] sent frame #49 (Rolling Index: 54)
[Telemetry][Frame #53] Timestamps -> Cap: 4835.3476, Snd: 4835.3914, Recv: 4835.4831 | Total Latency (Capture->Render): 135.50ms | Network Latency (Send->Render): 91.75ms
[capture] frame #55
[client 281472943008192] sent frame #50 (Rolling Index: 55)
[capture] frame #56
[Telemetry][Frame #54] Timestamps -> Cap: 4835.4125, Snd: 4835.4568, Recv: 4835.5606 | Total Latency (Capture->Render): 148.11ms | Network Latency (Send->Render): 103.81ms
[client 281472943008192] sent frame #51 (Rolling Index: 56)
[capture] frame #57
[Telemetry][Frame #55] Timestamps -> Cap: 4835.4834, Snd: 4835.5267, Recv: 4835.6262 | Total Latency (Capture->Render): 142.82ms | Network Latency (Send->Render): 99.51ms
[client 281472943008192] sent frame #52 (Rolling Index: 57)
[capture] frame #58
[Telemetry][Frame #56] Timestamps -> Cap: 4835.5472, Snd: 4835.5929, Recv: 4835.7001 | Total Latency (Capture->Render): 152.95ms | Network Latency (Send->Render): 107.20ms
[client 281472943008192] sent frame #53 (Rolling Index: 58)
[capture] frame #59
[Telemetry][Frame #57] Timestamps -> Cap: 4835.6140, Snd: 4835.6608, Recv: 4835.7573 | Total Latency (Capture->Render): 143.37ms | Network Latency (Send->Render): 96.54ms
[client 281472943008192] sent frame #54 (Rolling Index: 59)
[capture] frame #60
[Telemetry][Frame #58] Timestamps -> Cap: 4835.6785, Snd: 4835.7232, Recv: 4835.8207 | Total Latency (Capture->Render): 142.16ms | Network Latency (Send->Render): 97.52ms
[client 281472943008192] sent frame #55 (Rolling Index: 60)
[capture] frame #61
[Telemetry][Frame #59] Timestamps -> Cap: 4835.7473, Snd: 4835.7898, Recv: 4835.8874 | Total Latency (Capture->Render): 140.09ms | Network Latency (Send->Render): 97.55ms
[client 281472943008192] sent frame #56 (Rolling Index: 61)
[Telemetry][Frame #60] Timestamps -> Cap: 4835.8135, Snd: 4835.8561, Recv: 4835.9515 | Total Latency (Capture->Render): 138.00ms | Network Latency (Send->Render): 95.34ms
[capture] frame #62
[client 281472943008192] sent frame #57 (Rolling Index: 62)
[capture] frame #63
[Telemetry][Frame #61] Timestamps -> Cap: 4835.8786, Snd: 4835.9210, Recv: 4836.0282 | Total Latency (Capture->Render): 149.56ms | Network Latency (Send->Render): 107.18ms
[client 281472943008192] sent frame #58 (Rolling Index: 63)
[capture] frame #64
[Telemetry][Frame #62] Timestamps -> Cap: 4835.9517, Snd: 4835.9966, Recv: 4836.1081 | Total Latency (Capture->Render): 156.36ms | Network Latency (Send->Render): 111.52ms
[client 281472943008192] sent frame #59 (Rolling Index: 64)
[capture] frame #65
[Telemetry][Frame #63] Timestamps -> Cap: 4836.0107, Snd: 4836.0840, Recv: 4836.1671 | Total Latency (Capture->Render): 156.46ms | Network Latency (Send->Render): 83.11ms
[client 281472943008192] sent frame #60 (Rolling Index: 65)
[Telemetry][Frame #64] Timestamps -> Cap: 4836.0844, Snd: 4836.1315, Recv: 4836.2184 | Total Latency (Capture->Render): 134.06ms | Network Latency (Send->Render): 86.95ms
[capture] frame #66
[client 281472943008192] sent frame #61 (Rolling Index: 66)
[capture] frame #67
[Telemetry][Frame #65] Timestamps -> Cap: 4836.1447, Snd: 4836.1899, Recv: 4836.2899 | Total Latency (Capture->Render): 145.19ms | Network Latency (Send->Render): 99.95ms
[client 281472943008192] sent frame #62 (Rolling Index: 67)
[capture] frame #68
[Telemetry][Frame #66] Timestamps -> Cap: 4836.2187, Snd: 4836.2611, Recv: 4836.3512 | Total Latency (Capture->Render): 132.50ms | Network Latency (Send->Render): 90.12ms
[client 281472943008192] sent frame #63 (Rolling Index: 68)
[capture] frame #69
[Telemetry][Frame #67] Timestamps -> Cap: 4836.2802, Snd: 4836.3247, Recv: 4836.4227 | Total Latency (Capture->Render): 142.44ms | Network Latency (Send->Render): 98.01ms
[client 281472943008192] sent frame #64 (Rolling Index: 69)
[capture] frame #70
[Telemetry][Frame #68] Timestamps -> Cap: 4836.3482, Snd: 4836.3913, Recv: 4836.4862 | Total Latency (Capture->Render): 138.02ms | Network Latency (Send->Render): 94.91ms
[client 281472943008192] sent frame #65 (Rolling Index: 70)
[capture] frame #71
[Telemetry][Frame #69] Timestamps -> Cap: 4836.4123, Snd: 4836.4553, Recv: 4836.5516 | Total Latency (Capture->Render): 139.28ms | Network Latency (Send->Render): 96.30ms
[client 281472943008192] sent frame #66 (Rolling Index: 71)
[capture] frame #72
[Telemetry][Frame #70] Timestamps -> Cap: 4836.4787, Snd: 4836.5217, Recv: 4836.6223 | Total Latency (Capture->Render): 143.52ms | Network Latency (Send->Render): 100.58ms
[client 281472943008192] sent frame #67 (Rolling Index: 72)
[capture] frame #73
[Telemetry][Frame #71] Timestamps -> Cap: 4836.5456, Snd: 4836.5875, Recv: 4836.6851 | Total Latency (Capture->Render): 139.44ms | Network Latency (Send->Render): 97.54ms
[client 281472943008192] sent frame #68 (Rolling Index: 73)
[Telemetry][Frame #72] Timestamps -> Cap: 4836.6130, Snd: 4836.6568, Recv: 4836.7529 | Total Latency (Capture->Render): 139.95ms | Network Latency (Send->Render): 96.09ms
[capture] frame #74
[client 281472943008192] sent frame #69 (Rolling Index: 74)
[capture] frame #75
[Telemetry][Frame #73] Timestamps -> Cap: 4836.6808, Snd: 4836.7231, Recv: 4836.8381 | Total Latency (Capture->Render): 157.26ms | Network Latency (Send->Render): 114.94ms
[client 281472943008192] sent frame #70 (Rolling Index: 75)
[capture] frame #76
[Telemetry][Frame #74] Timestamps -> Cap: 4836.7532, Snd: 4836.7958, Recv: 4836.8843 | Total Latency (Capture->Render): 131.06ms | Network Latency (Send->Render): 88.46ms
[client 281472943008192] sent frame #71 (Rolling Index: 76)
[capture] frame #77
[Telemetry][Frame #75] Timestamps -> Cap: 4836.8111, Snd: 4836.8551, Recv: 4836.9544 | Total Latency (Capture->Render): 143.25ms | Network Latency (Send->Render): 99.27ms
[client 281472943008192] sent frame #72 (Rolling Index: 77)
[Telemetry][Frame #76] Timestamps -> Cap: 4836.8801, Snd: 4836.9231, Recv: 4837.0177 | Total Latency (Capture->Render): 137.62ms | Network Latency (Send->Render): 94.64ms
[capture] frame #78
[client 281472943008192] sent frame #73 (Rolling Index: 78)
[capture] frame #79
[Telemetry][Frame #77] Timestamps -> Cap: 4836.9453, Snd: 4836.9878, Recv: 4837.0912 | Total Latency (Capture->Render): 145.86ms | Network Latency (Send->Render): 103.38ms
[client 281472943008192] sent frame #74 (Rolling Index: 79)
[capture] frame #80
[Telemetry][Frame #78] Timestamps -> Cap: 4837.0181, Snd: 4837.0607, Recv: 4837.1514 | Total Latency (Capture->Render): 133.30ms | Network Latency (Send->Render): 90.70ms
[client 281472943008192] sent frame #75 (Rolling Index: 80)
[capture] frame #81
[Telemetry][Frame #79] Timestamps -> Cap: 4837.0821, Snd: 4837.1248, Recv: 4837.2243 | Total Latency (Capture->Render): 142.16ms | Network Latency (Send->Render): 99.45ms
[client 281472943008192] sent frame #76 (Rolling Index: 81)
[Telemetry][Frame #80] Timestamps -> Cap: 4837.1476, Snd: 4837.1911, Recv: 4837.2837 | Total Latency (Capture->Render): 136.08ms | Network Latency (Send->Render): 92.54ms
[capture] frame #82
[client 281472943008192] sent frame #77 (Rolling Index: 82)
[capture] frame #83
[Telemetry][Frame #81] Timestamps -> Cap: 4837.2133, Snd: 4837.2560, Recv: 4837.3565 | Total Latency (Capture->Render): 143.27ms | Network Latency (Send->Render): 100.55ms
[client 281472943008192] sent frame #78 (Rolling Index: 83)
[capture] frame #84
[Telemetry][Frame #82] Timestamps -> Cap: 4837.2839, Snd: 4837.3258, Recv: 4837.4158 | Total Latency (Capture->Render): 131.85ms | Network Latency (Send->Render): 89.99ms
[client 281472943008192] sent frame #79 (Rolling Index: 84)
[capture] frame #85
[Telemetry][Frame #83] Timestamps -> Cap: 4837.3477, Snd: 4837.3906, Recv: 4837.4897 | Total Latency (Capture->Render): 141.98ms | Network Latency (Send->Render): 99.04ms
[client 281472943008192] sent frame #80 (Rolling Index: 85)
[capture] frame #86
[Telemetry][Frame #84] Timestamps -> Cap: 4837.4152, Snd: 4837.4584, Recv: 4837.5513 | Total Latency (Capture->Render): 136.10ms | Network Latency (Send->Render): 92.87ms
[client 281472943008192] sent frame #81 (Rolling Index: 86)
[capture] frame #87
[Telemetry][Frame #85] Timestamps -> Cap: 4837.4825, Snd: 4837.5251, Recv: 4837.6179 | Total Latency (Capture->Render): 135.39ms | Network Latency (Send->Render): 92.75ms
[client 281472943008192] sent frame #82 (Rolling Index: 87)
[Telemetry][Frame #86] Timestamps -> Cap: 4837.5503, Snd: 4837.5917, Recv: 4837.6880 | Total Latency (Capture->Render): 137.70ms | Network Latency (Send->Render): 96.34ms
[capture] frame #88
[client 281472943008192] sent frame #83 (Rolling Index: 88)
[capture] frame #89
[Telemetry][Frame #87] Timestamps -> Cap: 4837.6126, Snd: 4837.6549, Recv: 4837.7604 | Total Latency (Capture->Render): 147.72ms | Network Latency (Send->Render): 105.42ms
[client 281472943008192] sent frame #84 (Rolling Index: 89)
[Telemetry][Frame #88] Timestamps -> Cap: 4837.6884, Snd: 4837.7293, Recv: 4837.8193 | Total Latency (Capture->Render): 130.95ms | Network Latency (Send->Render): 90.01ms
[capture] frame #90
[client 281472943008192] sent frame #85 (Rolling Index: 90)
[capture] frame #91
[Telemetry][Frame #89] Timestamps -> Cap: 4837.7462, Snd: 4837.7899, Recv: 4837.8907 | Total Latency (Capture->Render): 144.45ms | Network Latency (Send->Render): 100.74ms
[client 281472943008192] sent frame #86 (Rolling Index: 91)
[capture] frame #92
[Telemetry][Frame #90] Timestamps -> Cap: 4837.8196, Snd: 4837.8618, Recv: 4837.9573 | Total Latency (Capture->Render): 137.70ms | Network Latency (Send->Render): 95.43ms
[client 281472943008192] sent frame #87 (Rolling Index: 92)
[capture] frame #93
[Telemetry][Frame #91] Timestamps -> Cap: 4837.8828, Snd: 4837.9273, Recv: 4838.0487 | Total Latency (Capture->Render): 165.99ms | Network Latency (Send->Render): 121.41ms
[client 281472943008192] sent frame #88 (Rolling Index: 93)
[capture] frame #94
[Telemetry][Frame #92] Timestamps -> Cap: 4837.9478, Snd: 4838.0016, Recv: 4838.1031 | Total Latency (Capture->Render): 155.32ms | Network Latency (Send->Render): 101.51ms
[client 281472943008192] sent frame #89 (Rolling Index: 94)
[Telemetry][Frame #93] Timestamps -> Cap: 4838.0203, Snd: 4838.0662, Recv: 4838.1566 | Total Latency (Capture->Render): 136.34ms | Network Latency (Send->Render): 90.40ms
[capture] frame #95
[client 281472943008192] sent frame #90 (Rolling Index: 95)
[capture] frame #96
[Telemetry][Frame #94] Timestamps -> Cap: 4838.0811, Snd: 4838.1271, Recv: 4838.2386 | Total Latency (Capture->Render): 157.47ms | Network Latency (Send->Render): 111.42ms
[client 281472943008192] sent frame #91 (Rolling Index: 96)
[capture] frame #97
[Telemetry][Frame #95] Timestamps -> Cap: 4838.1569, Snd: 4838.2018, Recv: 4838.3035 | Total Latency (Capture->Render): 146.60ms | Network Latency (Send->Render): 101.71ms
[client 281472943008192] sent frame #92 (Rolling Index: 97)
[capture] frame #98
[Telemetry][Frame #96] Timestamps -> Cap: 4838.2168, Snd: 4838.2629, Recv: 4838.3591 | Total Latency (Capture->Render): 142.27ms | Network Latency (Send->Render): 96.22ms
[client 281472943008192] sent frame #93 (Rolling Index: 98)
[capture] frame #99
[Telemetry][Frame #97] Timestamps -> Cap: 4838.2817, Snd: 4838.3268, Recv: 4838.4273 | Total Latency (Capture->Render): 145.56ms | Network Latency (Send->Render): 100.54ms
[client 281472943008192] sent frame #94 (Rolling Index: 99)
[Telemetry][Frame #98] Timestamps -> Cap: 4838.3509, Snd: 4838.3946, Recv: 4838.4832 | Total Latency (Capture->Render): 132.22ms | Network Latency (Send->Render): 88.55ms
[capture] frame #100
[client 281472943008192] sent frame #95 (Rolling Index: 0)
[capture] frame #101
[Telemetry][Frame #99] Timestamps -> Cap: 4838.4121, Snd: 4838.4560, Recv: 4838.5559 | Total Latency (Capture->Render): 143.81ms | Network Latency (Send->Render): 99.88ms
[client 281472943008192] sent frame #96 (Rolling Index: 1)
[Telemetry][Frame #0] Timestamps -> Cap: 4838.4834, Snd: 4838.5266, Recv: 4838.6143 | Total Latency (Capture->Render): 130.90ms | Network Latency (Send->Render): 87.73ms
[capture] frame #102
[client 281472943008192] sent frame #97 (Rolling Index: 2)
[capture] frame #103
[Telemetry][Frame #1] Timestamps -> Cap: 4838.5487, Snd: 4838.5914, Recv: 4838.6893 | Total Latency (Capture->Render): 140.62ms | Network Latency (Send->Render): 97.90ms
[client 281472943008192] sent frame #98 (Rolling Index: 3)
[Telemetry][Frame #2] Timestamps -> Cap: 4838.6146, Snd: 4838.6582, Recv: 4838.7536 | Total Latency (Capture->Render): 138.92ms | Network Latency (Send->Render): 95.35ms
[capture] frame #104
[client 281472943008192] sent frame #99 (Rolling Index: 4)
[capture] frame #105
[Telemetry][Frame #3] Timestamps -> Cap: 4838.6826, Snd: 4838.7246, Recv: 4838.8259 | Total Latency (Capture->Render): 143.32ms | Network Latency (Send->Render): 101.29ms
[client 281472943008192] sent frame #100 (Rolling Index: 5)
[Telemetry][Frame #4] Timestamps -> Cap: 4838.7538, Snd: 4838.7965, Recv: 4838.8857 | Total Latency (Capture->Render): 131.88ms | Network Latency (Send->Render): 89.19ms
[capture] frame #106
[client 281472943008192] sent frame #101 (Rolling Index: 6)
[capture] frame #107
[Telemetry][Frame #5] Timestamps -> Cap: 4838.8156, Snd: 4838.8583, Recv: 4838.9512 | Total Latency (Capture->Render): 135.59ms | Network Latency (Send->Render): 92.89ms
[client 281472943008192] sent frame #102 (Rolling Index: 7)
[Telemetry][Frame #6] Timestamps -> Cap: 4838.8860, Snd: 4838.9281, Recv: 4839.0210 | Total Latency (Capture->Render): 135.06ms | Network Latency (Send->Render): 92.90ms
[capture] frame #108
[client 281472943008192] sent frame #103 (Rolling Index: 8)
[capture] frame #109
[Telemetry][Frame #7] Timestamps -> Cap: 4838.9478, Snd: 4838.9906, Recv: 4839.0943 | Total Latency (Capture->Render): 146.47ms | Network Latency (Send->Render): 103.65ms
[client 281472943008192] sent frame #104 (Rolling Index: 9)
[Telemetry][Frame #8] Timestamps -> Cap: 4839.0213, Snd: 4839.0642, Recv: 4839.1541 | Total Latency (Capture->Render): 132.80ms | Network Latency (Send->Render): 89.89ms
[capture] frame #110
[client 281472943008192] sent frame #105 (Rolling Index: 10)
[capture] frame #111
[Telemetry][Frame #9] Timestamps -> Cap: 4839.0814, Snd: 4839.1253, Recv: 4839.2384 | Total Latency (Capture->Render): 156.97ms | Network Latency (Send->Render): 113.15ms
[client 281472943008192] sent frame #106 (Rolling Index: 11)
[capture] frame #112
[Telemetry][Frame #10] Timestamps -> Cap: 4839.1543, Snd: 4839.1966, Recv: 4839.2936 | Total Latency (Capture->Render): 139.29ms | Network Latency (Send->Render): 97.04ms
[client 281472943008192] sent frame #107 (Rolling Index: 12)
[capture] frame #113
[Telemetry][Frame #11] Timestamps -> Cap: 4839.2170, Snd: 4839.2613, Recv: 4839.3546 | Total Latency (Capture->Render): 137.68ms | Network Latency (Send->Render): 93.32ms
[client 281472943008192] sent frame #108 (Rolling Index: 13)
[capture] frame #114
[Telemetry][Frame #12] Timestamps -> Cap: 4839.2833, Snd: 4839.3272, Recv: 4839.4231 | Total Latency (Capture->Render): 139.77ms | Network Latency (Send->Render): 95.95ms
[client 281472943008192] sent frame #109 (Rolling Index: 14)
[capture] frame #115
[WebSocket Control] Active generation advanced to 2. Camera capture halted.
[WebSocket] Channel teardown complete for client 281472943012704
[client 281472943008192] sent frame #110 (Rolling Index: 15)
[DEBUG][client 281472943008192] Loop stopped: Evicted/Disconnected by state change.
[capture] frame #116
[DEBUG][client 281472899460672] ===== Granted Camera Ownership (Gen 3) =====
[capture] frame #117
[capture] frame #118
[capture] frame #119
[client 281472899460672] sent frame #1 (Rolling Index: 17)
[capture] frame #120
[capture] frame #121
[client 281472899460672] sent frame #2 (Rolling Index: 20)
[Telemetry][Frame #17] Timestamps -> Cap: 4841.8833, Snd: 4841.9817, Recv: 4842.0842 | Total Latency (Capture->Render): 200.96ms | Network Latency (Send->Render): 102.56ms
[capture] frame #122
[client 281472899460672] sent frame #3 (Rolling Index: 22)
[capture] frame #123
[Telemetry][Frame #20] Timestamps -> Cap: 4841.9822, Snd: 4842.0533, Recv: 4842.1755 | Total Latency (Capture->Render): 193.27ms | Network Latency (Send->Render): 122.20ms
[client 281472899460672] sent frame #4 (Rolling Index: 23)
[capture] frame #124
[Telemetry][Frame #22] Timestamps -> Cap: 4842.0845, Snd: 4842.1503, Recv: 4842.2326 | Total Latency (Capture->Render): 148.16ms | Network Latency (Send->Render): 82.35ms
[client 281472899460672] sent frame #5 (Rolling Index: 24)
[capture] frame #125
[Telemetry][Frame #23] Timestamps -> Cap: 4842.1506, Snd: 4842.1989, Recv: 4842.2904 | Total Latency (Capture->Render): 139.72ms | Network Latency (Send->Render): 91.51ms
[client 281472899460672] sent frame #6 (Rolling Index: 25)
[capture] frame #126
[Telemetry][Frame #24] Timestamps -> Cap: 4842.2198, Snd: 4842.2627, Recv: 4842.3611 | Total Latency (Capture->Render): 141.35ms | Network Latency (Send->Render): 98.41ms
[client 281472899460672] sent frame #7 (Rolling Index: 26)
[capture] frame #127
[Telemetry][Frame #25] Timestamps -> Cap: 4842.2851, Snd: 4842.3282, Recv: 4842.4236 | Total Latency (Capture->Render): 138.48ms | Network Latency (Send->Render): 95.42ms
[client 281472899460672] sent frame #8 (Rolling Index: 27)
[capture] frame #128
[Telemetry][Frame #26] Timestamps -> Cap: 4842.3536, Snd: 4842.3962, Recv: 4842.4885 | Total Latency (Capture->Render): 134.93ms | Network Latency (Send->Render): 92.35ms
[client 281472899460672] sent frame #9 (Rolling Index: 28)
[Telemetry][Frame #27] Timestamps -> Cap: 4842.4183, Snd: 4842.4602, Recv: 4842.5560 | Total Latency (Capture->Render): 137.69ms | Network Latency (Send->Render): 95.87ms
[capture] frame #129
[client 281472899460672] sent frame #10 (Rolling Index: 29)
[capture] frame #130
[Telemetry][Frame #28] Timestamps -> Cap: 4842.4859, Snd: 4842.5275, Recv: 4842.6325 | Total Latency (Capture->Render): 146.55ms | Network Latency (Send->Render): 105.01ms
[client 281472899460672] sent frame #11 (Rolling Index: 30)
[capture] frame #131
[Telemetry][Frame #29] Timestamps -> Cap: 4842.5563, Snd: 4842.5977, Recv: 4842.6920 | Total Latency (Capture->Render): 135.74ms | Network Latency (Send->Render): 94.37ms
[client 281472899460672] sent frame #12 (Rolling Index: 31)
[Telemetry][Frame #30] Timestamps -> Cap: 4842.6188, Snd: 4842.6616, Recv: 4842.7532 | Total Latency (Capture->Render): 134.47ms | Network Latency (Send->Render): 91.68ms
[capture] frame #132
[client 281472899460672] sent frame #13 (Rolling Index: 32)
[Telemetry][Frame #31] Timestamps -> Cap: 4842.6882, Snd: 4842.7297, Recv: 4842.8237 | Total Latency (Capture->Render): 135.45ms | Network Latency (Send->Render): 93.95ms
[capture] frame #133
[client 281472899460672] sent frame #14 (Rolling Index: 33)
[capture] frame #134
[Telemetry][Frame #32] Timestamps -> Cap: 4842.7535, Snd: 4842.7946, Recv: 4842.9015 | Total Latency (Capture->Render): 148.00ms | Network Latency (Send->Render): 106.96ms
[client 281472899460672] sent frame #15 (Rolling Index: 34)
[capture] frame #135
[Telemetry][Frame #33] Timestamps -> Cap: 4842.8241, Snd: 4842.8662, Recv: 4842.9584 | Total Latency (Capture->Render): 134.33ms | Network Latency (Send->Render): 92.21ms
[client 281472899460672] sent frame #16 (Rolling Index: 35)
[capture] frame #136
[Telemetry][Frame #34] Timestamps -> Cap: 4842.8870, Snd: 4842.9310, Recv: 4843.0265 | Total Latency (Capture->Render): 139.55ms | Network Latency (Send->Render): 95.60ms
[client 281472899460672] sent frame #17 (Rolling Index: 36)
[capture] frame #137
[Telemetry][Frame #35] Timestamps -> Cap: 4842.9514, Snd: 4842.9938, Recv: 4843.0916 | Total Latency (Capture->Render): 140.26ms | Network Latency (Send->Render): 97.80ms
[client 281472899460672] sent frame #18 (Rolling Index: 37)
[capture] frame #138
[Telemetry][Frame #36] Timestamps -> Cap: 4843.0192, Snd: 4843.0614, Recv: 4843.1592 | Total Latency (Capture->Render): 139.98ms | Network Latency (Send->Render): 97.85ms
[client 281472899460672] sent frame #19 (Rolling Index: 38)
[Telemetry][Frame #37] Timestamps -> Cap: 4843.0857, Snd: 4843.1290, Recv: 4843.2224 | Total Latency (Capture->Render): 136.74ms | Network Latency (Send->Render): 93.42ms
[capture] frame #139
[client 281472899460672] sent frame #20 (Rolling Index: 39)
[capture] frame #140
[Telemetry][Frame #38] Timestamps -> Cap: 4843.1525, Snd: 4843.1956, Recv: 4843.3012 | Total Latency (Capture->Render): 148.68ms | Network Latency (Send->Render): 105.65ms
[client 281472899460672] sent frame #21 (Rolling Index: 40)
[capture] frame #141
[Telemetry][Frame #39] Timestamps -> Cap: 4843.2227, Snd: 4843.2658, Recv: 4843.3608 | Total Latency (Capture->Render): 138.14ms | Network Latency (Send->Render): 95.03ms
[client 281472899460672] sent frame #22 (Rolling Index: 41)
[capture] frame #142
[Telemetry][Frame #40] Timestamps -> Cap: 4843.2872, Snd: 4843.3312, Recv: 4843.4234 | Total Latency (Capture->Render): 136.23ms | Network Latency (Send->Render): 92.17ms
[client 281472899460672] sent frame #23 (Rolling Index: 42)
[capture] frame #143
[Telemetry][Frame #41] Timestamps -> Cap: 4843.3519, Snd: 4843.3949, Recv: 4843.4927 | Total Latency (Capture->Render): 140.84ms | Network Latency (Send->Render): 97.81ms
[client 281472899460672] sent frame #24 (Rolling Index: 43)
[capture] frame #144
[Telemetry][Frame #42] Timestamps -> Cap: 4843.4183, Snd: 4843.4616, Recv: 4843.5605 | Total Latency (Capture->Render): 142.17ms | Network Latency (Send->Render): 98.89ms
[client 281472899460672] sent frame #25 (Rolling Index: 44)
[capture] frame #145
[Telemetry][Frame #43] Timestamps -> Cap: 4843.4875, Snd: 4843.5300, Recv: 4843.6323 | Total Latency (Capture->Render): 144.86ms | Network Latency (Send->Render): 102.27ms
[client 281472899460672] sent frame #26 (Rolling Index: 45)
[Telemetry][Frame #44] Timestamps -> Cap: 4843.5533, Snd: 4843.5955, Recv: 4843.6909 | Total Latency (Capture->Render): 137.54ms | Network Latency (Send->Render): 95.35ms
[capture] frame #146
[client 281472899460672] sent frame #27 (Rolling Index: 46)
[capture] frame #147
[Telemetry][Frame #45] Timestamps -> Cap: 4843.6180, Snd: 4843.6611, Recv: 4843.7653 | Total Latency (Capture->Render): 147.31ms | Network Latency (Send->Render): 104.15ms
[client 281472899460672] sent frame #28 (Rolling Index: 47)
[capture] frame #148
[Telemetry][Frame #46] Timestamps -> Cap: 4843.6911, Snd: 4843.7331, Recv: 4843.8285 | Total Latency (Capture->Render): 137.37ms | Network Latency (Send->Render): 95.40ms
[client 281472899460672] sent frame #29 (Rolling Index: 48)
[capture] frame #149
[Telemetry][Frame #47] Timestamps -> Cap: 4843.7552, Snd: 4843.7984, Recv: 4843.8885 | Total Latency (Capture->Render): 133.28ms | Network Latency (Send->Render): 90.09ms
[client 281472899460672] sent frame #30 (Rolling Index: 49)
[capture] frame #150
[Telemetry][Frame #48] Timestamps -> Cap: 4843.8191, Snd: 4843.8620, Recv: 4843.9585 | Total Latency (Capture->Render): 139.47ms | Network Latency (Send->Render): 96.56ms
[client 281472899460672] sent frame #31 (Rolling Index: 50)
[capture] frame #151
[Telemetry][Frame #49] Timestamps -> Cap: 4843.8867, Snd: 4843.9279, Recv: 4844.0464 | Total Latency (Capture->Render): 159.68ms | Network Latency (Send->Render): 118.47ms
[client 281472899460672] sent frame #32 (Rolling Index: 51)
[capture] frame #152
[Telemetry][Frame #50] Timestamps -> Cap: 4843.9537, Snd: 4844.0089, Recv: 4844.1044 | Total Latency (Capture->Render): 150.65ms | Network Latency (Send->Render): 95.44ms
[WebSocket] Channel teardown complete for client 281472943001040
[client 281472899460672] sent frame #33 (Rolling Index: 52)
[capture] frame #153
[client 281472899460672] sent frame #34 (Rolling Index: 53)
[capture] frame #154
[client 281472899460672] sent frame #35 (Rolling Index: 54)
[capture] frame #155
[client 281472899460672] sent frame #36 (Rolling Index: 55)
[capture] frame #156
[client 281472899460672] sent frame #37 (Rolling Index: 56)
[capture] frame #157
[client 281472899460672] sent frame #38 (Rolling Index: 57)
[capture] frame #158
[client 281472899460672] sent frame #39 (Rolling Index: 58)
[capture] frame #159
[client 281472899460672] sent frame #40 (Rolling Index: 59)
[capture] frame #160
[client 281472899460672] sent frame #41 (Rolling Index: 60)
[capture] frame #161
[client 281472899460672] sent frame #42 (Rolling Index: 61)
[capture] frame #162
[client 281472899460672] sent frame #43 (Rolling Index: 62)
[capture] frame #163
[client 281472899460672] sent frame #44 (Rolling Index: 63)
[capture] frame #164
[client 281472899460672] sent frame #45 (Rolling Index: 64)
[capture] frame #165
[client 281472899460672] sent frame #46 (Rolling Index: 65)
[capture] frame #166
[client 281472899460672] sent frame #47 (Rolling Index: 66)
[capture] frame #167
[client 281472899460672] sent frame #48 (Rolling Index: 67)
[capture] frame #168
[client 281472899460672] sent frame #49 (Rolling Index: 68)
[capture] frame #169
[client 281472899460672] sent frame #50 (Rolling Index: 69)
[capture] frame #170
[client 281472899460672] sent frame #51 (Rolling Index: 70)
[capture] frame #171
[client 281472899460672] sent frame #52 (Rolling Index: 71)
[capture] frame #172
[client 281472899460672] sent frame #53 (Rolling Index: 72)
[capture] frame #173
[client 281472899460672] sent frame #54 (Rolling Index: 73)
[capture] frame #174
[client 281472899460672] sent frame #55 (Rolling Index: 74)
[capture] frame #175
[client 281472899460672] sent frame #56 (Rolling Index: 75)
[capture] frame #176
[client 281472899460672] sent frame #57 (Rolling Index: 76)
[capture] frame #177
[client 281472899460672] sent frame #58 (Rolling Index: 77)
[capture] frame #178
[client 281472899460672] sent frame #59 (Rolling Index: 78)
[capture] frame #179
[client 281472899460672] sent frame #60 (Rolling Index: 79)
[capture] frame #180
^C
[server] shutting down
```

</details>


# Test endurance 42000 frames

<details>
<summary>Log</summary>

```bash
ecv: 8047.7586 | Total Latency (Capture->Render): 131.82ms | Network Latency (Send->Render): 88.02ms
[capture] frame #42518
[client 281473522242512] sent frame #46 (Rolling Index: 18)
[capture] frame #42519
[Telemetry][Frame #17] Timestamps -> Cap: 8047.6868, Snd: 8047.7323, Recv: 8047.8432 | Total Latency (Capture->Render): 156.38ms | Network Latency (Send->Render): 110.88ms
[client 281473522242512] sent frame #47 (Rolling Index: 19)
[capture] frame #42520
[Telemetry][Frame #18] Timestamps -> Cap: 8047.7591, Snd: 8047.8029, Recv: 8047.8937 | Total Latency (Capture->Render): 134.60ms | Network Latency (Send->Render): 90.79ms
[client 281473522242512] sent frame #48 (Rolling Index: 20)
[capture] frame #42521
[Telemetry][Frame #19] Timestamps -> Cap: 8047.8150, Snd: 8047.8627, Recv: 8047.9598 | Total Latency (Capture->Render): 144.77ms | Network Latency (Send->Render): 97.11ms
[client 281473522242512] sent frame #49 (Rolling Index: 21)
[capture] frame #42522
[Telemetry][Frame #20] Timestamps -> Cap: 8047.8844, Snd: 8047.9285, Recv: 8048.0189 | Total Latency (Capture->Render): 134.57ms | Network Latency (Send->Render): 90.44ms
[client 281473522242512] sent frame #50 (Rolling Index: 22)
[capture] frame #42523
[Telemetry][Frame #21] Timestamps -> Cap: 8047.9441, Snd: 8047.9901, Recv: 8048.0799 | Total Latency (Capture->Render): 135.72ms | Network Latency (Send->Render): 89.73ms
[client 281473522242512] sent frame #51 (Rolling Index: 23)
[capture] frame #42524
[Telemetry][Frame #22] Timestamps -> Cap: 8048.0087, Snd: 8048.0528, Recv: 8048.1472 | Total Latency (Capture->Render): 138.48ms | Network Latency (Send->Render): 94.38ms
[client 281473522242512] sent frame #52 (Rolling Index: 24)
[capture] frame #42525
[Telemetry][Frame #23] Timestamps -> Cap: 8048.0709, Snd: 8048.1148, Recv: 8048.2293 | Total Latency (Capture->Render): 158.33ms | Network Latency (Send->Render): 114.49ms
[capture] frame #42526
[client 281473522242512] sent frame #53 (Rolling Index: 25)
[Telemetry][Frame #24] Timestamps -> Cap: 8048.1418, Snd: 8048.1853, Recv: 8048.2984 | Total Latency (Capture->Render): 156.65ms | Network Latency (Send->Render): 113.07ms
[capture] frame #42527
[client 281473522242512] sent frame #54 (Rolling Index: 27)
[capture] frame #42528
[Telemetry][Frame #25] Timestamps -> Cap: 8048.2145, Snd: 8048.2751, Recv: 8048.4071 | Total Latency (Capture->Render): 192.52ms | Network Latency (Send->Render): 132.01ms
[client 281473522242512] sent frame #55 (Rolling Index: 28)
[capture] frame #42529
[Telemetry][Frame #27] Timestamps -> Cap: 8048.3359, Snd: 8048.3777, Recv: 8048.4652 | Total Latency (Capture->Render): 129.31ms | Network Latency (Send->Render): 87.57ms
[client 281473522242512] sent frame #56 (Rolling Index: 29)
[capture] frame #42530
[Telemetry][Frame #28] Timestamps -> Cap: 8048.3929, Snd: 8048.4361, Recv: 8048.5289 | Total Latency (Capture->Render): 135.95ms | Network Latency (Send->Render): 92.71ms
[client 281473522242512] sent frame #57 (Rolling Index: 30)
[capture] frame #42531
[Telemetry][Frame #29] Timestamps -> Cap: 8048.4570, Snd: 8048.4995, Recv: 8048.5910 | Total Latency (Capture->Render): 134.03ms | Network Latency (Send->Render): 91.53ms
[client 281473522242512] sent frame #58 (Rolling Index: 31)
[capture] frame #42532
[Telemetry][Frame #30] Timestamps -> Cap: 8048.5212, Snd: 8048.5630, Recv: 8048.6552 | Total Latency (Capture->Render): 134.05ms | Network Latency (Send->Render): 92.28ms
[client 281473522242512] sent frame #59 (Rolling Index: 32)
[capture] frame #42533
[Telemetry][Frame #31] Timestamps -> Cap: 8048.5839, Snd: 8048.6276, Recv: 8048.7222 | Total Latency (Capture->Render): 138.27ms | Network Latency (Send->Render): 94.62ms
[client 281473522242512] sent frame #60 (Rolling Index: 33)
[capture] frame #42534
[Telemetry][Frame #32] Timestamps -> Cap: 8048.6491, Snd: 8048.6918, Recv: 8048.7887 | Total Latency (Capture->Render): 139.62ms | Network Latency (Send->Render): 96.87ms
[client 281473522242512] sent frame #61 (Rolling Index: 34)
[capture] frame #42535
[Telemetry][Frame #33] Timestamps -> Cap: 8048.7144, Snd: 8048.7606, Recv: 8048.8472 | Total Latency (Capture->Render): 132.79ms | Network Latency (Send->Render): 86.64ms
[client 281473522242512] sent frame #62 (Rolling Index: 35)
[capture] frame #42536
[Telemetry][Frame #34] Timestamps -> Cap: 8048.7769, Snd: 8048.8205, Recv: 8048.9114 | Total Latency (Capture->Render): 134.45ms | Network Latency (Send->Render): 90.84ms
[client 281473522242512] sent frame #63 (Rolling Index: 36)
[capture] frame #42537
[Telemetry][Frame #35] Timestamps -> Cap: 8048.8400, Snd: 8048.8838, Recv: 8048.9734 | Total Latency (Capture->Render): 133.45ms | Network Latency (Send->Render): 89.61ms
[client 281473522242512] sent frame #64 (Rolling Index: 37)
[capture] frame #42538
[Telemetry][Frame #36] Timestamps -> Cap: 8048.9048, Snd: 8048.9476, Recv: 8049.0425 | Total Latency (Capture->Render): 137.66ms | Network Latency (Send->Render): 94.83ms
[client 281473522242512] sent frame #65 (Rolling Index: 38)
[capture] frame #42539
[Telemetry][Frame #37] Timestamps -> Cap: 8048.9699, Snd: 8049.0124, Recv: 8049.1057 | Total Latency (Capture->Render): 135.87ms | Network Latency (Send->Render): 93.35ms
[client 281473522242512] sent frame #66 (Rolling Index: 39)
[capture] frame #42540
[Telemetry][Frame #38] Timestamps -> Cap: 8049.0343, Snd: 8049.0783, Recv: 8049.1702 | Total Latency (Capture->Render): 135.81ms | Network Latency (Send->Render): 91.84ms
[client 281473522242512] sent frame #67 (Rolling Index: 40)
[capture] frame #42541
[Telemetry][Frame #39] Timestamps -> Cap: 8049.0969, Snd: 8049.1401, Recv: 8049.2327 | Total Latency (Capture->Render): 135.78ms | Network Latency (Send->Render): 92.60ms
[client 281473522242512] sent frame #68 (Rolling Index: 41)
[capture] frame #42542
[Telemetry][Frame #40] Timestamps -> Cap: 8049.1612, Snd: 8049.2039, Recv: 8049.2991 | Total Latency (Capture->Render): 137.94ms | Network Latency (Send->Render): 95.23ms
[client 281473522242512] sent frame #69 (Rolling Index: 42)
[capture] frame #42543
[Telemetry][Frame #41] Timestamps -> Cap: 8049.2247, Snd: 8049.2699, Recv: 8049.3626 | Total Latency (Capture->Render): 137.89ms | Network Latency (Send->Render): 92.72ms
[client 281473522242512] sent frame #70 (Rolling Index: 43)
[capture] frame #42544
[Telemetry][Frame #42] Timestamps -> Cap: 8049.2897, Snd: 8049.3338, Recv: 8049.4292 | Total Latency (Capture->Render): 139.52ms | Network Latency (Send->Render): 95.39ms
[client 281473522242512] sent frame #71 (Rolling Index: 44)
[capture] frame #42545
[Telemetry][Frame #43] Timestamps -> Cap: 8049.3521, Snd: 8049.3986, Recv: 8049.5119 | Total Latency (Capture->Render): 159.73ms | Network Latency (Send->Render): 113.22ms
[client 281473522242512] sent frame #72 (Rolling Index: 45)
[capture] frame #42546
[Telemetry][Frame #44] Timestamps -> Cap: 8049.4215, Snd: 8049.4683, Recv: 8049.5631 | Total Latency (Capture->Render): 141.67ms | Network Latency (Send->Render): 94.81ms
[client 281473522242512] sent frame #73 (Rolling Index: 46)
[capture] frame #42547
[Telemetry][Frame #45] Timestamps -> Cap: 8049.4802, Snd: 8049.5309, Recv: 8049.6368 | Total Latency (Capture->Render): 156.64ms | Network Latency (Send->Render): 105.93ms
[client 281473522242512] sent frame #74 (Rolling Index: 47)
[capture] frame #42548
[Telemetry][Frame #46] Timestamps -> Cap: 8049.5460, Snd: 8049.5933, Recv: 8049.6866 | Total Latency (Capture->Render): 140.60ms | Network Latency (Send->Render): 93.27ms
[client 281473522242512] sent frame #75 (Rolling Index: 48)
[capture] frame #42549
[Telemetry][Frame #47] Timestamps -> Cap: 8049.6078, Snd: 8049.6549, Recv: 8049.7603 | Total Latency (Capture->Render): 152.51ms | Network Latency (Send->Render): 105.43ms
[client 281473522242512] sent frame #76 (Rolling Index: 49)
[capture] frame #42550
[Telemetry][Frame #48] Timestamps -> Cap: 8049.6769, Snd: 8049.7233, Recv: 8049.8224 | Total Latency (Capture->Render): 145.51ms | Network Latency (Send->Render): 99.15ms
[client 281473522242512] sent frame #77 (Rolling Index: 50)
[capture] frame #42551
[Telemetry][Frame #49] Timestamps -> Cap: 8049.7387, Snd: 8049.7840, Recv: 8049.8782 | Total Latency (Capture->Render): 139.56ms | Network Latency (Send->Render): 94.26ms
[client 281473522242512] sent frame #78 (Rolling Index: 51)
[capture] frame #42552
[Telemetry][Frame #50] Timestamps -> Cap: 8049.8007, Snd: 8049.8457, Recv: 8049.9366 | Total Latency (Capture->Render): 135.83ms | Network Latency (Send->Render): 90.83ms
[client 281473522242512] sent frame #79 (Rolling Index: 52)
[capture] frame #42553
[Telemetry][Frame #51] Timestamps -> Cap: 8049.8642, Snd: 8049.9084, Recv: 8050.0012 | Total Latency (Capture->Render): 137.00ms | Network Latency (Send->Render): 92.82ms
[client 281473522242512] sent frame #80 (Rolling Index: 53)
[Telemetry][Frame #52] Timestamps -> Cap: 8049.9278, Snd: 8049.9723, Recv: 8050.0609 | Total Latency (Capture->Render): 133.06ms | Network Latency (Send->Render): 88.60ms
[capture] frame #42554
[client 281473522242512] sent frame #81 (Rolling Index: 54)
[capture] frame #42555
[Telemetry][Frame #53] Timestamps -> Cap: 8049.9905, Snd: 8050.0355, Recv: 8050.1346 | Total Latency (Capture->Render): 144.07ms | Network Latency (Send->Render): 99.11ms
[WebSocket Control] Active generation advanced to 4. Camera capture halted.
[WebSocket] Channel teardown complete for client 281473503701872
[client 281473522242512] sent frame #82 (Rolling Index: 55)
[DEBUG][client 281473522242512] Loop stopped: Evicted/Disconnected by state change.
[capture] frame #42556
^C
[server] shutting down
```

</details>



# EOL


```bash
```


<details>
<summary>Log</summary>

```bash
xxx
```

</details>
