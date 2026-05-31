

<details>
<summary>Log</summary>

```bash
(.venv) sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ python demo-libcamera-webserver-http-mjpg-qos.py
[4:50:43.003957216] [20238]  INFO Camera camera_manager.cpp:340 libcamera v0.7.1+rpt20260429
[4:50:43.004827258] [20242]  INFO IPAManager ipa_manager.cpp:148 libcamera is not installed. Adding '/home/sona/libcamera/build/src/ipa' to the IPA search path
[4:50:43.066064649] [20242]  INFO IPAProxy ipa_proxy.cpp:73 libcamera is not installed. Loading IPA configuration from '/home/sona/libcamera/src/ipa/rpi/vc4/data'
[4:50:43.066159851] [20242]  INFO IPAProxy ipa_proxy.cpp:184 Using tuning file /home/sona/libcamera/src/ipa/rpi/vc4/data/imx219.json
[4:50:43.074040781] [20242]  INFO Camera camera_manager.cpp:223 Adding camera '/base/soc/i2c0mux/i2c@1/imx219@10' for pipeline handler rpi/vc4
[4:50:43.074120372] [20242]  INFO RPI vc4.cpp:445 Registered camera /base/soc/i2c0mux/i2c@1/imx219@10 to Unicam device /dev/media2 and ISP device /dev/media1
[main] starting camera
[4:50:43.075439610] [20238]  INFO Camera camera.cpp:1216 configuring streams: (0) 1640x1232-RGB888/sRGB
[4:50:43.076083896] [20242]  INFO RPI vc4.cpp:620 Sensor: /base/soc/i2c0mux/i2c@1/imx219@10 - Selected sensor format: 1640x1232-SBGGR10_1X10/RAW - Selected unicam format: 1640x1232-pBAA/RAW
[warmup] frame 0 done
[warmup] frame 1 done
[warmup] frame 2 done
[warmup] frame 3 done
[warmup] frame 4 done
[server] starting bare HTTP on port 8000
[ws] WebSocket server listening on :8765
[client 281472637631280] connected /mjpg
[ws] client connected
[capture] frame #1 ts=1780224495.4565601
[capture] frame #2 ts=1780224495.495932
[capture] frame #3 ts=1780224495.5281603
[capture] frame #4 ts=1780224495.5899374
[client 281472637631280] sent frame #1 (sent #1)
[capture] frame #5 ts=1780224495.612993
[capture] frame #6 ts=1780224495.6439352
[capture] frame #7 ts=1780224495.687362
[client 281472637631280] sent frame #5 (sent #2)
client drawn frame 1 timestamp 1780224495.6888123 (capture_ts=1780224495.4565601, latency=0.232s)
[capture] frame #8 ts=1780224495.7445195
[capture] frame #9 ts=1780224495.8247354
[client 281472637631280] sent frame #8 (sent #3)
client drawn frame 2 timestamp 1780224495.8386807 (capture_ts=1780224495.495932, latency=0.343s)
[capture] frame #10 ts=1780224495.8606074
[capture] frame #11 ts=1780224495.9224823
[client 281472637631280] sent frame #10 (sent #4)
client drawn frame 3 timestamp 1780224495.923509 (capture_ts=1780224495.5281603, latency=0.395s)
[capture] frame #12 ts=1780224495.9864845
[client 281472637631280] sent frame #12 (sent #5)
[capture] frame #13 ts=1780224496.0379765
client drawn frame 4 timestamp 1780224496.0383406 (capture_ts=1780224495.5899374, latency=0.448s)
[client 281472637631280] sent frame #13 (sent #6)
client drawn frame 5 timestamp 1780224496.091629 (capture_ts=1780224495.612993, latency=0.479s)
[capture] frame #14 ts=1780224496.1082678
[client 281472637631280] sent frame #14 (sent #7)
[capture] frame #15 ts=1780224496.15937
client drawn frame 6 timestamp 1780224496.1635027 (capture_ts=1780224495.6439352, latency=0.520s)
[client 281472637631280] sent frame #15 (sent #8)
client drawn frame 7 timestamp 1780224496.2187634 (capture_ts=1780224495.687362, latency=0.531s)
[capture] frame #16 ts=1780224496.2189689
[client 281472637631280] sent frame #16 (sent #9)
client drawn frame 8 timestamp 1780224496.279339 (capture_ts=1780224495.7445195, latency=0.535s)
[capture] frame #17 ts=1780224496.279539
[client 281472637631280] sent frame #17 (sent #10)
client drawn frame 9 timestamp 1780224496.3413208 (capture_ts=1780224495.8247354, latency=0.517s)
[capture] frame #18 ts=1780224496.3416097
[client 281472637631280] sent frame #18 (sent #11)
client drawn frame 10 timestamp 1780224496.4007049 (capture_ts=1780224495.8606074, latency=0.540s)
[capture] frame #19 ts=1780224496.401132
[client 281472637631280] sent frame #19 (sent #12)
client drawn frame 11 timestamp 1780224496.4613361 (capture_ts=1780224495.9224823, latency=0.539s)
[capture] frame #20 ts=1780224496.461689
[client 281472637631280] sent frame #20 (sent #13)
client drawn frame 12 timestamp 1780224496.5203075 (capture_ts=1780224495.9864845, latency=0.534s)
[capture] frame #21 ts=1780224496.5205193
[client 281472637631280] sent frame #21 (sent #14)
client drawn frame 13 timestamp 1780224496.5801172 (capture_ts=1780224496.0379765, latency=0.542s)
[capture] frame #22 ts=1780224496.5805054
[client 281472637631280] sent frame #22 (sent #15)
client drawn frame 14 timestamp 1780224496.6411154 (capture_ts=1780224496.1082678, latency=0.533s)
[capture] frame #23 ts=1780224496.641566
[client 281472637631280] sent frame #23 (sent #16)
client drawn frame 15 timestamp 1780224496.699083 (capture_ts=1780224496.15937, latency=0.540s)
[capture] frame #24 ts=1780224496.6993434
[client 281472637631280] sent frame #24 (sent #17)
[capture] frame #25 ts=1780224496.7597048
client drawn frame 16 timestamp 1780224496.759929 (capture_ts=1780224496.2189689, latency=0.541s)
[client 281472637631280] sent frame #25 (sent #18)
client drawn frame 17 timestamp 1780224496.8226457 (capture_ts=1780224496.279539, latency=0.543s)
[capture] frame #26 ts=1780224496.822941
[client 281472637631280] sent frame #26 (sent #19)
[capture] frame #27 ts=1780224496.879808
client drawn frame 18 timestamp 1780224496.8801696 (capture_ts=1780224496.3416097, latency=0.539s)
[client 281472637631280] sent frame #27 (sent #20)
[capture] frame #28 ts=1780224496.9400587
client drawn frame 19 timestamp 1780224496.9403722 (capture_ts=1780224496.401132, latency=0.539s)
[client 281472637631280] sent frame #28 (sent #21)
client drawn frame 20 timestamp 1780224496.9998643 (capture_ts=1780224496.461689, latency=0.538s)
[capture] frame #29 ts=1780224497.0001132
[client 281472637631280] sent frame #29 (sent #22)
client drawn frame 21 timestamp 1780224497.0511768 (capture_ts=1780224496.5205193, latency=0.531s)
[capture] frame #30 ts=1780224497.0633261
[client 281472637631280] sent frame #30 (sent #23)
[capture] frame #31 ts=1780224497.1196227
client drawn frame 22 timestamp 1780224497.1200092 (capture_ts=1780224496.5805054, latency=0.540s)
[client 281472637631280] sent frame #31 (sent #24)
client drawn frame 23 timestamp 1780224497.1724367 (capture_ts=1780224496.641566, latency=0.531s)
[capture] frame #32 ts=1780224497.185395
[client 281472637631280] sent frame #32 (sent #25)
[capture] frame #33 ts=1780224497.2391925
client drawn frame 24 timestamp 1780224497.2395499 (capture_ts=1780224496.6993434, latency=0.540s)
[client 281472637631280] sent frame #33 (sent #26)
client drawn frame 25 timestamp 1780224497.291025 (capture_ts=1780224496.7597048, latency=0.531s)
[capture] frame #34 ts=1780224497.3031397
[client 281472637631280] sent frame #34 (sent #27)
client drawn frame 26 timestamp 1780224497.360238 (capture_ts=1780224496.822941, latency=0.537s)
[capture] frame #35 ts=1780224497.3605075
[client 281472637631280] sent frame #35 (sent #28)
client drawn frame 27 timestamp 1780224497.4210434 (capture_ts=1780224496.879808, latency=0.541s)
[capture] frame #36 ts=1780224497.4212437
[client 281472637631280] sent frame #36 (sent #29)
client drawn frame 28 timestamp 1780224497.4728272 (capture_ts=1780224496.9400587, latency=0.533s)
[capture] frame #37 ts=1780224497.4839299
[client 281472637631280] sent frame #37 (sent #30)
client drawn frame 29 timestamp 1780224497.5424807 (capture_ts=1780224497.0001132, latency=0.542s)
[capture] frame #38 ts=1780224497.542724
[client 281472637631280] sent frame #38 (sent #31)
client drawn frame 30 timestamp 1780224497.6012669 (capture_ts=1780224497.0633261, latency=0.538s)
[capture] frame #39 ts=1780224497.6016548
[client 281472637631280] sent frame #39 (sent #32)
[capture] frame #40 ts=1780224497.6626432
client drawn frame 31 timestamp 1780224497.662925 (capture_ts=1780224497.1196227, latency=0.543s)
[client 281472637631280] sent frame #40 (sent #33)
[capture] frame #41 ts=1780224497.721628
client drawn frame 32 timestamp 1780224497.7218626 (capture_ts=1780224497.185395, latency=0.536s)
[client 281472637631280] sent frame #41 (sent #34)
client drawn frame 33 timestamp 1780224497.7847703 (capture_ts=1780224497.2391925, latency=0.546s)
[capture] frame #42 ts=1780224497.7849777
[client 281472637631280] sent frame #42 (sent #35)
[capture] frame #43 ts=1780224497.8401492
client drawn frame 34 timestamp 1780224497.840572 (capture_ts=1780224497.3031397, latency=0.537s)
[client 281472637631280] sent frame #43 (sent #36)
client drawn frame 35 timestamp 1780224497.902733 (capture_ts=1780224497.3605075, latency=0.542s)
[capture] frame #44 ts=1780224497.9029915
[client 281472637631280] sent frame #44 (sent #37)
client drawn frame 36 timestamp 1780224497.9618275 (capture_ts=1780224497.4212437, latency=0.541s)
[capture] frame #45 ts=1780224497.962202
[client 281472637631280] sent frame #45 (sent #38)
client drawn frame 37 timestamp 1780224498.0227418 (capture_ts=1780224497.4839299, latency=0.539s)
[capture] frame #46 ts=1780224498.0229464
[client 281472637631280] sent frame #46 (sent #39)
[capture] frame #47 ts=1780224498.082607
client drawn frame 38 timestamp 1780224498.0829525 (capture_ts=1780224497.542724, latency=0.540s)
[client 281472637631280] sent frame #47 (sent #40)
client drawn frame 39 timestamp 1780224498.1428988 (capture_ts=1780224497.6016548, latency=0.541s)
[capture] frame #48 ts=1780224498.1431437
[client 281472637631280] sent frame #48 (sent #41)
client drawn frame 40 timestamp 1780224498.1999624 (capture_ts=1780224497.6626432, latency=0.537s)
[capture] frame #49 ts=1780224498.200205
[client 281472637631280] sent frame #49 (sent #42)
client drawn frame 41 timestamp 1780224498.252797 (capture_ts=1780224497.721628, latency=0.531s)
[capture] frame #50 ts=1780224498.262983
[client 281472637631280] sent frame #50 (sent #43)
client drawn frame 42 timestamp 1780224498.323565 (capture_ts=1780224497.7849777, latency=0.539s)
[capture] frame #51 ts=1780224498.3237576
[client 281472637631280] sent frame #51 (sent #44)
[capture] frame #52 ts=1780224498.3820202
client drawn frame 43 timestamp 1780224498.3824627 (capture_ts=1780224497.8401492, latency=0.542s)
[client 281472637631280] sent frame #52 (sent #45)
client drawn frame 44 timestamp 1780224498.4420164 (capture_ts=1780224497.9029915, latency=0.539s)
[capture] frame #53 ts=1780224498.4422398
[client 281472637631280] sent frame #53 (sent #46)
client drawn frame 45 timestamp 1780224498.5014558 (capture_ts=1780224497.962202, latency=0.539s)
[capture] frame #54 ts=1780224498.5016656
[client 281472637631280] sent frame #54 (sent #47)
client drawn frame 46 timestamp 1780224498.5643206 (capture_ts=1780224498.0229464, latency=0.541s)
[capture] frame #55 ts=1780224498.564517
[client 281472637631280] sent frame #55 (sent #48)
client drawn frame 47 timestamp 1780224498.624081 (capture_ts=1780224498.082607, latency=0.541s)
[capture] frame #56 ts=1780224498.6244254
[client 281472637631280] sent frame #56 (sent #49)
client drawn frame 48 timestamp 1780224498.6836302 (capture_ts=1780224498.1431437, latency=0.540s)
[capture] frame #57 ts=1780224498.683852
[client 281472637631280] sent frame #57 (sent #50)
[capture] frame #58 ts=1780224498.7434926
client drawn frame 49 timestamp 1780224498.7437472 (capture_ts=1780224498.200205, latency=0.544s)
[client 281472637631280] sent frame #58 (sent #51)
client drawn frame 50 timestamp 1780224498.804085 (capture_ts=1780224498.262983, latency=0.541s)
[capture] frame #59 ts=1780224498.804306
[client 281472637631280] sent frame #59 (sent #52)
client drawn frame 51 timestamp 1780224498.8628397 (capture_ts=1780224498.3237576, latency=0.539s)
[capture] frame #60 ts=1780224498.8631115
[client 281472637631280] sent frame #60 (sent #53)
[capture] frame #61 ts=1780224498.9236963
client drawn frame 52 timestamp 1780224498.9239974 (capture_ts=1780224498.3820202, latency=0.542s)
[client 281472637631280] sent frame #61 (sent #54)
[capture] frame #62 ts=1780224498.981008
client drawn frame 53 timestamp 1780224498.9813623 (capture_ts=1780224498.4422398, latency=0.539s)
[client 281472637631280] sent frame #62 (sent #55)
client drawn frame 54 timestamp 1780224499.045263 (capture_ts=1780224498.5016656, latency=0.544s)
[capture] frame #63 ts=1780224499.0455098
[client 281472637631280] sent frame #63 (sent #56)
client drawn frame 55 timestamp 1780224499.1044455 (capture_ts=1780224498.564517, latency=0.540s)
[capture] frame #64 ts=1780224499.1046476
[client 281472637631280] sent frame #64 (sent #57)
client drawn frame 56 timestamp 1780224499.164858 (capture_ts=1780224498.6244254, latency=0.540s)
[capture] frame #65 ts=1780224499.1651087
[client 281472637631280] sent frame #65 (sent #58)
client drawn frame 57 timestamp 1780224499.223016 (capture_ts=1780224498.683852, latency=0.539s)
[capture] frame #66 ts=1780224499.2233338
[client 281472637631280] sent frame #66 (sent #59)
client drawn frame 58 timestamp 1780224499.2742221 (capture_ts=1780224498.7434926, latency=0.531s)
[capture] frame #67 ts=1780224499.2866821
[client 281472637631280] sent frame #67 (sent #60)
client drawn frame 59 timestamp 1780224499.342641 (capture_ts=1780224498.804306, latency=0.538s)
[capture] frame #68 ts=1780224499.3428419
[client 281472637631280] sent frame #68 (sent #61)
client drawn frame 60 timestamp 1780224499.4070044 (capture_ts=1780224498.8631115, latency=0.544s)
[capture] frame #69 ts=1780224499.4071949
[client 281472637631280] sent frame #69 (sent #62)
[capture] frame #70 ts=1780224499.4621909
client drawn frame 61 timestamp 1780224499.4626195 (capture_ts=1780224498.9236963, latency=0.539s)
[client 281472637631280] sent frame #70 (sent #63)
client drawn frame 62 timestamp 1780224499.513188 (capture_ts=1780224498.981008, latency=0.532s)
[capture] frame #71 ts=1780224499.5316315
[client 281472637631280] sent frame #71 (sent #64)
[capture] frame #72 ts=1780224499.5824645
client drawn frame 63 timestamp 1780224499.5876167 (capture_ts=1780224499.0455098, latency=0.542s)
[client 281472637631280] sent frame #72 (sent #65)
client drawn frame 64 timestamp 1780224499.635112 (capture_ts=1780224499.1046476, latency=0.530s)
[capture] frame #73 ts=1780224499.6470735
[client 281472637631280] sent frame #73 (sent #66)
[capture] frame #74 ts=1780224499.7050502
client drawn frame 65 timestamp 1780224499.7056246 (capture_ts=1780224499.1651087, latency=0.541s)
[client 281472637631280] sent frame #74 (sent #67)
client drawn frame 66 timestamp 1780224499.7634847 (capture_ts=1780224499.2233338, latency=0.540s)
[capture] frame #75 ts=1780224499.7637022
[client 281472637631280] sent frame #75 (sent #68)
client drawn frame 67 timestamp 1780224499.8261588 (capture_ts=1780224499.2866821, latency=0.539s)
[capture] frame #76 ts=1780224499.8263881
[client 281472637631280] sent frame #76 (sent #69)
[capture] frame #77 ts=1780224499.882236
client drawn frame 68 timestamp 1780224499.907742 (capture_ts=1780224499.3428419, latency=0.565s)
[client 281472637631280] sent frame #77 (sent #70)
client drawn frame 69 timestamp 1780224499.9310663 (capture_ts=1780224499.4071949, latency=0.524s)
[capture] frame #78 ts=1780224499.953093
[client 281472637631280] sent frame #78 (sent #71)
[capture] frame #79 ts=1780224500.005789
client drawn frame 70 timestamp 1780224500.006173 (capture_ts=1780224499.4621909, latency=0.544s)
[client 281472637631280] sent frame #79 (sent #72)
[capture] frame #80 ts=1780224500.065555
client drawn frame 71 timestamp 1780224500.0658119 (capture_ts=1780224499.5316315, latency=0.534s)
[client 281472637631280] sent frame #80 (sent #73)
[capture] frame #81 ts=1780224500.123601
client drawn frame 72 timestamp 1780224500.1239944 (capture_ts=1780224499.5824645, latency=0.542s)
[capture] frame #82 ts=1780224500.1945713
[client 281472637631280] sent frame #81 (sent #74)
client drawn frame 73 timestamp 1780224500.2062764 (capture_ts=1780224499.6470735, latency=0.559s)
[capture] frame #83 ts=1780224500.2534971
client drawn frame 74 timestamp 1780224500.3045652 (capture_ts=1780224499.7050502, latency=0.600s)
[client 281472637631280] sent frame #83 (sent #75)
[capture] frame #84 ts=1780224500.3052454
[client 281472637631280] sent frame #84 (sent #76)
[capture] frame #85 ts=1780224500.3687577
client drawn frame 75 timestamp 1780224500.3691564 (capture_ts=1780224499.7637022, latency=0.605s)
[client 281472637631280] sent frame #85 (sent #77)
client drawn frame 76 timestamp 1780224500.4207077 (capture_ts=1780224499.8263881, latency=0.594s)
[capture] frame #86 ts=1780224500.4415736
[client 281472637631280] sent frame #86 (sent #78)
client drawn frame 77 timestamp 1780224500.5036795 (capture_ts=1780224499.882236, latency=0.621s)
[capture] frame #87 ts=1780224500.5038724
[client 281472637631280] sent frame #87 (sent #79)
client drawn frame 78 timestamp 1780224500.5560348 (capture_ts=1780224499.953093, latency=0.603s)
[capture] frame #88 ts=1780224500.5682504
[client 281472637631280] sent frame #88 (sent #80)
client drawn frame 79 timestamp 1780224500.6213286 (capture_ts=1780224500.005789, latency=0.616s)
[capture] frame #89 ts=1780224500.638315
[client 281472637631280] sent frame #89 (sent #81)
client drawn frame 80 timestamp 1780224500.6910014 (capture_ts=1780224500.065555, latency=0.625s)
[capture] frame #90 ts=1780224500.7020667
[client 281472637631280] sent frame #90 (sent #82)
client drawn frame 81 timestamp 1780224500.7557127 (capture_ts=1780224500.123601, latency=0.632s)
[capture] frame #91 ts=1780224500.7749412
[client 281472637631280] sent frame #91 (sent #83)
client drawn frame 82 timestamp 1780224500.8365211 (capture_ts=1780224500.1945713, latency=0.642s)
[capture] frame #92 ts=1780224500.836775
[client 281472637631280] sent frame #92 (sent #84)
client drawn frame 83 timestamp 1780224500.8904192 (capture_ts=1780224500.2534971, latency=0.637s)
[capture] frame #93 ts=1780224500.90465
[client 281472637631280] sent frame #93 (sent #85)
client drawn frame 84 timestamp 1780224500.9568107 (capture_ts=1780224500.3052454, latency=0.652s)
[capture] frame #94 ts=1780224500.9697344
[client 281472637631280] sent frame #94 (sent #86)
client drawn frame 85 timestamp 1780224501.0207958 (capture_ts=1780224500.3687577, latency=0.652s)
[capture] frame #95 ts=1780224501.0389433
[client 281472637631280] sent frame #95 (sent #87)
client drawn frame 86 timestamp 1780224501.0928407 (capture_ts=1780224500.4415736, latency=0.651s)
[capture] frame #96 ts=1780224501.1040533
[client 281472637631280] sent frame #96 (sent #88)
client drawn frame 87 timestamp 1780224501.155525 (capture_ts=1780224500.5038724, latency=0.652s)
[capture] frame #97 ts=1780224501.175093
[client 281472637631280] sent frame #97 (sent #89)
client drawn frame 88 timestamp 1780224501.225396 (capture_ts=1780224500.5682504, latency=0.657s)
[capture] frame #98 ts=1780224501.2376182
[client 281472637631280] sent frame #98 (sent #90)
client drawn frame 89 timestamp 1780224501.2900488 (capture_ts=1780224500.638315, latency=0.652s)
[capture] frame #99 ts=1780224501.301916
[client 281472637631280] sent frame #99 (sent #91)
client drawn frame 90 timestamp 1780224501.3536642 (capture_ts=1780224500.7020667, latency=0.652s)
[capture] frame #100 ts=1780224501.3760614
[client 281472637631280] sent frame #100 (sent #92)
client drawn frame 91 timestamp 1780224501.4384425 (capture_ts=1780224500.7749412, latency=0.664s)
[capture] frame #101 ts=1780224501.4386516
[client 281472637631280] sent frame #101 (sent #93)
client drawn frame 92 timestamp 1780224501.4914794 (capture_ts=1780224500.836775, latency=0.655s)
[capture] frame #102 ts=1780224501.5021644
[client 281472637631280] sent frame #102 (sent #94)
client drawn frame 93 timestamp 1780224501.5533524 (capture_ts=1780224500.90465, latency=0.649s)
[capture] frame #103 ts=1780224501.5737746
[client 281472637631280] sent frame #103 (sent #95)
client drawn frame 94 timestamp 1780224501.6260386 (capture_ts=1780224500.9697344, latency=0.656s)
[capture] frame #104 ts=1780224501.638482
[client 281472637631280] sent frame #104 (sent #96)
client drawn frame 95 timestamp 1780224501.689526 (capture_ts=1780224501.0389433, latency=0.651s)
[capture] frame #105 ts=1780224501.703541
[client 281472637631280] sent frame #105 (sent #97)
client drawn frame 96 timestamp 1780224501.7574635 (capture_ts=1780224501.1040533, latency=0.653s)
[capture] frame #106 ts=1780224501.7719347
[client 281472637631280] sent frame #106 (sent #98)
client drawn frame 97 timestamp 1780224501.8242548 (capture_ts=1780224501.175093, latency=0.649s)
[capture] frame #107 ts=1780224501.836492
[client 281472637631280] sent frame #107 (sent #99)
client drawn frame 98 timestamp 1780224501.8904324 (capture_ts=1780224501.2376182, latency=0.653s)
[capture] frame #108 ts=1780224501.9094055
[client 281472637631280] sent frame #108 (sent #100)
[capture] frame #109 ts=1780224501.9687061
client drawn frame 99 timestamp 1780224501.9689746 (capture_ts=1780224501.301916, latency=0.667s)
[client 281472637631280] sent frame #109 (sent #101)
client drawn frame 100 timestamp 1780224502.0235295 (capture_ts=1780224501.3760614, latency=0.647s)
[capture] frame #110 ts=1780224502.0447822
[client 281472637631280] sent frame #110 (sent #102)
client drawn frame 101 timestamp 1780224502.1038585 (capture_ts=1780224501.4386516, latency=0.665s)
[capture] frame #111 ts=1780224502.104075
[client 281472637631280] sent frame #111 (sent #103)
client drawn frame 102 timestamp 1780224502.1568663 (capture_ts=1780224501.5021644, latency=0.655s)
[capture] frame #112 ts=1780224502.1712263
[client 281472637631280] sent frame #112 (sent #104)
client drawn frame 103 timestamp 1780224502.2236164 (capture_ts=1780224501.5737746, latency=0.650s)
[capture] frame #113 ts=1780224502.2420876
[client 281472637631280] sent frame #113 (sent #105)
client drawn frame 104 timestamp 1780224502.2929022 (capture_ts=1780224501.638482, latency=0.654s)
[capture] frame #114 ts=1780224502.305628
[client 281472637631280] sent frame #114 (sent #106)
client drawn frame 105 timestamp 1780224502.3568323 (capture_ts=1780224501.703541, latency=0.653s)
[capture] frame #115 ts=1780224502.370454
[client 281472637631280] sent frame #115 (sent #107)
client drawn frame 106 timestamp 1780224502.4212546 (capture_ts=1780224501.7719347, latency=0.649s)
[capture] frame #116 ts=1780224502.4443982
[client 281472637631280] sent frame #116 (sent #108)
client drawn frame 107 timestamp 1780224502.506579 (capture_ts=1780224501.836492, latency=0.670s)
[capture] frame #117 ts=1780224502.5067935
[client 281472637631280] sent frame #117 (sent #109)
client drawn frame 108 timestamp 1780224502.5600376 (capture_ts=1780224501.9094055, latency=0.651s)
[capture] frame #118 ts=1780224502.5715582
[client 281472637631280] sent frame #118 (sent #110)
client drawn frame 109 timestamp 1780224502.6215875 (capture_ts=1780224501.9687061, latency=0.653s)
[capture] frame #119 ts=1780224502.6388273
[client 281472637631280] sent frame #119 (sent #111)
client drawn frame 110 timestamp 1780224502.6909823 (capture_ts=1780224502.0447822, latency=0.646s)
[capture] frame #120 ts=1780224502.7104397
[client 281472637631280] sent frame #120 (sent #112)
client drawn frame 111 timestamp 1780224502.7611463 (capture_ts=1780224502.104075, latency=0.657s)
[capture] frame #121 ts=1780224502.7718973
[client 281472637631280] sent frame #121 (sent #113)
client drawn frame 112 timestamp 1780224502.8227375 (capture_ts=1780224502.1712263, latency=0.652s)
[capture] frame #122 ts=1780224502.8397822
[client 281472637631280] sent frame #122 (sent #114)
client drawn frame 113 timestamp 1780224502.901589 (capture_ts=1780224502.2420876, latency=0.660s)
[capture] frame #123 ts=1780224502.9020069
[client 281472637631280] sent frame #123 (sent #115)
client drawn frame 114 timestamp 1780224502.962873 (capture_ts=1780224502.305628, latency=0.657s)
[capture] frame #124 ts=1780224502.9633825
[client 281472637631280] sent frame #124 (sent #116)
client drawn frame 115 timestamp 1780224503.0149872 (capture_ts=1780224502.370454, latency=0.645s)
[capture] frame #125 ts=1780224503.0295575
[client 281472637631280] sent frame #125 (sent #117)
client drawn frame 116 timestamp 1780224503.0822656 (capture_ts=1780224502.4443982, latency=0.638s)
[capture] frame #126 ts=1780224503.0956101
[client 281472637631280] sent frame #126 (sent #118)
client drawn frame 117 timestamp 1780224503.1475477 (capture_ts=1780224502.5067935, latency=0.641s)
[capture] frame #127 ts=1780224503.1656296
[client 281472637631280] sent frame #127 (sent #119)
[capture] frame #128 ts=1780224503.2268622
client drawn frame 118 timestamp 1780224503.2271159 (capture_ts=1780224502.5715582, latency=0.656s)
[client 281472637631280] sent frame #128 (sent #120)
client drawn frame 119 timestamp 1780224503.2792358 (capture_ts=1780224502.6388273, latency=0.640s)
[capture] frame #129 ts=1780224503.2974548
[client 281472637631280] sent frame #129 (sent #121)
client drawn frame 120 timestamp 1780224503.3476636 (capture_ts=1780224502.7104397, latency=0.637s)
[capture] frame #130 ts=1780224503.364317
[client 281472637631280] sent frame #130 (sent #122)
client drawn frame 121 timestamp 1780224503.4144845 (capture_ts=1780224502.7718973, latency=0.643s)
[capture] frame #131 ts=1780224503.4317427
[client 281472637631280] sent frame #131 (sent #123)
client drawn frame 122 timestamp 1780224503.4830072 (capture_ts=1780224502.8397822, latency=0.643s)
[capture] frame #132 ts=1780224503.494758
[client 281472637631280] sent frame #132 (sent #124)
client drawn frame 123 timestamp 1780224503.5453098 (capture_ts=1780224502.9020069, latency=0.643s)
[capture] frame #133 ts=1780224503.5611992
[client 281472637631280] sent frame #133 (sent #125)
client drawn frame 124 timestamp 1780224503.614237 (capture_ts=1780224502.9633825, latency=0.651s)
[capture] frame #134 ts=1780224503.6307228
[client 281472637631280] sent frame #134 (sent #126)
client drawn frame 125 timestamp 1780224503.6938217 (capture_ts=1780224503.0295575, latency=0.664s)
[capture] frame #135 ts=1780224503.6941717
[client 281472637631280] sent frame #135 (sent #127)
client drawn frame 126 timestamp 1780224503.7469366 (capture_ts=1780224503.0956101, latency=0.651s)
[capture] frame #136 ts=1780224503.7665746
[client 281472637631280] sent frame #136 (sent #128)
client drawn frame 127 timestamp 1780224503.8165977 (capture_ts=1780224503.1656296, latency=0.651s)
[capture] frame #137 ts=1780224503.8311372
[client 281472637631280] sent frame #137 (sent #129)
client drawn frame 128 timestamp 1780224503.8808758 (capture_ts=1780224503.2268622, latency=0.654s)
[capture] frame #138 ts=1780224503.8965275
[client 281472637631280] sent frame #138 (sent #130)
client drawn frame 129 timestamp 1780224503.9479651 (capture_ts=1780224503.2974548, latency=0.651s)
[capture] frame #139 ts=1780224503.965521
[client 281472637631280] sent frame #139 (sent #131)
client drawn frame 130 timestamp 1780224504.0183532 (capture_ts=1780224503.364317, latency=0.654s)
[capture] frame #140 ts=1780224504.0290875
[client 281472637631280] sent frame #140 (sent #132)
client drawn frame 131 timestamp 1780224504.0931087 (capture_ts=1780224503.4317427, latency=0.661s)
[capture] frame #141 ts=1780224504.0935419
[client 281472637631280] sent frame #141 (sent #133)
client drawn frame 132 timestamp 1780224504.1451375 (capture_ts=1780224503.494758, latency=0.650s)
[capture] frame #142 ts=1780224504.1637263
[client 281472637631280] sent frame #142 (sent #134)
client drawn frame 133 timestamp 1780224504.2265923 (capture_ts=1780224503.5611992, latency=0.665s)
[capture] frame #143 ts=1780224504.2268777
[client 281472637631280] sent frame #143 (sent #135)
client drawn frame 134 timestamp 1780224504.2792492 (capture_ts=1780224503.6307228, latency=0.649s)
[capture] frame #144 ts=1780224504.2951002
[client 281472637631280] sent frame #144 (sent #136)
client drawn frame 135 timestamp 1780224504.3463898 (capture_ts=1780224503.6941717, latency=0.652s)
[capture] frame #145 ts=1780224504.365226
[client 281472637631280] sent frame #145 (sent #137)
client drawn frame 136 timestamp 1780224504.4280262 (capture_ts=1780224503.7665746, latency=0.661s)
[capture] frame #146 ts=1780224504.4282272
[client 281472637631280] sent frame #146 (sent #138)
client drawn frame 137 timestamp 1780224504.4811952 (capture_ts=1780224503.8311372, latency=0.650s)
[capture] frame #147 ts=1780224504.499609
[client 281472637631280] sent frame #147 (sent #139)
client drawn frame 138 timestamp 1780224504.5644732 (capture_ts=1780224503.8965275, latency=0.668s)
[capture] frame #148 ts=1780224504.5648296
[client 281472637631280] sent frame #148 (sent #140)
client drawn frame 139 timestamp 1780224504.62804 (capture_ts=1780224503.965521, latency=0.663s)
[capture] frame #149 ts=1780224504.6283355
[client 281472637631280] sent frame #149 (sent #141)
client drawn frame 140 timestamp 1780224504.6818545 (capture_ts=1780224504.0290875, latency=0.653s)
[capture] frame #150 ts=1780224504.7009497
[client 281472637631280] sent frame #150 (sent #142)
client drawn frame 141 timestamp 1780224504.7606575 (capture_ts=1780224504.0935419, latency=0.667s)
[capture] frame #151 ts=1780224504.7608483
[client 281472637631280] sent frame #151 (sent #143)
client drawn frame 142 timestamp 1780224504.812269 (capture_ts=1780224504.1637263, latency=0.649s)
[capture] frame #152 ts=1780224504.8298278
[client 281472637631280] sent frame #152 (sent #144)
client drawn frame 143 timestamp 1780224504.8839614 (capture_ts=1780224504.2268777, latency=0.657s)
[capture] frame #153 ts=1780224504.8989956
[client 281472637631280] sent frame #153 (sent #145)
client drawn frame 144 timestamp 1780224504.9505863 (capture_ts=1780224504.2951002, latency=0.655s)
[capture] frame #154 ts=1780224504.9648921
[client 281472637631280] sent frame #154 (sent #146)
client drawn frame 145 timestamp 1780224505.0162618 (capture_ts=1780224504.365226, latency=0.651s)
[capture] frame #155 ts=1780224505.0268729
[client 281472637631280] sent frame #155 (sent #147)
client drawn frame 146 timestamp 1780224505.0797405 (capture_ts=1780224504.4282272, latency=0.652s)
[capture] frame #156 ts=1780224505.100218
[client 281472637631280] sent frame #156 (sent #148)
client drawn frame 147 timestamp 1780224505.1608737 (capture_ts=1780224504.499609, latency=0.661s)
[capture] frame #157 ts=1780224505.1610932
[client 281472637631280] sent frame #157 (sent #149)
[capture] frame #158 ts=1780224505.2225637
client drawn frame 148 timestamp 1780224505.2227817 (capture_ts=1780224504.5648296, latency=0.658s)
[client 281472637631280] sent frame #158 (sent #150)
client drawn frame 149 timestamp 1780224505.275277 (capture_ts=1780224504.6283355, latency=0.647s)
[capture] frame #159 ts=1780224505.2875414
[client 281472637631280] sent frame #159 (sent #151)
[capture] frame #160 ts=1780224505.343572
client drawn frame 150 timestamp 1780224505.343966 (capture_ts=1780224504.7009497, latency=0.643s)
[client 281472637631280] sent frame #160 (sent #152)
client drawn frame 151 timestamp 1780224505.3939164 (capture_ts=1780224504.7608483, latency=0.633s)
[capture] frame #161 ts=1780224505.4110355
[client 281472637631280] sent frame #161 (sent #153)
[capture] frame #162 ts=1780224505.4651337
client drawn frame 152 timestamp 1780224505.4655647 (capture_ts=1780224504.8298278, latency=0.636s)
[client 281472637631280] sent frame #162 (sent #154)
client drawn frame 153 timestamp 1780224505.5244298 (capture_ts=1780224504.8989956, latency=0.625s)
[capture] frame #163 ts=1780224505.524674
[client 281472637631280] sent frame #163 (sent #155)
client drawn frame 154 timestamp 1780224505.5757542 (capture_ts=1780224504.9648921, latency=0.611s)
[capture] frame #164 ts=1780224505.58709
[client 281472637631280] sent frame #164 (sent #156)
[capture] frame #165 ts=1780224505.6436198
client drawn frame 155 timestamp 1780224505.6440394 (capture_ts=1780224505.0268729, latency=0.617s)
[client 281472637631280] sent frame #165 (sent #157)
client drawn frame 156 timestamp 1780224505.707951 (capture_ts=1780224505.100218, latency=0.608s)
[capture] frame #166 ts=1780224505.708186
[client 281472637631280] sent frame #166 (sent #158)
client drawn frame 157 timestamp 1780224505.7624142 (capture_ts=1780224505.1610932, latency=0.601s)
[capture] frame #167 ts=1780224505.7811236
[client 281472637631280] sent frame #167 (sent #159)
client drawn frame 158 timestamp 1780224505.840816 (capture_ts=1780224505.2225637, latency=0.618s)
[capture] frame #168 ts=1780224505.8410335
[client 281472637631280] sent frame #168 (sent #160)
client drawn frame 159 timestamp 1780224505.8967967 (capture_ts=1780224505.2875414, latency=0.609s)
[capture] frame #169 ts=1780224505.9116511
[client 281472637631280] sent frame #169 (sent #161)
client drawn frame 160 timestamp 1780224505.9638448 (capture_ts=1780224505.343572, latency=0.620s)
[capture] frame #170 ts=1780224505.9803724
[client 281472637631280] sent frame #170 (sent #162)
client drawn frame 161 timestamp 1780224506.0295582 (capture_ts=1780224505.4110355, latency=0.619s)
[capture] frame #171 ts=1780224506.0409982
[client 281472637631280] sent frame #171 (sent #163)
[capture] frame #172 ts=1780224506.1141646
client drawn frame 162 timestamp 1780224506.114559 (capture_ts=1780224505.4651337, latency=0.649s)
[client 281472637631280] sent frame #172 (sent #164)
[capture] frame #173 ts=1780224506.175076
client drawn frame 163 timestamp 1780224506.1753488 (capture_ts=1780224505.524674, latency=0.651s)
[client 281472637631280] sent frame #173 (sent #165)
client drawn frame 164 timestamp 1780224506.2288382 (capture_ts=1780224505.58709, latency=0.642s)
[capture] frame #174 ts=1780224506.2468672
[client 281472637631280] sent frame #174 (sent #166)
client drawn frame 165 timestamp 1780224506.297941 (capture_ts=1780224505.6436198, latency=0.654s)
[capture] frame #175 ts=1780224506.30949
[client 281472637631280] sent frame #175 (sent #167)
client drawn frame 166 timestamp 1780224506.360798 (capture_ts=1780224505.708186, latency=0.653s)
[capture] frame #176 ts=1780224506.374405
[client 281472637631280] sent frame #176 (sent #168)
client drawn frame 167 timestamp 1780224506.4277923 (capture_ts=1780224505.7811236, latency=0.647s)
[capture] frame #177 ts=1780224506.4462411
[client 281472637631280] sent frame #177 (sent #169)
[capture] frame #178 ts=1780224506.5028121
client drawn frame 168 timestamp 1780224506.5032494 (capture_ts=1780224505.8410335, latency=0.662s)
[client 281472637631280] sent frame #178 (sent #170)
client drawn frame 169 timestamp 1780224506.5629923 (capture_ts=1780224505.9116511, latency=0.651s)
[capture] frame #179 ts=1780224506.5632138
[client 281472637631280] sent frame #179 (sent #171)
[capture] frame #180 ts=1780224506.6227453
client drawn frame 170 timestamp 1780224506.6230423 (capture_ts=1780224505.9803724, latency=0.643s)
[client 281472637631280] sent frame #180 (sent #172)
client drawn frame 171 timestamp 1780224506.6848395 (capture_ts=1780224506.0409982, latency=0.644s)
[capture] frame #181 ts=1780224506.6852503
[client 281472637631280] sent frame #181 (sent #173)
client drawn frame 172 timestamp 1780224506.7479029 (capture_ts=1780224506.1141646, latency=0.634s)
[capture] frame #182 ts=1780224506.7482164
[client 281472637631280] sent frame #182 (sent #174)
[capture] frame #183 ts=1780224506.8057315
client drawn frame 173 timestamp 1780224506.8061187 (capture_ts=1780224506.175076, latency=0.631s)
[client 281472637631280] sent frame #183 (sent #175)
[capture] frame #184 ts=1780224506.8614488
client drawn frame 174 timestamp 1780224506.8618267 (capture_ts=1780224506.2468672, latency=0.615s)
[client 281472637631280] sent frame #184 (sent #176)
client drawn frame 175 timestamp 1780224506.9144356 (capture_ts=1780224506.30949, latency=0.605s)
[capture] frame #185 ts=1780224506.9256036
[client 281472637631280] sent frame #185 (sent #177)
client drawn frame 176 timestamp 1780224506.9901025 (capture_ts=1780224506.374405, latency=0.616s)
[capture] frame #186 ts=1780224506.9903915
[client 281472637631280] sent frame #186 (sent #178)
client drawn frame 177 timestamp 1780224507.0452034 (capture_ts=1780224506.4462411, latency=0.599s)
[capture] frame #187 ts=1780224507.0618806
[client 281472637631280] sent frame #187 (sent #179)
client drawn frame 178 timestamp 1780224507.1145215 (capture_ts=1780224506.5028121, latency=0.612s)
[capture] frame #188 ts=1780224507.1259844
[client 281472637631280] sent frame #188 (sent #180)
client drawn frame 179 timestamp 1780224507.17786 (capture_ts=1780224506.5632138, latency=0.615s)
[capture] frame #189 ts=1780224507.191802
[client 281472637631280] sent frame #189 (sent #181)
client drawn frame 180 timestamp 1780224507.2427323 (capture_ts=1780224506.6227453, latency=0.620s)
[capture] frame #190 ts=1780224507.2629828
[client 281472637631280] sent frame #190 (sent #182)
client drawn frame 181 timestamp 1780224507.3228319 (capture_ts=1780224506.6852503, latency=0.638s)
[capture] frame #191 ts=1780224507.3230548
[client 281472637631280] sent frame #191 (sent #183)
client drawn frame 182 timestamp 1780224507.3768644 (capture_ts=1780224506.7482164, latency=0.629s)
[capture] frame #192 ts=1780224507.3981638
[client 281472637631280] sent frame #192 (sent #184)
[capture] frame #193 ts=1780224507.4548016
client drawn frame 183 timestamp 1780224507.4552221 (capture_ts=1780224506.8057315, latency=0.649s)
[client 281472637631280] sent frame #193 (sent #185)
client drawn frame 184 timestamp 1780224507.5076814 (capture_ts=1780224506.8614488, latency=0.646s)
[capture] frame #194 ts=1780224507.5255172
[client 281472637631280] sent frame #194 (sent #186)
client drawn frame 185 timestamp 1780224507.5782113 (capture_ts=1780224506.9256036, latency=0.653s)
[capture] frame #195 ts=1780224507.5945764
[client 281472637631280] sent frame #195 (sent #187)
client drawn frame 186 timestamp 1780224507.6466415 (capture_ts=1780224506.9903915, latency=0.656s)
[capture] frame #196 ts=1780224507.657812
[client 281472637631280] sent frame #196 (sent #188)
client drawn frame 187 timestamp 1780224507.7116294 (capture_ts=1780224507.0618806, latency=0.650s)
[capture] frame #197 ts=1780224507.7309878
[client 281472637631280] sent frame #197 (sent #189)
[capture] frame #198 ts=1780224507.788652
client drawn frame 188 timestamp 1780224507.7890244 (capture_ts=1780224507.1259844, latency=0.663s)
[client 281472637631280] sent frame #198 (sent #190)
client drawn frame 189 timestamp 1780224507.8419461 (capture_ts=1780224507.191802, latency=0.650s)
[capture] frame #199 ts=1780224507.8584592
[client 281472637631280] sent frame #199 (sent #191)
client drawn frame 190 timestamp 1780224507.9131825 (capture_ts=1780224507.2629828, latency=0.650s)
[capture] frame #200 ts=1780224507.9292524
[client 281472637631280] sent frame #200 (sent #192)
client drawn frame 191 timestamp 1780224507.990719 (capture_ts=1780224507.3230548, latency=0.668s)
[capture] frame #201 ts=1780224507.9909358
[client 281472637631280] sent frame #201 (sent #193)
client drawn frame 192 timestamp 1780224508.0431936 (capture_ts=1780224507.3981638, latency=0.645s)
[capture] frame #202 ts=1780224508.058819
[client 281472637631280] sent frame #202 (sent #194)
client drawn frame 193 timestamp 1780224508.1110046 (capture_ts=1780224507.4548016, latency=0.656s)
[capture] frame #203 ts=1780224508.1294131
[client 281472637631280] sent frame #203 (sent #195)
client drawn frame 194 timestamp 1780224508.1905384 (capture_ts=1780224507.5255172, latency=0.665s)
[capture] frame #204 ts=1780224508.19074
[client 281472637631280] sent frame #204 (sent #196)
client drawn frame 195 timestamp 1780224508.2449634 (capture_ts=1780224507.5945764, latency=0.650s)
[capture] frame #205 ts=1780224508.2589734
[client 281472637631280] sent frame #205 (sent #197)
client drawn frame 196 timestamp 1780224508.3105202 (capture_ts=1780224507.657812, latency=0.653s)
[capture] frame #206 ts=1780224508.3225532
[client 281472637631280] sent frame #206 (sent #198)
client drawn frame 197 timestamp 1780224508.3752282 (capture_ts=1780224507.7309878, latency=0.644s)
[capture] frame #207 ts=1780224508.393436
[client 281472637631280] sent frame #207 (sent #199)
client drawn frame 198 timestamp 1780224508.4461076 (capture_ts=1780224507.788652, latency=0.657s)
[capture] frame #208 ts=1780224508.4612317
[client 281472637631280] sent frame #208 (sent #200)
client drawn frame 199 timestamp 1780224508.5253453 (capture_ts=1780224507.8584592, latency=0.667s)
[capture] frame #209 ts=1780224508.5257013
[client 281472637631280] sent frame #209 (sent #201)
client drawn frame 200 timestamp 1780224508.5780466 (capture_ts=1780224507.9292524, latency=0.649s)
[capture] frame #210 ts=1780224508.590945
[client 281472637631280] sent frame #210 (sent #202)
client drawn frame 201 timestamp 1780224508.6424534 (capture_ts=1780224507.9909358, latency=0.652s)
[capture] frame #211 ts=1780224508.6633778
[client 281472637631280] sent frame #211 (sent #203)
client drawn frame 202 timestamp 1780224508.7160156 (capture_ts=1780224508.058819, latency=0.657s)
[capture] frame #212 ts=1780224508.727207
[client 281472637631280] sent frame #212 (sent #204)
[capture] frame #213 ts=1780224508.7908883
[ws] client disconnected
[client 281472637631280] disconnect: [Errno 32] Broken pipe
[client 281472637631280] releasing active_client_lock
[capture] frame #214 ts=1780224508.8585691
[client 281472648334080] connected /mjpg
[ws] client connected
[capture] frame #215 ts=1780224513.0955784
[capture] frame #216 ts=1780224513.1206653
[capture] frame #217 ts=1780224513.1707149
[client 281472648334080] sent frame #215 (sent #1)
[capture] frame #218 ts=1780224513.1964574
[capture] frame #219 ts=1780224513.2224066
[capture] frame #220 ts=1780224513.268362
client drawn frame 1 timestamp 1780224513.2695186 (capture_ts=1780224495.4565601, latency=17.813s)
[client 281472648334080] sent frame #218 (sent #2)
[capture] frame #221 ts=1780224513.3342595
[client 281472648334080] sent frame #221 (sent #3)
client drawn frame 2 timestamp 1780224513.3942108 (capture_ts=1780224495.495932, latency=17.898s)
[capture] frame #222 ts=1780224513.3946316
[client 281472648334080] sent frame #222 (sent #4)
client drawn frame 3 timestamp 1780224513.4458609 (capture_ts=1780224495.5281603, latency=17.918s)
[capture] frame #223 ts=1780224513.4648678
[client 281472648334080] sent frame #223 (sent #5)
client drawn frame 4 timestamp 1780224513.517571 (capture_ts=1780224495.5899374, latency=17.928s)
[capture] frame #224 ts=1780224513.5343206
[client 281472648334080] sent frame #224 (sent #6)
client drawn frame 5 timestamp 1780224513.59658 (capture_ts=1780224495.612993, latency=17.984s)
[capture] frame #225 ts=1780224513.5967696
[client 281472648334080] sent frame #225 (sent #7)
client drawn frame 6 timestamp 1780224513.6500945 (capture_ts=1780224495.6439352, latency=18.006s)
[capture] frame #226 ts=1780224513.6624606
[client 281472648334080] sent frame #226 (sent #8)
client drawn frame 7 timestamp 1780224513.7159958 (capture_ts=1780224495.687362, latency=18.029s)
[capture] frame #227 ts=1780224513.7377355
[client 281472648334080] sent frame #227 (sent #9)
client drawn frame 8 timestamp 1780224513.7947502 (capture_ts=1780224495.7445195, latency=18.050s)
[capture] frame #228 ts=1780224513.794945
[client 281472648334080] sent frame #228 (sent #10)
client drawn frame 9 timestamp 1780224513.8492131 (capture_ts=1780224495.8247354, latency=18.024s)
[capture] frame #229 ts=1780224513.8651433
[client 281472648334080] sent frame #229 (sent #11)
client drawn frame 10 timestamp 1780224513.9166083 (capture_ts=1780224495.8606074, latency=18.056s)
[capture] frame #230 ts=1780224513.9331992
[client 281472648334080] sent frame #230 (sent #12)
client drawn frame 11 timestamp 1780224513.985757 (capture_ts=1780224495.9224823, latency=18.063s)
[capture] frame #231 ts=1780224513.9971776
[client 281472648334080] sent frame #231 (sent #13)
client drawn frame 12 timestamp 1780224514.0510504 (capture_ts=1780224495.9864845, latency=18.065s)
[capture] frame #232 ts=1780224514.0633874
[client 281472648334080] sent frame #232 (sent #14)
client drawn frame 13 timestamp 1780224514.1175401 (capture_ts=1780224496.0379765, latency=18.080s)
[capture] frame #233 ts=1780224514.130212
[client 281472648334080] sent frame #233 (sent #15)
client drawn frame 14 timestamp 1780224514.182339 (capture_ts=1780224496.1082678, latency=18.074s)
[capture] frame #234 ts=1780224514.2005792
[client 281472648334080] sent frame #234 (sent #16)
client drawn frame 15 timestamp 1780224514.263534 (capture_ts=1780224496.15937, latency=18.104s)
[capture] frame #235 ts=1780224514.2638693
[client 281472648334080] sent frame #235 (sent #17)
client drawn frame 16 timestamp 1780224514.3160925 (capture_ts=1780224496.2189689, latency=18.097s)
[capture] frame #236 ts=1780224514.3376148
[client 281472648334080] sent frame #236 (sent #18)
[capture] frame #237 ts=1780224514.396077
client drawn frame 17 timestamp 1780224514.396493 (capture_ts=1780224496.279539, latency=18.117s)
[client 281472648334080] sent frame #237 (sent #19)
client drawn frame 18 timestamp 1780224514.4479313 (capture_ts=1780224496.3416097, latency=18.106s)
[capture] frame #238 ts=1780224514.4640875
[client 281472648334080] sent frame #238 (sent #20)
client drawn frame 19 timestamp 1780224514.5179014 (capture_ts=1780224496.401132, latency=18.117s)
[capture] frame #239 ts=1780224514.5279481
[client 281472648334080] sent frame #239 (sent #21)
client drawn frame 20 timestamp 1780224514.5797863 (capture_ts=1780224496.461689, latency=18.118s)
[capture] frame #240 ts=1780224514.6019945
[client 281472648334080] sent frame #240 (sent #22)
[capture] frame #241 ts=1780224514.663027
client drawn frame 21 timestamp 1780224514.663351 (capture_ts=1780224496.5205193, latency=18.143s)
[client 281472648334080] sent frame #241 (sent #23)
client drawn frame 22 timestamp 1780224514.7176917 (capture_ts=1780224496.5805054, latency=18.137s)
[capture] frame #242 ts=1780224514.7368283
[client 281472648334080] sent frame #242 (sent #24)
client drawn frame 23 timestamp 1780224514.7961643 (capture_ts=1780224496.641566, latency=18.155s)
[capture] frame #243 ts=1780224514.796434
[client 281472648334080] sent frame #243 (sent #25)
client drawn frame 24 timestamp 1780224514.8492308 (capture_ts=1780224496.6993434, latency=18.150s)
[capture] frame #244 ts=1780224514.8647513
[client 281472648334080] sent frame #244 (sent #26)
client drawn frame 25 timestamp 1780224514.918355 (capture_ts=1780224496.7597048, latency=18.159s)
[capture] frame #245 ts=1780224514.9349186
[client 281472648334080] sent frame #245 (sent #27)
client drawn frame 26 timestamp 1780224514.9968467 (capture_ts=1780224496.822941, latency=18.174s)
[capture] frame #246 ts=1780224514.997048
[client 281472648334080] sent frame #246 (sent #28)
client drawn frame 27 timestamp 1780224515.0533938 (capture_ts=1780224496.879808, latency=18.174s)
[capture] frame #247 ts=1780224515.065018
[client 281472648334080] sent frame #247 (sent #29)
client drawn frame 28 timestamp 1780224515.1163642 (capture_ts=1780224496.9400587, latency=18.176s)
[capture] frame #248 ts=1780224515.1347997
[client 281472648334080] sent frame #248 (sent #30)
client drawn frame 29 timestamp 1780224515.1982555 (capture_ts=1780224497.0001132, latency=18.198s)
[capture] frame #249 ts=1780224515.198465
[client 281472648334080] sent frame #249 (sent #31)
[capture] frame #250 ts=1780224515.2622187
client drawn frame 30 timestamp 1780224515.2625225 (capture_ts=1780224497.0633261, latency=18.199s)
[client 281472648334080] sent frame #250 (sent #32)
client drawn frame 31 timestamp 1780224515.3161123 (capture_ts=1780224497.1196227, latency=18.196s)
[capture] frame #251 ts=1780224515.3364756
[client 281472648334080] sent frame #251 (sent #33)
client drawn frame 32 timestamp 1780224515.38967 (capture_ts=1780224497.185395, latency=18.204s)
[capture] frame #252 ts=1780224515.3996599
[client 281472648334080] sent frame #252 (sent #34)
client drawn frame 33 timestamp 1780224515.454275 (capture_ts=1780224497.2391925, latency=18.215s)
[capture] frame #253 ts=1780224515.465157
[client 281472648334080] sent frame #253 (sent #35)
client drawn frame 34 timestamp 1780224515.519897 (capture_ts=1780224497.3031397, latency=18.217s)
[capture] frame #254 ts=1780224515.5334167
[client 281472648334080] sent frame #254 (sent #36)
client drawn frame 35 timestamp 1780224515.5865977 (capture_ts=1780224497.3605075, latency=18.226s)
[capture] frame #255 ts=1780224515.599636
[client 281472648334080] sent frame #255 (sent #37)
client drawn frame 36 timestamp 1780224515.6660395 (capture_ts=1780224497.4212437, latency=18.245s)
[capture] frame #256 ts=1780224515.6663914
[client 281472648334080] sent frame #256 (sent #38)
client drawn frame 37 timestamp 1780224515.718187 (capture_ts=1780224497.4839299, latency=18.234s)
[capture] frame #257 ts=1780224515.7320514
[client 281472648334080] sent frame #257 (sent #39)
client drawn frame 38 timestamp 1780224515.783823 (capture_ts=1780224497.542724, latency=18.241s)
[capture] frame #258 ts=1780224515.7979543
[client 281472648334080] sent frame #258 (sent #40)
client drawn frame 39 timestamp 1780224515.8505301 (capture_ts=1780224497.6016548, latency=18.249s)
[capture] frame #259 ts=1780224515.870591
[client 281472648334080] sent frame #259 (sent #41)
client drawn frame 40 timestamp 1780224515.9215798 (capture_ts=1780224497.6626432, latency=18.259s)
[capture] frame #260 ts=1780224515.932921
[client 281472648334080] sent frame #260 (sent #42)
client drawn frame 41 timestamp 1780224515.9844453 (capture_ts=1780224497.721628, latency=18.263s)
[capture] frame #261 ts=1780224515.9983852
[client 281472648334080] sent frame #261 (sent #43)
client drawn frame 42 timestamp 1780224516.051128 (capture_ts=1780224497.7849777, latency=18.266s)
[capture] frame #262 ts=1780224516.0687654
[client 281472648334080] sent frame #262 (sent #44)
client drawn frame 43 timestamp 1780224516.1199636 (capture_ts=1780224497.8401492, latency=18.280s)
[capture] frame #263 ts=1780224516.1302648
[client 281472648334080] sent frame #263 (sent #45)
client drawn frame 44 timestamp 1780224516.1825445 (capture_ts=1780224497.9029915, latency=18.280s)
[capture] frame #264 ts=1780224516.2040231
[client 281472648334080] sent frame #264 (sent #46)
client drawn frame 45 timestamp 1780224516.2658975 (capture_ts=1780224497.962202, latency=18.304s)
[capture] frame #265 ts=1780224516.2660987
[client 281472648334080] sent frame #265 (sent #47)
client drawn frame 46 timestamp 1780224516.3159785 (capture_ts=1780224498.0229464, latency=18.293s)
[capture] frame #266 ts=1780224516.338817
[client 281472648334080] sent frame #266 (sent #48)
[capture] frame #267 ts=1780224516.3948638
client drawn frame 47 timestamp 1780224516.3952596 (capture_ts=1780224498.082607, latency=18.313s)
[client 281472648334080] sent frame #267 (sent #49)
client drawn frame 48 timestamp 1780224516.4455957 (capture_ts=1780224498.1431437, latency=18.302s)
[capture] frame #268 ts=1780224516.46447
[client 281472648334080] sent frame #268 (sent #50)
[capture] frame #269 ts=1780224516.5167375
client drawn frame 49 timestamp 1780224516.5192056 (capture_ts=1780224498.200205, latency=18.319s)
[client 281472648334080] sent frame #269 (sent #51)
client drawn frame 50 timestamp 1780224516.5694563 (capture_ts=1780224498.262983, latency=18.306s)
[capture] frame #270 ts=1780224516.5905547
[client 281472648334080] sent frame #270 (sent #52)
client drawn frame 51 timestamp 1780224516.6523542 (capture_ts=1780224498.3237576, latency=18.329s)
[capture] frame #271 ts=1780224516.6525607
[client 281472648334080] sent frame #271 (sent #53)
client drawn frame 52 timestamp 1780224516.7044408 (capture_ts=1780224498.3820202, latency=18.322s)
[capture] frame #272 ts=1780224516.7190437
[client 281472648334080] sent frame #272 (sent #54)
client drawn frame 53 timestamp 1780224516.7719572 (capture_ts=1780224498.4422398, latency=18.330s)
[capture] frame #273 ts=1780224516.782919
[client 281472648334080] sent frame #273 (sent #55)
client drawn frame 54 timestamp 1780224516.8345568 (capture_ts=1780224498.5016656, latency=18.333s)
[capture] frame #274 ts=1780224516.8518398
[client 281472648334080] sent frame #274 (sent #56)
client drawn frame 55 timestamp 1780224516.902425 (capture_ts=1780224498.564517, latency=18.338s)
[capture] frame #275 ts=1780224516.9204872
[client 281472648334080] sent frame #275 (sent #57)
client drawn frame 56 timestamp 1780224516.9730127 (capture_ts=1780224498.6244254, latency=18.349s)
[capture] frame #276 ts=1780224516.9862504
[client 281472648334080] sent frame #276 (sent #58)
client drawn frame 57 timestamp 1780224517.037149 (capture_ts=1780224498.683852, latency=18.353s)
[capture] frame #277 ts=1780224517.057628
[client 281472648334080] sent frame #277 (sent #59)
client drawn frame 58 timestamp 1780224517.1097608 (capture_ts=1780224498.7434926, latency=18.366s)
[capture] frame #278 ts=1780224517.121754
[client 281472648334080] sent frame #278 (sent #60)
client drawn frame 59 timestamp 1780224517.1746454 (capture_ts=1780224498.804306, latency=18.370s)
[capture] frame #279 ts=1780224517.1850827
[client 281472648334080] sent frame #279 (sent #61)
client drawn frame 60 timestamp 1780224517.2380059 (capture_ts=1780224498.8631115, latency=18.375s)
[capture] frame #280 ts=1780224517.2540147
[client 281472648334080] sent frame #280 (sent #62)
client drawn frame 61 timestamp 1780224517.3036938 (capture_ts=1780224498.9236963, latency=18.380s)
[capture] frame #281 ts=1780224517.323479
[client 281472648334080] sent frame #281 (sent #63)
client drawn frame 62 timestamp 1780224517.375725 (capture_ts=1780224498.981008, latency=18.395s)
[capture] frame #282 ts=1780224517.3883035
[client 281472648334080] sent frame #282 (sent #64)
client drawn frame 63 timestamp 1780224517.4392638 (capture_ts=1780224499.0455098, latency=18.394s)
[capture] frame #283 ts=1780224517.4516957
[client 281472648334080] sent frame #283 (sent #65)
client drawn frame 64 timestamp 1780224517.5035508 (capture_ts=1780224499.1046476, latency=18.399s)
[capture] frame #284 ts=1780224517.5200367
[client 281472648334080] sent frame #284 (sent #66)
client drawn frame 65 timestamp 1780224517.5712082 (capture_ts=1780224499.1651087, latency=18.406s)
[capture] frame #285 ts=1780224517.5905638
[client 281472648334080] sent frame #285 (sent #67)
[capture] frame #286 ts=1780224517.6486938
client drawn frame 66 timestamp 1780224517.649008 (capture_ts=1780224499.2233338, latency=18.426s)
[client 281472648334080] sent frame #286 (sent #68)
client drawn frame 67 timestamp 1780224517.710875 (capture_ts=1780224499.2866821, latency=18.424s)
[capture] frame #287 ts=1780224517.7111368
[client 281472648334080] sent frame #287 (sent #69)
client drawn frame 68 timestamp 1780224517.773406 (capture_ts=1780224499.3428419, latency=18.431s)
[capture] frame #288 ts=1780224517.7736895
[client 281472648334080] sent frame #288 (sent #70)
[capture] frame #289 ts=1780224517.8317003
client drawn frame 69 timestamp 1780224517.8321233 (capture_ts=1780224499.4071949, latency=18.425s)
[client 281472648334080] sent frame #289 (sent #71)
[capture] frame #290 ts=1780224517.8936622
client drawn frame 70 timestamp 1780224517.8939178 (capture_ts=1780224499.4621909, latency=18.432s)
[client 281472648334080] sent frame #290 (sent #72)
[capture] frame #291 ts=1780224517.9506578
client drawn frame 71 timestamp 1780224517.9510567 (capture_ts=1780224499.5316315, latency=18.419s)
[client 281472648334080] sent frame #291 (sent #73)
[capture] frame #292 ts=1780224518.010568
client drawn frame 72 timestamp 1780224518.0109417 (capture_ts=1780224499.5824645, latency=18.428s)
[client 281472648334080] sent frame #292 (sent #74)
[capture] frame #293 ts=1780224518.069439
client drawn frame 73 timestamp 1780224518.0696962 (capture_ts=1780224499.6470735, latency=18.423s)
[client 281472648334080] sent frame #293 (sent #75)
client drawn frame 74 timestamp 1780224518.135475 (capture_ts=1780224499.7050502, latency=18.430s)
[capture] frame #294 ts=1780224518.135708
[client 281472648334080] sent frame #294 (sent #76)
[capture] frame #295 ts=1780224518.1895487
client drawn frame 75 timestamp 1780224518.189898 (capture_ts=1780224499.7637022, latency=18.426s)
[client 281472648334080] sent frame #295 (sent #77)
[capture] frame #296 ts=1780224518.2520087
client drawn frame 76 timestamp 1780224518.2523441 (capture_ts=1780224499.8263881, latency=18.426s)
[client 281472648334080] sent frame #296 (sent #78)
client drawn frame 77 timestamp 1780224518.3108451 (capture_ts=1780224499.882236, latency=18.429s)
[capture] frame #297 ts=1780224518.3110805
[client 281472648334080] sent frame #297 (sent #79)
[capture] frame #298 ts=1780224518.3704317
client drawn frame 78 timestamp 1780224518.3707983 (capture_ts=1780224499.953093, latency=18.418s)
[client 281472648334080] sent frame #298 (sent #80)
client drawn frame 79 timestamp 1780224518.4335823 (capture_ts=1780224500.005789, latency=18.428s)
[capture] frame #299 ts=1780224518.433791
[client 281472648334080] sent frame #299 (sent #81)
[capture] frame #300 ts=1780224518.4912333
client drawn frame 80 timestamp 1780224518.49166 (capture_ts=1780224500.065555, latency=18.426s)
[client 281472648334080] sent frame #300 (sent #82)
client drawn frame 81 timestamp 1780224518.5508025 (capture_ts=1780224500.123601, latency=18.427s)
[capture] frame #301 ts=1780224518.551054
[client 281472648334080] sent frame #301 (sent #83)
[capture] frame #302 ts=1780224518.6114402
client drawn frame 82 timestamp 1780224518.6116843 (capture_ts=1780224500.1945713, latency=18.417s)
[client 281472648334080] sent frame #302 (sent #84)
[ws] client disconnected
[capture] frame #303 ts=1780224518.67161
[client 281472648334080] disconnect: [Errno 32] Broken pipe
[client 281472648334080] releasing active_client_lock
[capture] frame #304 ts=1780224518.730658
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

