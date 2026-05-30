# HowTo-Ubuntu24S-Raspicam-Webserver-Streaming

Create a streaming webserver on Ubuntu 24 server LTS with raspicam. It's harder than on RaspberryPi OS because there is no native libcamera.

![](/images/2026-05-30_07_28_IMG_20260530_072810%20Raspberry%20Pi%204B%20Ubuntu%2024%20Server%20LTS%20Ethernet%20and%20WiFi.jpg)

## Plan

The plan is to compile from source a RaspberryPi OS C++ raspicam application, patching everything that is needed from APT to make it work

I tried over a dozen guides and methods, the only one that worked is this [guide](https://dev.to/minindu_pasan_8f0e03c1063/how-to-setup-raspberry-pi-camera-module-3-on-ubuntu-2404-4pme)



# Install OS

Start with a clean Ubuntu 24 Server install on a Raspberry Pi 4

[GUIDE](https://github.com/OrsoEric/HowTo-Ubuntu-RaspberryPi)

# Fix Ubuntu APT Sources

Ubuntu APT is bricked by default on fresh install by leaving out the sources you need for APT packages.

This is what you'd get if you don't unbrick the Ubuntu APT Sources

```bash
The following packages have unmet dependencies:
 libidn2-dev : Depends: libidn2-0 (= 2.3.7-2build1) but 2.3.7-2build1.1 is to be installed
 libp11-kit-dev : Depends: libp11-kit0 (= 0.25.3-4ubuntu2) but 0.25.3-4ubuntu2.1 is to be installed
 libzstd-dev : Depends: libzstd1 (= 1.5.5+dfsg2-2build1) but 1.5.5+dfsg2-2build1.1 is to be installed
 nettle-dev : Depends: libnettle8t64 (= 3.9.1-2.2build1) but 3.9.1-2.2build1.1 is to be installed
              Depends: libhogweed6t64 (= 3.9.1-2.2build1) but 3.9.1-2.2build1.1 is to be installed
              Depends: libgmp-dev but it is not going to be installed
 zlib1g-dev : Depends: zlib1g (= 1:1.3.dfsg-3.1ubuntu2) but 1:1.3.dfsg-3.1ubuntu2.1 is to be installed
E: Unable to correct problems, you have held broken packages.
```

In order to restore Ubuntu to working operation after clean install you need to **manually** add sources to the APT config file.


```bash
sudo nano /etc/apt/sources.list.d/ubuntu.sources

#MANUALLY ADD noble-updates noble-backports AND SAVE
#Suites: noble noble-updates noble-backports

sudo apt update 

sudo apt full-upgrade

sudo reboot
```

This is what a working APT source should look like

```bash
sona@rpi-orso-sdb:~/2026-05-29-picamera2$ cat /etc/apt/sources.list.d/ubuntu.sources
## Ubuntu distribution repository
##
## The following settings can be adjusted to configure which packages to use from Ubuntu.
## Mirror your choices (except for URIs and Suites) in the security section below to
## ensure timely security updates.
##
## Types: Append deb-src to enable the fetching of source package.
## URIs: A URL to the repository (you may add multiple URLs)
## Suites: The following additional suites can be configured
##   <name>-updates   - Major bug fix updates produced after the final release of the
##                      distribution.
##   <name>-backports - software from this repository may not have been tested as
##                      extensively as that contained in the main release, although it includes
##                      newer versions of some applications which may provide useful features.
##                      Also, please note that software in backports WILL NOT receive any review
##                      or updates from the Ubuntu security team.
## Components: Aside from main, the following components can be added to the list
##   restricted  - Software that may not be under a free license, or protected by patents.
##   universe    - Community maintained packages. Software in this repository receives maintenance
##                 from volunteers in the Ubuntu community, or a 10 year security maintenance
##                 commitment from Canonical when an Ubuntu Pro subscription is attached.
##   multiverse  - Community maintained of restricted. Software from this repository is
##                 ENTIRELY UNSUPPORTED by the Ubuntu team, and may not be under a free
##                 licence. Please satisfy yourself as to your rights to use the software.
##                 Also, please note that software in multiverse WILL NOT receive any
##                 review or updates from the Ubuntu security team.
##
## See the sources.list(5) manual page for further settings.
Types: deb
URIs: http://ports.ubuntu.com/ubuntu-ports/
Suites: noble noble-updates noble-backports
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

## Ubuntu security updates. Aside from URIs and Suites,
## this should mirror your choices in the previous section.
Types: deb
URIs: http://ports.ubuntu.com/ubuntu-ports/
Suites: noble-security
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```

# Remove packages that shouldn't be there

```bash

sudo apt remove --purge rpicam-apps
sudo apt remove --purge libcamera-dev libcamera0
```

```bash
sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ sudo apt remove --purge rpicam-apps
sudo apt remove --purge libcamera-dev libcamera0
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package rpicam-apps
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Package 'libcamera0' is not installed, so not removed
Package 'libcamera-dev' is not installed, so not removed
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```


# Essential build tools

```bash
sudo apt install -y git python3-pip python3-jinja2 meson cmake ninja-build
```

<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ sudo apt install -y git python3-pip python3-jinja2 meson cmake ninja-build
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
git is already the newest version (1:2.43.0-1ubuntu7.3).
python3-jinja2 is already the newest version (3.1.2-1ubuntu1.3).
python3-jinja2 set to manually installed.
The following additional packages will be installed:
  cmake-data cpp cpp-13 cpp-13-aarch64-linux-gnu
  cpp-aarch64-linux-gnu fontconfig-config fonts-dejavu-core
  fonts-dejavu-mono gcc gcc-13 gcc-13-aarch64-linux-gnu gcc-13-base
  gcc-aarch64-linux-gnu libaom3 libasan8 libatomic1 libc-dev-bin
  libc-devtools libc6-dev libcc1-0 libcrypt-dev libde265-0
  libdeflate0 libfontconfig1 libfreetype6 libgcc-13-dev libgd3
  libgomp1 libheif-plugin-aomdec libheif-plugin-aomenc
  libheif-plugin-libde265 libheif1 libhwasan0 libisl23 libitm1
  libjbig0 libjpeg-turbo8 libjpeg8 libjsoncpp25 liblerc4 liblsan0
  libmpc3 librhash0 libsharpyuv0 libtiff6 libtsan2 libubsan1
  libwebp7 libxpm4 linux-libc-dev make manpages-dev python3-wheel
  rpcsvc-proto
Suggested packages:
  cmake-doc cmake-format elpa-cmake-mode cpp-doc gcc-13-locales
  cpp-13-doc gcc-multilib autoconf automake libtool flex bison gdb
  gcc-doc gcc-13-doc gdb-aarch64-linux-gnu glibc-doc libgd-tools
  libheif-plugin-x265 libheif-plugin-ffmpegdec
  libheif-plugin-jpegdec libheif-plugin-jpegenc
  libheif-plugin-j2kdec libheif-plugin-j2kenc libheif-plugin-rav1e
  libheif-plugin-svtenc make-doc
Recommended packages:
  dpkg-dev build-essential python3-dev
The following NEW packages will be installed:
  cmake cmake-data cpp cpp-13 cpp-13-aarch64-linux-gnu
  cpp-aarch64-linux-gnu fontconfig-config fonts-dejavu-core
  fonts-dejavu-mono gcc gcc-13 gcc-13-aarch64-linux-gnu gcc-13-base
  gcc-aarch64-linux-gnu libaom3 libasan8 libatomic1 libc-dev-bin
  libc-devtools libc6-dev libcc1-0 libcrypt-dev libde265-0
  libdeflate0 libfontconfig1 libfreetype6 libgcc-13-dev libgd3
  libgomp1 libheif-plugin-aomdec libheif-plugin-aomenc
  libheif-plugin-libde265 libheif1 libhwasan0 libisl23 libitm1
  libjbig0 libjpeg-turbo8 libjpeg8 libjsoncpp25 liblerc4 liblsan0
  libmpc3 librhash0 libsharpyuv0 libtiff6 libtsan2 libubsan1
  libwebp7 libxpm4 linux-libc-dev make manpages-dev meson
  ninja-build python3-pip python3-wheel rpcsvc-proto
0 upgraded, 58 newly installed, 0 to remove and 0 not upgraded.
Need to get 67.1 MB of archives.
After this operation, 228 MB of additional disk space will be used.
Get:1 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libjsoncpp25 arm64 1.9.5-6build1 [78.2 kB]
Get:2 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 librhash0 arm64 1.4.3-3build1 [126 kB]
Get:3 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 cmake-data all 3.28.3-1build7 [2155 kB]
Get:4 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 cmake arm64 3.28.3-1build7 [10.3 MB]
Get:5 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 gcc-13-base arm64 13.3.0-6ubuntu2~24.04.1 [51.6 kB]
Get:6 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libisl23 arm64 0.26-3build1 [669 kB]
Get:7 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libmpc3 arm64 1.3.1-1build1 [56.4 kB]
Get:8 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 cpp-13-aarch64-linux-gnu arm64 13.3.0-6ubuntu2~24.04.1 [9560 kB]
Get:9 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 cpp-13 arm64 13.3.0-6ubuntu2~24.04.1 [1038 B]
Get:10 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 cpp-aarch64-linux-gnu arm64 4:13.2.0-7ubuntu1 [5316 B]
Get:11 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 cpp arm64 4:13.2.0-7ubuntu1 [22.4 kB]
Get:12 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 fonts-dejavu-mono all 2.37-8 [502 kB]
Get:13 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 fonts-dejavu-core all 2.37-8 [835 kB]
Get:14 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 fontconfig-config arm64 2.15.0-1.1ubuntu2 [37.4 kB]
Get:15 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libcc1-0 arm64 14.2.0-4ubuntu2~24.04.1 [49.7 kB]
Get:16 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libgomp1 arm64 14.2.0-4ubuntu2~24.04.1 [145 kB]
Get:17 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libitm1 arm64 14.2.0-4ubuntu2~24.04.1 [28.2 kB]
Get:18 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libatomic1 arm64 14.2.0-4ubuntu2~24.04.1 [11.6 kB]
Get:19 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libasan8 arm64 14.2.0-4ubuntu2~24.04.1 [2928 kB]
Get:20 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 liblsan0 arm64 14.2.0-4ubuntu2~24.04.1 [1289 kB]
Get:21 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libtsan2 arm64 14.2.0-4ubuntu2~24.04.1 [2697 kB]
Get:22 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libubsan1 arm64 14.2.0-4ubuntu2~24.04.1 [1157 kB]
Get:23 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libhwasan0 arm64 14.2.0-4ubuntu2~24.04.1 [1605 kB]
Get:24 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libgcc-13-dev arm64 13.3.0-6ubuntu2~24.04.1 [2473 kB]
Get:25 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 gcc-13-aarch64-linux-gnu arm64 13.3.0-6ubuntu2~24.04.1 [18.7 MB]
Get:26 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 gcc-13 arm64 13.3.0-6ubuntu2~24.04.1 [484 kB]
Get:27 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 gcc-aarch64-linux-gnu arm64 4:13.2.0-7ubuntu1 [1198 B]
Get:28 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 gcc arm64 4:13.2.0-7ubuntu1 [5018 B]
Get:29 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libaom3 arm64 3.8.2-2ubuntu0.1 [1617 kB]
Get:30 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libc-dev-bin arm64 2.39-0ubuntu8.7 [19.7 kB]
Get:31 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libfreetype6 arm64 2.13.2+dfsg-1ubuntu0.1 [394 kB]
Get:32 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libfontconfig1 arm64 2.15.0-1.1ubuntu2 [142 kB]
Get:33 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libsharpyuv0 arm64 1.3.2-0.4build3 [14.5 kB]
Get:34 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libheif-plugin-aomdec arm64 1.17.6-1ubuntu4.2 [10.4 kB]
Get:35 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libde265-0 arm64 1.0.15-1build3 [143 kB]
Get:36 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libheif-plugin-libde265 arm64 1.17.6-1ubuntu4.2 [8016 B]
Get:37 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libheif1 arm64 1.17.6-1ubuntu4.2 [260 kB]
Get:38 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libjpeg-turbo8 arm64 2.1.5-2ubuntu2 [163 kB]
Get:39 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libjpeg8 arm64 8c-2ubuntu11 [2148 B]
Get:40 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libdeflate0 arm64 1.19-1build1 [43.4 kB]
Get:41 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libjbig0 arm64 2.1-6.1ubuntu2 [29.3 kB]
Get:42 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 liblerc4 arm64 4.0.0+ds-4ubuntu2 [154 kB]
Get:43 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libwebp7 arm64 1.3.2-0.4build3 [191 kB]
Get:44 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libtiff6 arm64 4.5.1+git230720-4ubuntu2.5 [192 kB]
Get:45 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxpm4 arm64 1:3.5.17-1build2 [35.1 kB]
Get:46 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libgd3 arm64 2.3.3-9ubuntu5 [122 kB]
Get:47 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libc-devtools arm64 2.39-0ubuntu8.7 [27.8 kB]
Get:48 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 linux-libc-dev arm64 6.8.0-117.117 [1470 kB]
Get:49 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libcrypt-dev arm64 1:4.4.36-4build1 [118 kB]
Get:50 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 rpcsvc-proto arm64 1.4.2-0ubuntu7 [64.8 kB]
Get:51 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libc6-dev arm64 2.39-0ubuntu8.7 [1596 kB]
Get:52 http://ports.ubuntu.com/ubuntu-ports noble-security/main arm64 libheif-plugin-aomenc arm64 1.17.6-1ubuntu4.2 [13.7 kB]
Get:53 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 make arm64 4.3-4.1build2 [178 kB]
Get:54 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 manpages-dev all 6.7-2 [2013 kB]
Get:55 http://ports.ubuntu.com/ubuntu-ports noble/universe arm64 ninja-build arm64 1.11.1-2 [125 kB]
Get:56 http://ports.ubuntu.com/ubuntu-ports noble/universe arm64 meson all 1.3.2-1ubuntu1 [604 kB]
Get:57 http://ports.ubuntu.com/ubuntu-ports noble/universe arm64 python3-wheel all 0.42.0-2 [53.1 kB]
Get:58 http://ports.ubuntu.com/ubuntu-ports noble-security/universe arm64 python3-pip all 24.0+dfsg-1ubuntu1.3 [1320 kB]
Fetched 67.1 MB in 7s (10.1 MB/s)                                    
Extracting templates from packages: 100%
Selecting previously unselected package libjsoncpp25:arm64.
(Reading database ... 59155 files and directories currently installed.)
Preparing to unpack .../00-libjsoncpp25_1.9.5-6build1_arm64.deb ...
Unpacking libjsoncpp25:arm64 (1.9.5-6build1) ...
Selecting previously unselected package librhash0:arm64.
Preparing to unpack .../01-librhash0_1.4.3-3build1_arm64.deb ...
Unpacking librhash0:arm64 (1.4.3-3build1) ...
Selecting previously unselected package cmake-data.
Preparing to unpack .../02-cmake-data_3.28.3-1build7_all.deb ...
Unpacking cmake-data (3.28.3-1build7) ...
Selecting previously unselected package cmake.
Preparing to unpack .../03-cmake_3.28.3-1build7_arm64.deb ...
Unpacking cmake (3.28.3-1build7) ...
Selecting previously unselected package gcc-13-base:arm64.
Preparing to unpack .../04-gcc-13-base_13.3.0-6ubuntu2~24.04.1_arm64.deb ...
Unpacking gcc-13-base:arm64 (13.3.0-6ubuntu2~24.04.1) ...
Selecting previously unselected package libisl23:arm64.
Preparing to unpack .../05-libisl23_0.26-3build1_arm64.deb ...
Unpacking libisl23:arm64 (0.26-3build1) ...
Selecting previously unselected package libmpc3:arm64.
Preparing to unpack .../06-libmpc3_1.3.1-1build1_arm64.deb ...
Unpacking libmpc3:arm64 (1.3.1-1build1) ...
Selecting previously unselected package cpp-13-aarch64-linux-gnu.
Preparing to unpack .../07-cpp-13-aarch64-linux-gnu_13.3.0-6ubuntu2~24.04.1_arm64.deb ...
Unpacking cpp-13-aarch64-linux-gnu (13.3.0-6ubuntu2~24.04.1) ...
Selecting previously unselected package cpp-13.
Preparing to unpack .../08-cpp-13_13.3.0-6ubuntu2~24.04.1_arm64.deb ...
Unpacking cpp-13 (13.3.0-6ubuntu2~24.04.1) ...
Selecting previously unselected package cpp-aarch64-linux-gnu.
Preparing to unpack .../09-cpp-aarch64-linux-gnu_4%3a13.2.0-7ubuntu1_arm64.deb ...
Unpacking cpp-aarch64-linux-gnu (4:13.2.0-7ubuntu1) ...
Selecting previously unselected package cpp.
Preparing to unpack .../10-cpp_4%3a13.2.0-7ubuntu1_arm64.deb ...
Unpacking cpp (4:13.2.0-7ubuntu1) ...
Selecting previously unselected package fonts-dejavu-mono.
Preparing to unpack .../11-fonts-dejavu-mono_2.37-8_all.deb ...
Unpacking fonts-dejavu-mono (2.37-8) ...
Selecting previously unselected package fonts-dejavu-core.
Preparing to unpack .../12-fonts-dejavu-core_2.37-8_all.deb ...
Unpacking fonts-dejavu-core (2.37-8) ...
Selecting previously unselected package fontconfig-config.
Preparing to unpack .../13-fontconfig-config_2.15.0-1.1ubuntu2_arm64.deb ...
Unpacking fontconfig-config (2.15.0-1.1ubuntu2) ...
Selecting previously unselected package libcc1-0:arm64.
Preparing to unpack .../14-libcc1-0_14.2.0-4ubuntu2~24.04.1_arm64.deb ...
Unpacking libcc1-0:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Selecting previously unselected package libgomp1:arm64.
Preparing to unpack .../15-libgomp1_14.2.0-4ubuntu2~24.04.1_arm64.deb ...
Unpacking libgomp1:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Selecting previously unselected package libitm1:arm64.
Preparing to unpack .../16-libitm1_14.2.0-4ubuntu2~24.04.1_arm64.deb ...
Unpacking libitm1:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Selecting previously unselected package libatomic1:arm64.
Preparing to unpack .../17-libatomic1_14.2.0-4ubuntu2~24.04.1_arm64.deb ...
Unpacking libatomic1:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Selecting previously unselected package libasan8:arm64.
Preparing to unpack .../18-libasan8_14.2.0-4ubuntu2~24.04.1_arm64.deb ...
Unpacking libasan8:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Selecting previously unselected package liblsan0:arm64.
Preparing to unpack .../19-liblsan0_14.2.0-4ubuntu2~24.04.1_arm64.deb ...
Unpacking liblsan0:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Selecting previously unselected package libtsan2:arm64.
Preparing to unpack .../20-libtsan2_14.2.0-4ubuntu2~24.04.1_arm64.deb ...
Unpacking libtsan2:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Selecting previously unselected package libubsan1:arm64.
Preparing to unpack .../21-libubsan1_14.2.0-4ubuntu2~24.04.1_arm64.deb ...
Unpacking libubsan1:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Selecting previously unselected package libhwasan0:arm64.
Preparing to unpack .../22-libhwasan0_14.2.0-4ubuntu2~24.04.1_arm64.deb ...
Unpacking libhwasan0:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Selecting previously unselected package libgcc-13-dev:arm64.
Preparing to unpack .../23-libgcc-13-dev_13.3.0-6ubuntu2~24.04.1_arm64.deb ...
Unpacking libgcc-13-dev:arm64 (13.3.0-6ubuntu2~24.04.1) ...
Selecting previously unselected package gcc-13-aarch64-linux-gnu.
Preparing to unpack .../24-gcc-13-aarch64-linux-gnu_13.3.0-6ubuntu2~24.04.1_arm64.deb ...
Unpacking gcc-13-aarch64-linux-gnu (13.3.0-6ubuntu2~24.04.1) ...
Selecting previously unselected package gcc-13.
Preparing to unpack .../25-gcc-13_13.3.0-6ubuntu2~24.04.1_arm64.deb ...
Unpacking gcc-13 (13.3.0-6ubuntu2~24.04.1) ...
Selecting previously unselected package gcc-aarch64-linux-gnu.
Preparing to unpack .../26-gcc-aarch64-linux-gnu_4%3a13.2.0-7ubuntu1_arm64.deb ...
Unpacking gcc-aarch64-linux-gnu (4:13.2.0-7ubuntu1) ...
Selecting previously unselected package gcc.
Preparing to unpack .../27-gcc_4%3a13.2.0-7ubuntu1_arm64.deb ...
Unpacking gcc (4:13.2.0-7ubuntu1) ...
Selecting previously unselected package libaom3:arm64.
Preparing to unpack .../28-libaom3_3.8.2-2ubuntu0.1_arm64.deb ...
Unpacking libaom3:arm64 (3.8.2-2ubuntu0.1) ...
Selecting previously unselected package libc-dev-bin.
Preparing to unpack .../29-libc-dev-bin_2.39-0ubuntu8.7_arm64.deb ...
Unpacking libc-dev-bin (2.39-0ubuntu8.7) ...
Selecting previously unselected package libfreetype6:arm64.
Preparing to unpack .../30-libfreetype6_2.13.2+dfsg-1ubuntu0.1_arm64.deb ...
Unpacking libfreetype6:arm64 (2.13.2+dfsg-1ubuntu0.1) ...
Selecting previously unselected package libfontconfig1:arm64.
Preparing to unpack .../31-libfontconfig1_2.15.0-1.1ubuntu2_arm64.deb ...
Unpacking libfontconfig1:arm64 (2.15.0-1.1ubuntu2) ...
Selecting previously unselected package libsharpyuv0:arm64.
Preparing to unpack .../32-libsharpyuv0_1.3.2-0.4build3_arm64.deb ...
Unpacking libsharpyuv0:arm64 (1.3.2-0.4build3) ...
Selecting previously unselected package libheif-plugin-aomdec:arm64.
Preparing to unpack .../33-libheif-plugin-aomdec_1.17.6-1ubuntu4.2_arm64.deb ...
Unpacking libheif-plugin-aomdec:arm64 (1.17.6-1ubuntu4.2) ...
Selecting previously unselected package libde265-0:arm64.
Preparing to unpack .../34-libde265-0_1.0.15-1build3_arm64.deb ...
Unpacking libde265-0:arm64 (1.0.15-1build3) ...
Selecting previously unselected package libheif-plugin-libde265:arm64.
Preparing to unpack .../35-libheif-plugin-libde265_1.17.6-1ubuntu4.2_arm64.deb ...
Unpacking libheif-plugin-libde265:arm64 (1.17.6-1ubuntu4.2) ...
Selecting previously unselected package libheif1:arm64.
Preparing to unpack .../36-libheif1_1.17.6-1ubuntu4.2_arm64.deb ...
Unpacking libheif1:arm64 (1.17.6-1ubuntu4.2) ...
Selecting previously unselected package libjpeg-turbo8:arm64.
Preparing to unpack .../37-libjpeg-turbo8_2.1.5-2ubuntu2_arm64.deb ...
Unpacking libjpeg-turbo8:arm64 (2.1.5-2ubuntu2) ...
Selecting previously unselected package libjpeg8:arm64.
Preparing to unpack .../38-libjpeg8_8c-2ubuntu11_arm64.deb ...
Unpacking libjpeg8:arm64 (8c-2ubuntu11) ...
Selecting previously unselected package libdeflate0:arm64.
Preparing to unpack .../39-libdeflate0_1.19-1build1_arm64.deb ...
Unpacking libdeflate0:arm64 (1.19-1build1) ...
Selecting previously unselected package libjbig0:arm64.
Preparing to unpack .../40-libjbig0_2.1-6.1ubuntu2_arm64.deb ...
Unpacking libjbig0:arm64 (2.1-6.1ubuntu2) ...
Selecting previously unselected package liblerc4:arm64.
Preparing to unpack .../41-liblerc4_4.0.0+ds-4ubuntu2_arm64.deb ...
Unpacking liblerc4:arm64 (4.0.0+ds-4ubuntu2) ...
Selecting previously unselected package libwebp7:arm64.
Preparing to unpack .../42-libwebp7_1.3.2-0.4build3_arm64.deb ...
Unpacking libwebp7:arm64 (1.3.2-0.4build3) ...
Selecting previously unselected package libtiff6:arm64.
Preparing to unpack .../43-libtiff6_4.5.1+git230720-4ubuntu2.5_arm64.deb ...
Unpacking libtiff6:arm64 (4.5.1+git230720-4ubuntu2.5) ...
Selecting previously unselected package libxpm4:arm64.
Preparing to unpack .../44-libxpm4_1%3a3.5.17-1build2_arm64.deb ...
Unpacking libxpm4:arm64 (1:3.5.17-1build2) ...
Selecting previously unselected package libgd3:arm64.
Preparing to unpack .../45-libgd3_2.3.3-9ubuntu5_arm64.deb ...
Unpacking libgd3:arm64 (2.3.3-9ubuntu5) ...
Selecting previously unselected package libc-devtools.
Preparing to unpack .../46-libc-devtools_2.39-0ubuntu8.7_arm64.deb ...
Unpacking libc-devtools (2.39-0ubuntu8.7) ...
Selecting previously unselected package linux-libc-dev:arm64.
Preparing to unpack .../47-linux-libc-dev_6.8.0-117.117_arm64.deb ...
Unpacking linux-libc-dev:arm64 (6.8.0-117.117) ...
Selecting previously unselected package libcrypt-dev:arm64.
Preparing to unpack .../48-libcrypt-dev_1%3a4.4.36-4build1_arm64.deb ...
Unpacking libcrypt-dev:arm64 (1:4.4.36-4build1) ...
Selecting previously unselected package rpcsvc-proto.
Preparing to unpack .../49-rpcsvc-proto_1.4.2-0ubuntu7_arm64.deb ...
Unpacking rpcsvc-proto (1.4.2-0ubuntu7) ...
Selecting previously unselected package libc6-dev:arm64.
Preparing to unpack .../50-libc6-dev_2.39-0ubuntu8.7_arm64.deb ...
Unpacking libc6-dev:arm64 (2.39-0ubuntu8.7) ...
Selecting previously unselected package libheif-plugin-aomenc:arm64.
Preparing to unpack .../51-libheif-plugin-aomenc_1.17.6-1ubuntu4.2_arm64.deb ...
Unpacking libheif-plugin-aomenc:arm64 (1.17.6-1ubuntu4.2) ...
Selecting previously unselected package make.
Preparing to unpack .../52-make_4.3-4.1build2_arm64.deb ...
Unpacking make (4.3-4.1build2) ...
Selecting previously unselected package manpages-dev.
Preparing to unpack .../53-manpages-dev_6.7-2_all.deb ...
Unpacking manpages-dev (6.7-2) ...
Selecting previously unselected package ninja-build.
Preparing to unpack .../54-ninja-build_1.11.1-2_arm64.deb ...
Unpacking ninja-build (1.11.1-2) ...
Selecting previously unselected package meson.
Preparing to unpack .../55-meson_1.3.2-1ubuntu1_all.deb ...
Unpacking meson (1.3.2-1ubuntu1) ...
Selecting previously unselected package python3-wheel.
Preparing to unpack .../56-python3-wheel_0.42.0-2_all.deb ...
Unpacking python3-wheel (0.42.0-2) ...
Selecting previously unselected package python3-pip.
Preparing to unpack .../57-python3-pip_24.0+dfsg-1ubuntu1.3_all.deb ...
Unpacking python3-pip (24.0+dfsg-1ubuntu1.3) ...
Setting up libsharpyuv0:arm64 (1.3.2-0.4build3) ...
Setting up libaom3:arm64 (3.8.2-2ubuntu0.1) ...
Setting up manpages-dev (6.7-2) ...
Setting up liblerc4:arm64 (4.0.0+ds-4ubuntu2) ...
Setting up libxpm4:arm64 (1:3.5.17-1build2) ...
Setting up libdeflate0:arm64 (1.19-1build1) ...
Setting up linux-libc-dev:arm64 (6.8.0-117.117) ...
Setting up libgomp1:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Setting up python3-wheel (0.42.0-2) ...
Setting up libjbig0:arm64 (2.1-6.1ubuntu2) ...
Setting up ninja-build (1.11.1-2) ...
Setting up rpcsvc-proto (1.4.2-0ubuntu7) ...
Setting up gcc-13-base:arm64 (13.3.0-6ubuntu2~24.04.1) ...
Setting up libfreetype6:arm64 (2.13.2+dfsg-1ubuntu0.1) ...
Setting up make (4.3-4.1build2) ...
Setting up fonts-dejavu-mono (2.37-8) ...
Setting up libmpc3:arm64 (1.3.1-1build1) ...
Setting up libatomic1:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Setting up libjsoncpp25:arm64 (1.9.5-6build1) ...
Setting up fonts-dejavu-core (2.37-8) ...
Setting up python3-pip (24.0+dfsg-1ubuntu1.3) ...
Setting up libjpeg-turbo8:arm64 (2.1.5-2ubuntu2) ...
Setting up libwebp7:arm64 (1.3.2-0.4build3) ...
Setting up libubsan1:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Setting up libhwasan0:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Setting up librhash0:arm64 (1.4.3-3build1) ...
Setting up libcrypt-dev:arm64 (1:4.4.36-4build1) ...
Setting up libasan8:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Setting up cmake-data (3.28.3-1build7) ...
Setting up libtsan2:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Setting up libisl23:arm64 (0.26-3build1) ...
Setting up libde265-0:arm64 (1.0.15-1build3) ...
Setting up libc-dev-bin (2.39-0ubuntu8.7) ...
Setting up libcc1-0:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Setting up liblsan0:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Setting up libitm1:arm64 (14.2.0-4ubuntu2~24.04.1) ...
Setting up libjpeg8:arm64 (8c-2ubuntu11) ...
Setting up cpp-13-aarch64-linux-gnu (13.3.0-6ubuntu2~24.04.1) ...
Setting up fontconfig-config (2.15.0-1.1ubuntu2) ...
Setting up meson (1.3.2-1ubuntu1) ...
Setting up cpp-aarch64-linux-gnu (4:13.2.0-7ubuntu1) ...
Setting up libgcc-13-dev:arm64 (13.3.0-6ubuntu2~24.04.1) ...
Setting up libtiff6:arm64 (4.5.1+git230720-4ubuntu2.5) ...
Setting up cmake (3.28.3-1build7) ...
Setting up libc6-dev:arm64 (2.39-0ubuntu8.7) ...
Setting up cpp-13 (13.3.0-6ubuntu2~24.04.1) ...
Setting up gcc-13-aarch64-linux-gnu (13.3.0-6ubuntu2~24.04.1) ...
Setting up gcc-13 (13.3.0-6ubuntu2~24.04.1) ...
Setting up cpp (4:13.2.0-7ubuntu1) ...
Setting up gcc-aarch64-linux-gnu (4:13.2.0-7ubuntu1) ...
Setting up gcc (4:13.2.0-7ubuntu1) ...
Setting up libheif-plugin-aomdec:arm64 (1.17.6-1ubuntu4.2) ...
Setting up libheif1:arm64 (1.17.6-1ubuntu4.2) ...
Setting up libheif-plugin-libde265:arm64 (1.17.6-1ubuntu4.2) ...
Setting up libheif-plugin-aomenc:arm64 (1.17.6-1ubuntu4.2) ...
Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
Processing triggers for man-db (2.12.0-4build2) ...
Processing triggers for sgml-base (1.31) ...
Setting up libfontconfig1:arm64 (2.15.0-1.1ubuntu2) ...
Setting up libgd3:arm64 (2.3.3-9ubuntu5) ...
Setting up libc-devtools (2.39-0ubuntu8.7) ...
Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
Scanning processes...                                                 
Scanning candidates...                                                
Scanning processor microcode...                                       
Scanning linux images...                                              

Pending kernel upgrade!
Running kernel version:
  6.8.0-1047-raspi
Diagnostics:
  The currently running kernel version is not the expected kernel
version 6.8.0-1056-raspi.

Restarting the system to load the new kernel will not be handled
automatically, so you should consider rebooting.

The processor microcode seems to be up-to-date.

Restarting services...

Service restarts being deferred:
 /etc/needrestart/restart.d/dbus.service
 systemctl restart getty@tty1.service
 systemctl restart serial-getty@ttyS0.service
 systemctl restart systemd-logind.service
 systemctl restart unattended-upgrades.service
 systemctl restart wpa_supplicant.service

No containers need to be restarted.

User sessions running outdated binaries:
 sona @ session #3: node[2423,2925], sh[2419]
 sona @ session #6: sshd[2812]
 sona @ user manager service: systemd[2200]

No VM guests are running outdated hypervisor (qemu) binaries on this
 host.
```

</details>

# libcamera dependencies 


```bash
sudo apt install -y libboost-dev libgnutls28-dev openssl libtiff5-dev pybind11-dev
```


<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ sudo apt install -y libboost-dev libgnutls28-dev openssl libtiff5-dev pybind11-dev
[sudo] password for sona: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
openssl is already the newest version (3.0.13-0ubuntu3.9).
openssl set to manually installed.
The following packages were automatically installed and are no longer required:
  linux-image-6.8.0-1047-raspi linux-modules-6.8.0-1047-raspi
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libboost1.83-dev libdeflate-dev libeigen3-dev libevent-2.1-7t64
  libexpat1-dev libgmp-dev libgmpxx4ldbl libgnutls-dane0t64
  libgnutls-openssl27t64 libidn2-dev libjbig-dev libjpeg-dev
  libjpeg-turbo8-dev libjpeg8-dev liblerc-dev liblzma-dev
  libp11-kit-dev libpkgconf3 libpython3-dev libpython3.12-dev
  libsharpyuv-dev libstdc++-13-dev libtasn1-6-dev libtasn1-doc
  libtiff-dev libtiffxx6 libunbound8 libwebp-dev libwebpdecoder3
  libwebpdemux2 libwebpmux3 libzstd-dev nettle-dev pkg-config
  pkgconf pkgconf-bin zlib1g-dev
Suggested packages:
  libboost-doc libboost1.83-doc libboost-atomic1.83-dev
  libboost-chrono1.83-dev libboost-container1.83-dev
  libboost-context1.83-dev libboost-contract1.83-dev
  libboost-coroutine1.83-dev libboost-date-time1.83-dev
  libboost-exception1.83-dev libboost-fiber1.83-dev
  libboost-filesystem1.83-dev libboost-graph-parallel1.83-dev
  libboost-graph1.83-dev libboost-iostreams1.83-dev
  libboost-json1.83-dev libboost-locale1.83-dev libboost-log1.83-dev
  libboost-math1.83-dev libboost-mpi-python1.83-dev
  libboost-mpi1.83-dev libboost-nowide1.83-dev
  libboost-numpy1.83-dev libboost-program-options1.83-dev
  libboost-python1.83-dev libboost-random1.83-dev
  libboost-regex1.83-dev libboost-serialization1.83-dev
  libboost-stacktrace1.83-dev libboost-system1.83-dev
  libboost-test1.83-dev libboost-thread1.83-dev
  libboost-timer1.83-dev libboost-type-erasure1.83-dev
  libboost-url1.83-dev libboost-wave1.83-dev libboost1.83-tools-dev
  libmpfrc++-dev libntl-dev libeigen3-doc gmp-doc libgmp10-doc
  libmpfr-dev dns-root-data gnutls-bin gnutls-doc liblzma-doc
  p11-kit-doc libstdc++-13-doc pybind11-doc
The following NEW packages will be installed:
  libboost-dev libboost1.83-dev libdeflate-dev libeigen3-dev
  libevent-2.1-7t64 libexpat1-dev libgmp-dev libgmpxx4ldbl
  libgnutls-dane0t64 libgnutls-openssl27t64 libgnutls28-dev
  libidn2-dev libjbig-dev libjpeg-dev libjpeg-turbo8-dev
  libjpeg8-dev liblerc-dev liblzma-dev libp11-kit-dev libpkgconf3
  libpython3-dev libpython3.12-dev libsharpyuv-dev libstdc++-13-dev
  libtasn1-6-dev libtasn1-doc libtiff-dev libtiff5-dev libtiffxx6
  libunbound8 libwebp-dev libwebpdecoder3 libwebpdemux2 libwebpmux3
  libzstd-dev nettle-dev pkg-config pkgconf pkgconf-bin pybind11-dev
  zlib1g-dev
0 upgraded, 41 newly installed, 0 to remove and 0 not upgraded.
Need to get 26.7 MB of archives.
After this operation, 245 MB of additional disk space will be used.
Get:1 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libstdc++-13-dev arm64 13.3.0-6ubuntu2~24.04.1 [2397 kB]
Get:2 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libboost1.83-dev arm64 1.83.0-2.1ubuntu3.2 [10.7 MB]
Get:3 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libboost-dev arm64 1.83.0.1ubuntu2 [4308 B]
Get:4 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libdeflate-dev arm64 1.19-1build1.1 [51.2 kB]
Get:5 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libevent-2.1-7t64 arm64 2.1.12-stable-9ubuntu2 [140 kB]
Get:6 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libexpat1-dev arm64 2.6.1-2ubuntu0.4 [128 kB]
Get:7 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgmpxx4ldbl arm64 2:6.3.0+dfsg-2ubuntu6.1 [10.1 kB]
Get:8 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgmp-dev arm64 2:6.3.0+dfsg-2ubuntu6.1 [334 kB]
Get:9 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libunbound8 arm64 1.19.2-1ubuntu3.8 [427 kB]
Get:10 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgnutls-dane0t64 arm64 3.8.3-1.1ubuntu3.6 [23.5 kB]
Get:11 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgnutls-openssl27t64 arm64 3.8.3-1.1ubuntu3.6 [23.5 kB]
Get:12 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libidn2-dev arm64 2.3.7-2build1.1 [120 kB]
Get:13 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libp11-kit-dev arm64 0.25.3-4ubuntu2.1 [22.7 kB]
Get:14 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libtasn1-6-dev arm64 4.19.0-3ubuntu0.24.04.2 [90.9 kB]
Get:15 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 nettle-dev arm64 3.9.1-2.2build1.1 [1171 kB]
Get:16 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgnutls28-dev arm64 3.8.3-1.1ubuntu3.6 [1120 kB]
Get:17 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libjpeg-turbo8-dev arm64 2.1.5-2ubuntu2 [305 kB]
Get:18 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libjpeg8-dev arm64 8c-2ubuntu11 [1484 B]
Get:19 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libjpeg-dev arm64 8c-2ubuntu11 [1482 B]
Get:20 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 liblerc-dev arm64 4.0.0+ds-4ubuntu2 [168 kB]
Get:21 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libpkgconf3 arm64 1.8.1-2build1 [31.2 kB]
Get:22 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 zlib1g-dev arm64 1:1.3.dfsg-3.1ubuntu2.1 [894 kB]
Get:23 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libpython3.12-dev arm64 3.12.3-1ubuntu0.13 [5538 kB]
Get:24 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libpython3-dev arm64 3.12.3-0ubuntu2.1 [10.4 kB]
Get:25 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libsharpyuv-dev arm64 1.3.2-0.4build3 [15.1 kB]
Get:26 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libjbig-dev arm64 2.1-6.1ubuntu2 [27.5 kB]
Get:27 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 liblzma-dev arm64 5.6.1+really5.4.5-1ubuntu0.2 [178 kB]
Get:28 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libzstd-dev arm64 1.5.5+dfsg2-2build1.1 [344 kB]
Get:29 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libwebpdemux2 arm64 1.3.2-0.4build3 [12.3 kB]
Get:30 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libwebpmux3 arm64 1.3.2-0.4build3 [25.0 kB]
Get:31 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libwebpdecoder3 arm64 1.3.2-0.4build3 [88.7 kB]
Get:32 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libwebp-dev arm64 1.3.2-0.4build3 [334 kB]
Get:33 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libtiffxx6 arm64 4.5.1+git230720-4ubuntu2.5 [5646 B]
Get:34 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libtiff-dev arm64 4.5.1+git230720-4ubuntu2.5 [337 kB]
Get:35 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libtiff5-dev arm64 4.5.1+git230720-4ubuntu2.5 [2160 B]
Get:36 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 pkgconf-bin arm64 1.8.1-2build1 [20.5 kB]
Get:37 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 pkgconf arm64 1.8.1-2build1 [16.8 kB]
Get:38 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 pkg-config arm64 1.8.1-2build1 [7264 B]
Get:39 http://ports.ubuntu.com/ubuntu-ports noble/universe arm64 pybind11-dev all 2.11.1-2 [159 kB]
Get:40 http://ports.ubuntu.com/ubuntu-ports noble-updates/universe arm64 libeigen3-dev all 3.4.0-4build0.1 [1057 kB]
Get:41 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libtasn1-doc all 4.19.0-3ubuntu0.24.04.2 [318 kB]
Fetched 26.7 MB in 3s (8692 kB/s)       
Extracting templates from packages: 100%
Selecting previously unselected package libstdc++-13-dev:arm64.
(Reading database ... 75651 files and directories currently installed.)
Preparing to unpack .../00-libstdc++-13-dev_13.3.0-6ubuntu2~24.04.1_arm64.deb ...
Unpacking libstdc++-13-dev:arm64 (13.3.0-6ubuntu2~24.04.1) ...
Selecting previously unselected package libboost1.83-dev:arm64.
Preparing to unpack .../01-libboost1.83-dev_1.83.0-2.1ubuntu3.2_arm64.deb ...
Unpacking libboost1.83-dev:arm64 (1.83.0-2.1ubuntu3.2) ...
Selecting previously unselected package libboost-dev:arm64.
Preparing to unpack .../02-libboost-dev_1.83.0.1ubuntu2_arm64.deb ...
Unpacking libboost-dev:arm64 (1.83.0.1ubuntu2) ...
Selecting previously unselected package libdeflate-dev:arm64.
Preparing to unpack .../03-libdeflate-dev_1.19-1build1.1_arm64.deb ...
Unpacking libdeflate-dev:arm64 (1.19-1build1.1) ...
Selecting previously unselected package libevent-2.1-7t64:arm64.
Preparing to unpack .../04-libevent-2.1-7t64_2.1.12-stable-9ubuntu2_arm64.deb ...
Unpacking libevent-2.1-7t64:arm64 (2.1.12-stable-9ubuntu2) ...
Selecting previously unselected package libexpat1-dev:arm64.
Preparing to unpack .../05-libexpat1-dev_2.6.1-2ubuntu0.4_arm64.deb ...
Unpacking libexpat1-dev:arm64 (2.6.1-2ubuntu0.4) ...
Selecting previously unselected package libgmpxx4ldbl:arm64.
Preparing to unpack .../06-libgmpxx4ldbl_2%3a6.3.0+dfsg-2ubuntu6.1_arm64.deb ...
Unpacking libgmpxx4ldbl:arm64 (2:6.3.0+dfsg-2ubuntu6.1) ...
Selecting previously unselected package libgmp-dev:arm64.
Preparing to unpack .../07-libgmp-dev_2%3a6.3.0+dfsg-2ubuntu6.1_arm64.deb ...
Unpacking libgmp-dev:arm64 (2:6.3.0+dfsg-2ubuntu6.1) ...
Selecting previously unselected package libunbound8:arm64.
Preparing to unpack .../08-libunbound8_1.19.2-1ubuntu3.8_arm64.deb ...
Unpacking libunbound8:arm64 (1.19.2-1ubuntu3.8) ...
Selecting previously unselected package libgnutls-dane0t64:arm64.
Preparing to unpack .../09-libgnutls-dane0t64_3.8.3-1.1ubuntu3.6_arm64.deb ...
Unpacking libgnutls-dane0t64:arm64 (3.8.3-1.1ubuntu3.6) ...
Selecting previously unselected package libgnutls-openssl27t64:arm64.
Preparing to unpack .../10-libgnutls-openssl27t64_3.8.3-1.1ubuntu3.6_arm64.deb ...
Unpacking libgnutls-openssl27t64:arm64 (3.8.3-1.1ubuntu3.6) ...
Selecting previously unselected package libidn2-dev:arm64.
Preparing to unpack .../11-libidn2-dev_2.3.7-2build1.1_arm64.deb ...
Unpacking libidn2-dev:arm64 (2.3.7-2build1.1) ...
Selecting previously unselected package libp11-kit-dev:arm64.
Preparing to unpack .../12-libp11-kit-dev_0.25.3-4ubuntu2.1_arm64.deb ...
Unpacking libp11-kit-dev:arm64 (0.25.3-4ubuntu2.1) ...
Selecting previously unselected package libtasn1-6-dev:arm64.
Preparing to unpack .../13-libtasn1-6-dev_4.19.0-3ubuntu0.24.04.2_arm64.deb ...
Unpacking libtasn1-6-dev:arm64 (4.19.0-3ubuntu0.24.04.2) ...
Selecting previously unselected package nettle-dev:arm64.
Preparing to unpack .../14-nettle-dev_3.9.1-2.2build1.1_arm64.deb ...
Unpacking nettle-dev:arm64 (3.9.1-2.2build1.1) ...
Selecting previously unselected package libgnutls28-dev:arm64.
Preparing to unpack .../15-libgnutls28-dev_3.8.3-1.1ubuntu3.6_arm64.deb ...
Unpacking libgnutls28-dev:arm64 (3.8.3-1.1ubuntu3.6) ...
Selecting previously unselected package libjpeg-turbo8-dev:arm64.
Preparing to unpack .../16-libjpeg-turbo8-dev_2.1.5-2ubuntu2_arm64.deb ...
Unpacking libjpeg-turbo8-dev:arm64 (2.1.5-2ubuntu2) ...
Selecting previously unselected package libjpeg8-dev:arm64.
Preparing to unpack .../17-libjpeg8-dev_8c-2ubuntu11_arm64.deb ...
Unpacking libjpeg8-dev:arm64 (8c-2ubuntu11) ...
Selecting previously unselected package libjpeg-dev:arm64.
Preparing to unpack .../18-libjpeg-dev_8c-2ubuntu11_arm64.deb ...
Unpacking libjpeg-dev:arm64 (8c-2ubuntu11) ...
Selecting previously unselected package liblerc-dev:arm64.
Preparing to unpack .../19-liblerc-dev_4.0.0+ds-4ubuntu2_arm64.deb ...
Unpacking liblerc-dev:arm64 (4.0.0+ds-4ubuntu2) ...
Selecting previously unselected package libpkgconf3:arm64.
Preparing to unpack .../20-libpkgconf3_1.8.1-2build1_arm64.deb ...
Unpacking libpkgconf3:arm64 (1.8.1-2build1) ...
Selecting previously unselected package zlib1g-dev:arm64.
Preparing to unpack .../21-zlib1g-dev_1%3a1.3.dfsg-3.1ubuntu2.1_arm64.deb ...
Unpacking zlib1g-dev:arm64 (1:1.3.dfsg-3.1ubuntu2.1) ...
Selecting previously unselected package libpython3.12-dev:arm64.
Preparing to unpack .../22-libpython3.12-dev_3.12.3-1ubuntu0.13_arm64.deb ...
Unpacking libpython3.12-dev:arm64 (3.12.3-1ubuntu0.13) ...
Selecting previously unselected package libpython3-dev:arm64.
Preparing to unpack .../23-libpython3-dev_3.12.3-0ubuntu2.1_arm64.deb ...
Unpacking libpython3-dev:arm64 (3.12.3-0ubuntu2.1) ...
Selecting previously unselected package libsharpyuv-dev:arm64.
Preparing to unpack .../24-libsharpyuv-dev_1.3.2-0.4build3_arm64.deb ...
Unpacking libsharpyuv-dev:arm64 (1.3.2-0.4build3) ...
Selecting previously unselected package libjbig-dev:arm64.
Preparing to unpack .../25-libjbig-dev_2.1-6.1ubuntu2_arm64.deb ...
Unpacking libjbig-dev:arm64 (2.1-6.1ubuntu2) ...
Selecting previously unselected package liblzma-dev:arm64.
Preparing to unpack .../26-liblzma-dev_5.6.1+really5.4.5-1ubuntu0.2_arm64.deb ...
Unpacking liblzma-dev:arm64 (5.6.1+really5.4.5-1ubuntu0.2) ...
Selecting previously unselected package libzstd-dev:arm64.
Preparing to unpack .../27-libzstd-dev_1.5.5+dfsg2-2build1.1_arm64.deb ...
Unpacking libzstd-dev:arm64 (1.5.5+dfsg2-2build1.1) ...
Selecting previously unselected package libwebpdemux2:arm64.
Preparing to unpack .../28-libwebpdemux2_1.3.2-0.4build3_arm64.deb ...
Unpacking libwebpdemux2:arm64 (1.3.2-0.4build3) ...
Selecting previously unselected package libwebpmux3:arm64.
Preparing to unpack .../29-libwebpmux3_1.3.2-0.4build3_arm64.deb ...
Unpacking libwebpmux3:arm64 (1.3.2-0.4build3) ...
Selecting previously unselected package libwebpdecoder3:arm64.
Preparing to unpack .../30-libwebpdecoder3_1.3.2-0.4build3_arm64.deb ...
Unpacking libwebpdecoder3:arm64 (1.3.2-0.4build3) ...
Selecting previously unselected package libwebp-dev:arm64.
Preparing to unpack .../31-libwebp-dev_1.3.2-0.4build3_arm64.deb ...
Unpacking libwebp-dev:arm64 (1.3.2-0.4build3) ...
Selecting previously unselected package libtiffxx6:arm64.
Preparing to unpack .../32-libtiffxx6_4.5.1+git230720-4ubuntu2.5_arm64.deb ...
Unpacking libtiffxx6:arm64 (4.5.1+git230720-4ubuntu2.5) ...
Selecting previously unselected package libtiff-dev:arm64.
Preparing to unpack .../33-libtiff-dev_4.5.1+git230720-4ubuntu2.5_arm64.deb ...
Unpacking libtiff-dev:arm64 (4.5.1+git230720-4ubuntu2.5) ...
Selecting previously unselected package libtiff5-dev:arm64.
Preparing to unpack .../34-libtiff5-dev_4.5.1+git230720-4ubuntu2.5_arm64.deb ...
Unpacking libtiff5-dev:arm64 (4.5.1+git230720-4ubuntu2.5) ...
Selecting previously unselected package pkgconf-bin.
Preparing to unpack .../35-pkgconf-bin_1.8.1-2build1_arm64.deb ...
Unpacking pkgconf-bin (1.8.1-2build1) ...
Selecting previously unselected package pkgconf:arm64.
Preparing to unpack .../36-pkgconf_1.8.1-2build1_arm64.deb ...
Unpacking pkgconf:arm64 (1.8.1-2build1) ...
Selecting previously unselected package pkg-config:arm64.
Preparing to unpack .../37-pkg-config_1.8.1-2build1_arm64.deb ...
Unpacking pkg-config:arm64 (1.8.1-2build1) ...
Selecting previously unselected package pybind11-dev.
Preparing to unpack .../38-pybind11-dev_2.11.1-2_all.deb ...
Unpacking pybind11-dev (2.11.1-2) ...
Selecting previously unselected package libeigen3-dev.
Preparing to unpack .../39-libeigen3-dev_3.4.0-4build0.1_all.deb ...
Unpacking libeigen3-dev (3.4.0-4build0.1) ...
Selecting previously unselected package libtasn1-doc.
Preparing to unpack .../40-libtasn1-doc_4.19.0-3ubuntu0.24.04.2_all.deb ...
Unpacking libtasn1-doc (4.19.0-3ubuntu0.24.04.2) ...
Setting up libgnutls-openssl27t64:arm64 (3.8.3-1.1ubuntu3.6) ...
Setting up libjpeg-turbo8-dev:arm64 (2.1.5-2ubuntu2) ...
Setting up libzstd-dev:arm64 (1.5.5+dfsg2-2build1.1) ...
Setting up libwebpdemux2:arm64 (1.3.2-0.4build3) ...
Setting up libtasn1-doc (4.19.0-3ubuntu0.24.04.2) ...
Setting up libjbig-dev:arm64 (2.1-6.1ubuntu2) ...
Setting up libwebpdecoder3:arm64 (1.3.2-0.4build3) ...
Setting up libevent-2.1-7t64:arm64 (2.1.12-stable-9ubuntu2) ...
Setting up libunbound8:arm64 (1.19.2-1ubuntu3.8) ...
Setting up libpkgconf3:arm64 (1.8.1-2build1) ...
Setting up libgmpxx4ldbl:arm64 (2:6.3.0+dfsg-2ubuntu6.1) ...
Setting up libexpat1-dev:arm64 (2.6.1-2ubuntu0.4) ...
Setting up libgnutls-dane0t64:arm64 (3.8.3-1.1ubuntu3.6) ...
Setting up pkgconf-bin (1.8.1-2build1) ...
Setting up liblerc-dev:arm64 (4.0.0+ds-4ubuntu2) ...
Setting up libidn2-dev:arm64 (2.3.7-2build1.1) ...
Setting up liblzma-dev:arm64 (5.6.1+really5.4.5-1ubuntu0.2) ...
Setting up zlib1g-dev:arm64 (1:1.3.dfsg-3.1ubuntu2.1) ...
Setting up libjpeg8-dev:arm64 (8c-2ubuntu11) ...
Setting up libsharpyuv-dev:arm64 (1.3.2-0.4build3) ...
Setting up libtasn1-6-dev:arm64 (4.19.0-3ubuntu0.24.04.2) ...
Setting up libwebpmux3:arm64 (1.3.2-0.4build3) ...
Setting up libtiffxx6:arm64 (4.5.1+git230720-4ubuntu2.5) ...
Setting up libdeflate-dev:arm64 (1.19-1build1.1) ...
Setting up libp11-kit-dev:arm64 (0.25.3-4ubuntu2.1) ...
Setting up libstdc++-13-dev:arm64 (13.3.0-6ubuntu2~24.04.1) ...
Setting up libboost1.83-dev:arm64 (1.83.0-2.1ubuntu3.2) ...
Setting up libgmp-dev:arm64 (2:6.3.0+dfsg-2ubuntu6.1) ...
Setting up nettle-dev:arm64 (3.9.1-2.2build1.1) ...
Setting up libjpeg-dev:arm64 (8c-2ubuntu11) ...
Setting up libpython3.12-dev:arm64 (3.12.3-1ubuntu0.13) ...
Setting up pkgconf:arm64 (1.8.1-2build1) ...
Setting up libwebp-dev:arm64 (1.3.2-0.4build3) ...
Setting up libtiff-dev:arm64 (4.5.1+git230720-4ubuntu2.5) ...
Setting up libeigen3-dev (3.4.0-4build0.1) ...
Setting up pkg-config:arm64 (1.8.1-2build1) ...
Setting up libboost-dev:arm64 (1.83.0.1ubuntu2) ...
Setting up libgnutls28-dev:arm64 (3.8.3-1.1ubuntu3.6) ...
Setting up libpython3-dev:arm64 (3.12.3-0ubuntu2.1) ...
Setting up libtiff5-dev:arm64 (4.5.1+git230720-4ubuntu2.5) ...
Setting up pybind11-dev (2.11.1-2) ...
Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
Processing triggers for man-db (2.12.0-4build2) ...
Processing triggers for install-info (7.1-3build2) ...
Scanning processes...                                                 
Scanning processor microcode...                                       
Scanning linux images...                                              

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this
 host.
```

</details>


# Libcamera Dependencies 2

```bash
sudo apt install -y python3-yaml python3-ply libglib2.0-dev libgstreamer-plugins-base1.0-dev
```


<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ sudo apt install -y python3-yaml python3-ply libglib2.0-dev libgstreamer-plugins-base1.0-dev
[sudo] password for sona: 
Sorry, try again.
[sudo] password for sona: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3-yaml is already the newest version (6.0.1-2build2).
python3-yaml set to manually installed.
The following packages were automatically installed and are no longer required:
  linux-image-6.8.0-1047-raspi linux-modules-6.8.0-1047-raspi
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0
  gir1.2-gudev-1.0 gstreamer1.0-gl gstreamer1.0-plugins-base
  libblkid-dev libcairo2 libcdparanoia0 libdrm-amdgpu1
  libdrm-dev libdrm-etnaviv1 libdrm-freedreno1 libdrm-nouveau2
  libdrm-radeon1 libdrm-tegra0 libdw-dev libegl-dev
  libegl-mesa0 libegl1 libelf-dev libffi-dev libgbm-dev
  libgbm1 libgirepository-2.0-0 libgl-dev libgl1
  libgl1-mesa-dri libgles-dev libgles1 libgles2
  libglib2.0-dev-bin libglvnd0 libglx-dev libglx-mesa0 libglx0
  libgraphene-1.0-0 libgstreamer-gl1.0-0
  libgstreamer-plugins-base1.0-0 libgstreamer1.0-dev
  libgudev-1.0-dev libllvm20 libmount-dev libogg0 libopus0
  liborc-0.4-0t64 liborc-0.4-dev liborc-0.4-dev-bin
  libpciaccess-dev libpciaccess0 libpcre2-16-0 libpcre2-32-0
  libpcre2-dev libpcre2-posix3 libpixman-1-0
  libpthread-stubs0-dev libselinux1-dev libsepol-dev
  libtheora0 libudev-dev libunwind-dev libvisual-0.4-0
  libvorbis0a libvorbisenc2 libvulkan1 libwayland-bin
  libwayland-client0 libwayland-cursor0 libwayland-dev
  libwayland-egl1 libwayland-server0 libx11-dev libx11-xcb-dev
  libx11-xcb1 libxau-dev libxcb-dri3-0 libxcb-glx0
  libxcb-present0 libxcb-randr0 libxcb-render0 libxcb-shm0
  libxcb-sync1 libxcb-xfixes0 libxcb1-dev libxdmcp-dev
  libxrender1 libxshmfence1 libxxf86vm1 mesa-libgallium
  mesa-vulkan-drivers uuid-dev x11proto-dev xorg-sgml-doctools
  xtrans-dev
Suggested packages:
  gvfs gir1.2-glib-2.0-dev libglib2.0-doc libgdk-pixbuf2.0-bin
  libxml2-utils libvisual-0.4-plugins gstreamer1.0-doc
  opus-tools liborc-0.4-doc libwayland-doc libx11-doc
  libxcb-doc python-ply-doc
The following NEW packages will be installed:
  gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0
  gir1.2-gudev-1.0 gstreamer1.0-gl gstreamer1.0-plugins-base
  libblkid-dev libcairo2 libcdparanoia0 libdrm-amdgpu1
  libdrm-dev libdrm-etnaviv1 libdrm-freedreno1 libdrm-nouveau2
  libdrm-radeon1 libdrm-tegra0 libdw-dev libegl-dev
  libegl-mesa0 libegl1 libelf-dev libffi-dev libgbm-dev
  libgbm1 libgirepository-2.0-0 libgl-dev libgl1
  libgl1-mesa-dri libgles-dev libgles1 libgles2 libglib2.0-dev
  libglib2.0-dev-bin libglvnd0 libglx-dev libglx-mesa0 libglx0
  libgraphene-1.0-0 libgstreamer-gl1.0-0
  libgstreamer-plugins-base1.0-0
  libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
  libgudev-1.0-dev libllvm20 libmount-dev libogg0 libopus0
  liborc-0.4-0t64 liborc-0.4-dev liborc-0.4-dev-bin
  libpciaccess-dev libpciaccess0 libpcre2-16-0 libpcre2-32-0
  libpcre2-dev libpcre2-posix3 libpixman-1-0
  libpthread-stubs0-dev libselinux1-dev libsepol-dev
  libtheora0 libudev-dev libunwind-dev libvisual-0.4-0
  libvorbis0a libvorbisenc2 libvulkan1 libwayland-bin
  libwayland-client0 libwayland-cursor0 libwayland-dev
  libwayland-egl1 libwayland-server0 libx11-dev libx11-xcb-dev
  libx11-xcb1 libxau-dev libxcb-dri3-0 libxcb-glx0
  libxcb-present0 libxcb-randr0 libxcb-render0 libxcb-shm0
  libxcb-sync1 libxcb-xfixes0 libxcb1-dev libxdmcp-dev
  libxrender1 libxshmfence1 libxxf86vm1 mesa-libgallium
  mesa-vulkan-drivers python3-ply uuid-dev x11proto-dev
  xorg-sgml-doctools xtrans-dev
0 upgraded, 96 newly installed, 0 to remove and 0 not upgraded.
Need to get 75.5 MB of archives.
After this operation, 376 MB of additional disk space will be used.
Get:1 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 gir1.2-gstreamer-1.0 arm64 1.24.2-1ubuntu0.1 [88.4 kB]
Get:2 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libglvnd0 arm64 1.7.0-1build1 [60.6 kB]
Get:3 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libdrm-amdgpu1 arm64 2.4.125-1ubuntu0.1~24.04.1 [21.9 kB]
Get:4 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libllvm20 arm64 1:20.1.2-0ubuntu1~24.04.2 [29.3 MB]
Get:5 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libx11-xcb1 arm64 2:1.8.7-1build1 [7870 B]
Get:6 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxcb-dri3-0 arm64 1.15-1ubuntu2 [7196 B]
Get:7 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxcb-present0 arm64 1.15-1ubuntu2 [5866 B]
Get:8 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxcb-randr0 arm64 1.15-1ubuntu2 [18.4 kB]
Get:9 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxcb-sync1 arm64 1.15-1ubuntu2 [9682 B]
Get:10 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxcb-xfixes0 arm64 1.15-1ubuntu2 [10.6 kB]
Get:11 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxshmfence1 arm64 1.3-1build5 [4938 B]
Get:12 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 mesa-libgallium arm64 25.2.8-0ubuntu0.24.04.1 [12.1 MB]
Get:13 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgbm1 arm64 25.2.8-0ubuntu0.24.04.1 [35.0 kB]
Get:14 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libwayland-client0 arm64 1.22.0-2.1build1 [25.9 kB]
Get:15 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxcb-shm0 arm64 1.15-1ubuntu2 [5876 B]
Get:16 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libegl-mesa0 arm64 25.2.8-0ubuntu0.24.04.1 [116 kB]
Get:17 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libegl1 arm64 1.7.0-1build1 [29.5 kB]
Get:18 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxcb-glx0 arm64 1.15-1ubuntu2 [25.5 kB]
Get:19 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxxf86vm1 arm64 1:1.1.4-1build4 [9130 B]
Get:20 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libvulkan1 arm64 1.3.275.0-1build1 [150 kB]
Get:21 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgl1-mesa-dri arm64 25.2.8-0ubuntu0.24.04.1 [36.9 kB]
Get:22 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libglx-mesa0 arm64 25.2.8-0ubuntu0.24.04.1 [111 kB]
Get:23 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libglx0 arm64 1.7.0-1build1 [33.2 kB]
Get:24 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libgl1 arm64 1.7.0-1build1 [106 kB]
Get:25 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 liborc-0.4-0t64 arm64 1:0.4.38-1ubuntu0.1 [205 kB]
Get:26 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgstreamer-plugins-base1.0-0 arm64 1.24.2-1ubuntu0.4 [829 kB]
Get:27 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libwayland-cursor0 arm64 1.22.0-2.1build1 [10.3 kB]
Get:28 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libwayland-egl1 arm64 1.22.0-2.1build1 [5622 B]
Get:29 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgstreamer-gl1.0-0 arm64 1.24.2-1ubuntu0.4 [209 kB]
Get:30 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 gir1.2-gst-plugins-base-1.0 arm64 1.24.2-1ubuntu0.4 [115 kB]
Get:31 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 gir1.2-gudev-1.0 arm64 1:238-5ubuntu1 [3812 B]
Get:32 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libgraphene-1.0-0 arm64 1.10.8-3build2 [47.0 kB]
Get:33 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 gstreamer1.0-gl arm64 1.24.2-1ubuntu0.4 [114 kB]
Get:34 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libcdparanoia0 arm64 3.10.2+debian-14build3 [46.9 kB]
Get:35 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libogg0 arm64 1.3.5-3build1 [22.6 kB]
Get:36 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libopus0 arm64 1.4-1build1 [198 kB]
Get:37 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libpixman-1-0 arm64 0.42.2-1build1 [204 kB]
Get:38 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxcb-render0 arm64 1.15-1ubuntu2 [16.6 kB]
Get:39 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxrender1 arm64 1:0.9.10-1.1build1 [18.8 kB]
Get:40 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libcairo2 arm64 1.18.0-3build1 [555 kB]
Get:41 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libtheora0 arm64 1.1.1+dfsg.1-16.1build3 [224 kB]
Get:42 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libvisual-0.4-0 arm64 0.4.2-2build1 [110 kB]
Get:43 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libvorbis0a arm64 1.3.7-1build3 [94.0 kB]
Get:44 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libvorbisenc2 arm64 1.3.7-1build3 [80.0 kB]
Get:45 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 gstreamer1.0-plugins-base arm64 1.24.2-1ubuntu0.4 [691 kB]
Get:46 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libdrm-radeon1 arm64 2.4.125-1ubuntu0.1~24.04.1 [20.9 kB]
Get:47 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libdrm-nouveau2 arm64 2.4.125-1ubuntu0.1~24.04.1 [17.8 kB]
Get:48 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libdrm-freedreno1 arm64 2.4.125-1ubuntu0.1~24.04.1 [20.2 kB]
Get:49 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libdrm-tegra0 arm64 2.4.125-1ubuntu0.1~24.04.1 [9622 B]
Get:50 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libdrm-etnaviv1 arm64 2.4.125-1ubuntu0.1~24.04.1 [12.5 kB]
Get:51 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libpciaccess0 arm64 0.17-3ubuntu0.24.04.2 [19.1 kB]
Get:52 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libpciaccess-dev arm64 0.17-3ubuntu0.24.04.2 [23.5 kB]
Get:53 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libdrm-dev arm64 2.4.125-1ubuntu0.1~24.04.1 [350 kB]
Get:54 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libelf-dev arm64 0.190-1.1ubuntu0.1 [72.2 kB]
Get:55 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libdw-dev arm64 0.190-1.1ubuntu0.1 [341 kB]
Get:56 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 xorg-sgml-doctools all 1:1.11-1.1 [10.9 kB]
Get:57 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 x11proto-dev all 2023.2-1 [602 kB]
Get:58 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxau-dev arm64 1:1.0.9-1build6 [10.0 kB]
Get:59 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxdmcp-dev arm64 1:1.1.3-0ubuntu6 [26.3 kB]
Get:60 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 xtrans-dev all 1.4.0-1 [68.9 kB]
Get:61 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libpthread-stubs0-dev arm64 0.4-1build3 [4734 B]
Get:62 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxcb1-dev arm64 1.15-1ubuntu2 [91.2 kB]
Get:63 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libx11-dev arm64 2:1.8.7-1build1 [742 kB]
Get:64 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libglx-dev arm64 1.7.0-1build1 [14.2 kB]
Get:65 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libgl-dev arm64 1.7.0-1build1 [102 kB]
Get:66 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libegl-dev arm64 1.7.0-1build1 [18.2 kB]
Get:67 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgbm-dev arm64 25.2.8-0ubuntu0.24.04.1 [12.7 kB]
Get:68 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgirepository-2.0-0 arm64 2.80.0-6ubuntu3.8 [71.5 kB]
Get:69 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libgles1 arm64 1.7.0-1build1 [11.6 kB]
Get:70 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libgles2 arm64 1.7.0-1build1 [17.6 kB]
Get:71 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libgles-dev arm64 1.7.0-1build1 [50.4 kB]
Get:72 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libffi-dev arm64 3.4.6-1build1 [59.5 kB]
Get:73 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libglib2.0-dev-bin arm64 2.80.0-6ubuntu3.8 [138 kB]
Get:74 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 uuid-dev arm64 2.39.3-9ubuntu6.5 [34.8 kB]
Get:75 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libblkid-dev arm64 2.39.3-9ubuntu6.5 [219 kB]
Get:76 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libsepol-dev arm64 3.5-2build1 [395 kB]
Get:77 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libpcre2-16-0 arm64 10.42-4ubuntu2.1 [196 kB]
Get:78 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libpcre2-32-0 arm64 10.42-4ubuntu2.1 [184 kB]
Get:79 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libpcre2-posix3 arm64 10.42-4ubuntu2.1 [6604 B]
Get:80 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libpcre2-dev arm64 10.42-4ubuntu2.1 [680 kB]
Get:81 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libselinux1-dev arm64 3.5-2ubuntu2.1 [172 kB]
Get:82 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libmount-dev arm64 2.39.3-9ubuntu6.5 [14.9 kB]
Get:83 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libglib2.0-dev arm64 2.80.0-6ubuntu3.8 [1964 kB]
Get:84 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libunwind-dev arm64 1.6.2-3build1.1 [1872 kB]
Get:85 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgstreamer1.0-dev arm64 1.24.2-1ubuntu0.1 [524 kB]
Get:86 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 liborc-0.4-dev-bin arm64 1:0.4.38-1ubuntu0.1 [20.9 kB]
Get:87 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 liborc-0.4-dev arm64 1:0.4.38-1ubuntu0.1 [30.2 kB]
Get:88 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libx11-xcb-dev arm64 2:1.8.7-1build1 [9996 B]
Get:89 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libwayland-server0 arm64 1.22.0-2.1build1 [34.6 kB]
Get:90 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libwayland-bin arm64 1.22.0-2.1build1 [20.3 kB]
Get:91 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libwayland-dev arm64 1.22.0-2.1build1 [71.3 kB]
Get:92 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libudev-dev arm64 255.4-1ubuntu8.15 [22.0 kB]
Get:93 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libgudev-1.0-dev arm64 1:238-5ubuntu1 [27.2 kB]
Get:94 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libgstreamer-plugins-base1.0-dev arm64 1.24.2-1ubuntu0.4 [466 kB]
Get:95 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 mesa-vulkan-drivers arm64 25.2.8-0ubuntu0.24.04.1 [19.4 MB]
Get:96 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 python3-ply all 3.11-6 [46.5 kB]
Fetched 75.5 MB in 9s (8792 kB/s)                              
Extracting templates from packages: 100%
Selecting previously unselected package gir1.2-gstreamer-1.0:arm64.
(Reading database ... 95073 files and directories currently installed.)
Preparing to unpack .../00-gir1.2-gstreamer-1.0_1.24.2-1ubuntu0.1_arm64.deb ...
Unpacking gir1.2-gstreamer-1.0:arm64 (1.24.2-1ubuntu0.1) ...
Selecting previously unselected package libglvnd0:arm64.
Preparing to unpack .../01-libglvnd0_1.7.0-1build1_arm64.deb ...
Unpacking libglvnd0:arm64 (1.7.0-1build1) ...
Selecting previously unselected package libdrm-amdgpu1:arm64.
Preparing to unpack .../02-libdrm-amdgpu1_2.4.125-1ubuntu0.1~24.04.1_arm64.deb ...
Unpacking libdrm-amdgpu1:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Selecting previously unselected package libllvm20:arm64.
Preparing to unpack .../03-libllvm20_1%3a20.1.2-0ubuntu1~24.04.2_arm64.deb ...
Unpacking libllvm20:arm64 (1:20.1.2-0ubuntu1~24.04.2) ...
Selecting previously unselected package libx11-xcb1:arm64.
Preparing to unpack .../04-libx11-xcb1_2%3a1.8.7-1build1_arm64.deb ...
Unpacking libx11-xcb1:arm64 (2:1.8.7-1build1) ...
Selecting previously unselected package libxcb-dri3-0:arm64.
Preparing to unpack .../05-libxcb-dri3-0_1.15-1ubuntu2_arm64.deb ...
Unpacking libxcb-dri3-0:arm64 (1.15-1ubuntu2) ...
Selecting previously unselected package libxcb-present0:arm64.
Preparing to unpack .../06-libxcb-present0_1.15-1ubuntu2_arm64.deb ...
Unpacking libxcb-present0:arm64 (1.15-1ubuntu2) ...
Selecting previously unselected package libxcb-randr0:arm64.
Preparing to unpack .../07-libxcb-randr0_1.15-1ubuntu2_arm64.deb ...
Unpacking libxcb-randr0:arm64 (1.15-1ubuntu2) ...
Selecting previously unselected package libxcb-sync1:arm64.
Preparing to unpack .../08-libxcb-sync1_1.15-1ubuntu2_arm64.deb ...
Unpacking libxcb-sync1:arm64 (1.15-1ubuntu2) ...
Selecting previously unselected package libxcb-xfixes0:arm64.
Preparing to unpack .../09-libxcb-xfixes0_1.15-1ubuntu2_arm64.deb ...
Unpacking libxcb-xfixes0:arm64 (1.15-1ubuntu2) ...
Selecting previously unselected package libxshmfence1:arm64.
Preparing to unpack .../10-libxshmfence1_1.3-1build5_arm64.deb ...
Unpacking libxshmfence1:arm64 (1.3-1build5) ...
Selecting previously unselected package mesa-libgallium:arm64.
Preparing to unpack .../11-mesa-libgallium_25.2.8-0ubuntu0.24.04.1_arm64.deb ...
Unpacking mesa-libgallium:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Selecting previously unselected package libgbm1:arm64.
Preparing to unpack .../12-libgbm1_25.2.8-0ubuntu0.24.04.1_arm64.deb ...
Unpacking libgbm1:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Selecting previously unselected package libwayland-client0:arm64.
Preparing to unpack .../13-libwayland-client0_1.22.0-2.1build1_arm64.deb ...
Unpacking libwayland-client0:arm64 (1.22.0-2.1build1) ...
Selecting previously unselected package libxcb-shm0:arm64.
Preparing to unpack .../14-libxcb-shm0_1.15-1ubuntu2_arm64.deb ...
Unpacking libxcb-shm0:arm64 (1.15-1ubuntu2) ...
Selecting previously unselected package libegl-mesa0:arm64.
Preparing to unpack .../15-libegl-mesa0_25.2.8-0ubuntu0.24.04.1_arm64.deb ...
Unpacking libegl-mesa0:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Selecting previously unselected package libegl1:arm64.
Preparing to unpack .../16-libegl1_1.7.0-1build1_arm64.deb ...
Unpacking libegl1:arm64 (1.7.0-1build1) ...
Selecting previously unselected package libxcb-glx0:arm64.
Preparing to unpack .../17-libxcb-glx0_1.15-1ubuntu2_arm64.deb ...
Unpacking libxcb-glx0:arm64 (1.15-1ubuntu2) ...
Selecting previously unselected package libxxf86vm1:arm64.
Preparing to unpack .../18-libxxf86vm1_1%3a1.1.4-1build4_arm64.deb ...
Unpacking libxxf86vm1:arm64 (1:1.1.4-1build4) ...
Selecting previously unselected package libvulkan1:arm64.
Preparing to unpack .../19-libvulkan1_1.3.275.0-1build1_arm64.deb ...
Unpacking libvulkan1:arm64 (1.3.275.0-1build1) ...
Selecting previously unselected package libgl1-mesa-dri:arm64.
Preparing to unpack .../20-libgl1-mesa-dri_25.2.8-0ubuntu0.24.04.1_arm64.deb ...
Unpacking libgl1-mesa-dri:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Selecting previously unselected package libglx-mesa0:arm64.
Preparing to unpack .../21-libglx-mesa0_25.2.8-0ubuntu0.24.04.1_arm64.deb ...
Unpacking libglx-mesa0:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Selecting previously unselected package libglx0:arm64.
Preparing to unpack .../22-libglx0_1.7.0-1build1_arm64.deb ...
Unpacking libglx0:arm64 (1.7.0-1build1) ...
Selecting previously unselected package libgl1:arm64.
Preparing to unpack .../23-libgl1_1.7.0-1build1_arm64.deb ...
Unpacking libgl1:arm64 (1.7.0-1build1) ...
Selecting previously unselected package liborc-0.4-0t64:arm64.
Preparing to unpack .../24-liborc-0.4-0t64_1%3a0.4.38-1ubuntu0.1_arm64.deb ...
Unpacking liborc-0.4-0t64:arm64 (1:0.4.38-1ubuntu0.1) ...
Selecting previously unselected package libgstreamer-plugins-base1.0-0:arm64.
Preparing to unpack .../25-libgstreamer-plugins-base1.0-0_1.24.2-1ubuntu0.4_arm64.deb ...
Unpacking libgstreamer-plugins-base1.0-0:arm64 (1.24.2-1ubuntu0.4) ...
Selecting previously unselected package libwayland-cursor0:arm64.
Preparing to unpack .../26-libwayland-cursor0_1.22.0-2.1build1_arm64.deb ...
Unpacking libwayland-cursor0:arm64 (1.22.0-2.1build1) ...
Selecting previously unselected package libwayland-egl1:arm64.
Preparing to unpack .../27-libwayland-egl1_1.22.0-2.1build1_arm64.deb ...
Unpacking libwayland-egl1:arm64 (1.22.0-2.1build1) ...
Selecting previously unselected package libgstreamer-gl1.0-0:arm64.
Preparing to unpack .../28-libgstreamer-gl1.0-0_1.24.2-1ubuntu0.4_arm64.deb ...
Unpacking libgstreamer-gl1.0-0:arm64 (1.24.2-1ubuntu0.4) ...
Selecting previously unselected package gir1.2-gst-plugins-base-1.0:arm64.
Preparing to unpack .../29-gir1.2-gst-plugins-base-1.0_1.24.2-1ubuntu0.4_arm64.deb ...
Unpacking gir1.2-gst-plugins-base-1.0:arm64 (1.24.2-1ubuntu0.4) ...
Selecting previously unselected package gir1.2-gudev-1.0:arm64.
Preparing to unpack .../30-gir1.2-gudev-1.0_1%3a238-5ubuntu1_arm64.deb ...
Unpacking gir1.2-gudev-1.0:arm64 (1:238-5ubuntu1) ...
Selecting previously unselected package libgraphene-1.0-0:arm64.
Preparing to unpack .../31-libgraphene-1.0-0_1.10.8-3build2_arm64.deb ...
Unpacking libgraphene-1.0-0:arm64 (1.10.8-3build2) ...
Selecting previously unselected package gstreamer1.0-gl:arm64.
Preparing to unpack .../32-gstreamer1.0-gl_1.24.2-1ubuntu0.4_arm64.deb ...
Unpacking gstreamer1.0-gl:arm64 (1.24.2-1ubuntu0.4) ...
Selecting previously unselected package libcdparanoia0:arm64.
Preparing to unpack .../33-libcdparanoia0_3.10.2+debian-14build3_arm64.deb ...
Unpacking libcdparanoia0:arm64 (3.10.2+debian-14build3) ...
Selecting previously unselected package libogg0:arm64.
Preparing to unpack .../34-libogg0_1.3.5-3build1_arm64.deb ...
Unpacking libogg0:arm64 (1.3.5-3build1) ...
Selecting previously unselected package libopus0:arm64.
Preparing to unpack .../35-libopus0_1.4-1build1_arm64.deb ...
Unpacking libopus0:arm64 (1.4-1build1) ...
Selecting previously unselected package libpixman-1-0:arm64.
Preparing to unpack .../36-libpixman-1-0_0.42.2-1build1_arm64.deb ...
Unpacking libpixman-1-0:arm64 (0.42.2-1build1) ...
Selecting previously unselected package libxcb-render0:arm64.
Preparing to unpack .../37-libxcb-render0_1.15-1ubuntu2_arm64.deb ...
Unpacking libxcb-render0:arm64 (1.15-1ubuntu2) ...
Selecting previously unselected package libxrender1:arm64.
Preparing to unpack .../38-libxrender1_1%3a0.9.10-1.1build1_arm64.deb ...
Unpacking libxrender1:arm64 (1:0.9.10-1.1build1) ...
Selecting previously unselected package libcairo2:arm64.
Preparing to unpack .../39-libcairo2_1.18.0-3build1_arm64.deb ...
Unpacking libcairo2:arm64 (1.18.0-3build1) ...
Selecting previously unselected package libtheora0:arm64.
Preparing to unpack .../40-libtheora0_1.1.1+dfsg.1-16.1build3_arm64.deb ...
Unpacking libtheora0:arm64 (1.1.1+dfsg.1-16.1build3) ...
Selecting previously unselected package libvisual-0.4-0:arm64.
Preparing to unpack .../41-libvisual-0.4-0_0.4.2-2build1_arm64.deb ...
Unpacking libvisual-0.4-0:arm64 (0.4.2-2build1) ...
Selecting previously unselected package libvorbis0a:arm64.
Preparing to unpack .../42-libvorbis0a_1.3.7-1build3_arm64.deb ...
Unpacking libvorbis0a:arm64 (1.3.7-1build3) ...
Selecting previously unselected package libvorbisenc2:arm64.
Preparing to unpack .../43-libvorbisenc2_1.3.7-1build3_arm64.deb ...
Unpacking libvorbisenc2:arm64 (1.3.7-1build3) ...
Selecting previously unselected package gstreamer1.0-plugins-base:arm64.
Preparing to unpack .../44-gstreamer1.0-plugins-base_1.24.2-1ubuntu0.4_arm64.deb ...
Unpacking gstreamer1.0-plugins-base:arm64 (1.24.2-1ubuntu0.4) ...
Selecting previously unselected package libdrm-radeon1:arm64.
Preparing to unpack .../45-libdrm-radeon1_2.4.125-1ubuntu0.1~24.04.1_arm64.deb ...
Unpacking libdrm-radeon1:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Selecting previously unselected package libdrm-nouveau2:arm64.
Preparing to unpack .../46-libdrm-nouveau2_2.4.125-1ubuntu0.1~24.04.1_arm64.deb ...
Unpacking libdrm-nouveau2:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Selecting previously unselected package libdrm-freedreno1:arm64.
Preparing to unpack .../47-libdrm-freedreno1_2.4.125-1ubuntu0.1~24.04.1_arm64.deb ...
Unpacking libdrm-freedreno1:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Selecting previously unselected package libdrm-tegra0:arm64.
Preparing to unpack .../48-libdrm-tegra0_2.4.125-1ubuntu0.1~24.04.1_arm64.deb ...
Unpacking libdrm-tegra0:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Selecting previously unselected package libdrm-etnaviv1:arm64.
Preparing to unpack .../49-libdrm-etnaviv1_2.4.125-1ubuntu0.1~24.04.1_arm64.deb ...
Unpacking libdrm-etnaviv1:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Selecting previously unselected package libpciaccess0:arm64.
Preparing to unpack .../50-libpciaccess0_0.17-3ubuntu0.24.04.2_arm64.deb ...
Unpacking libpciaccess0:arm64 (0.17-3ubuntu0.24.04.2) ...
Selecting previously unselected package libpciaccess-dev:arm64.
Preparing to unpack .../51-libpciaccess-dev_0.17-3ubuntu0.24.04.2_arm64.deb ...
Unpacking libpciaccess-dev:arm64 (0.17-3ubuntu0.24.04.2) ...
Selecting previously unselected package libdrm-dev:arm64.
Preparing to unpack .../52-libdrm-dev_2.4.125-1ubuntu0.1~24.04.1_arm64.deb ...
Unpacking libdrm-dev:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Selecting previously unselected package libelf-dev:arm64.
Preparing to unpack .../53-libelf-dev_0.190-1.1ubuntu0.1_arm64.deb ...
Unpacking libelf-dev:arm64 (0.190-1.1ubuntu0.1) ...
Selecting previously unselected package libdw-dev:arm64.
Preparing to unpack .../54-libdw-dev_0.190-1.1ubuntu0.1_arm64.deb ...
Unpacking libdw-dev:arm64 (0.190-1.1ubuntu0.1) ...
Selecting previously unselected package xorg-sgml-doctools.
Preparing to unpack .../55-xorg-sgml-doctools_1%3a1.11-1.1_all.deb ...
Unpacking xorg-sgml-doctools (1:1.11-1.1) ...
Selecting previously unselected package x11proto-dev.
Preparing to unpack .../56-x11proto-dev_2023.2-1_all.deb ...
Unpacking x11proto-dev (2023.2-1) ...
Selecting previously unselected package libxau-dev:arm64.
Preparing to unpack .../57-libxau-dev_1%3a1.0.9-1build6_arm64.deb ...
Unpacking libxau-dev:arm64 (1:1.0.9-1build6) ...
Selecting previously unselected package libxdmcp-dev:arm64.
Preparing to unpack .../58-libxdmcp-dev_1%3a1.1.3-0ubuntu6_arm64.deb ...
Unpacking libxdmcp-dev:arm64 (1:1.1.3-0ubuntu6) ...
Selecting previously unselected package xtrans-dev.
Preparing to unpack .../59-xtrans-dev_1.4.0-1_all.deb ...
Unpacking xtrans-dev (1.4.0-1) ...
Selecting previously unselected package libpthread-stubs0-dev:arm64.
Preparing to unpack .../60-libpthread-stubs0-dev_0.4-1build3_arm64.deb ...
Unpacking libpthread-stubs0-dev:arm64 (0.4-1build3) ...
Selecting previously unselected package libxcb1-dev:arm64.
Preparing to unpack .../61-libxcb1-dev_1.15-1ubuntu2_arm64.deb ...
Unpacking libxcb1-dev:arm64 (1.15-1ubuntu2) ...
Selecting previously unselected package libx11-dev:arm64.
Preparing to unpack .../62-libx11-dev_2%3a1.8.7-1build1_arm64.deb ...
Unpacking libx11-dev:arm64 (2:1.8.7-1build1) ...
Selecting previously unselected package libglx-dev:arm64.
Preparing to unpack .../63-libglx-dev_1.7.0-1build1_arm64.deb ...
Unpacking libglx-dev:arm64 (1.7.0-1build1) ...
Selecting previously unselected package libgl-dev:arm64.
Preparing to unpack .../64-libgl-dev_1.7.0-1build1_arm64.deb ...
Unpacking libgl-dev:arm64 (1.7.0-1build1) ...
Selecting previously unselected package libegl-dev:arm64.
Preparing to unpack .../65-libegl-dev_1.7.0-1build1_arm64.deb ...
Unpacking libegl-dev:arm64 (1.7.0-1build1) ...
Selecting previously unselected package libgbm-dev:arm64.
Preparing to unpack .../66-libgbm-dev_25.2.8-0ubuntu0.24.04.1_arm64.deb ...
Unpacking libgbm-dev:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Selecting previously unselected package libgirepository-2.0-0:arm64.
Preparing to unpack .../67-libgirepository-2.0-0_2.80.0-6ubuntu3.8_arm64.deb ...
Unpacking libgirepository-2.0-0:arm64 (2.80.0-6ubuntu3.8) ...
Selecting previously unselected package libgles1:arm64.
Preparing to unpack .../68-libgles1_1.7.0-1build1_arm64.deb ...
Unpacking libgles1:arm64 (1.7.0-1build1) ...
Selecting previously unselected package libgles2:arm64.
Preparing to unpack .../69-libgles2_1.7.0-1build1_arm64.deb ...
Unpacking libgles2:arm64 (1.7.0-1build1) ...
Selecting previously unselected package libgles-dev:arm64.
Preparing to unpack .../70-libgles-dev_1.7.0-1build1_arm64.deb ...
Unpacking libgles-dev:arm64 (1.7.0-1build1) ...
Selecting previously unselected package libffi-dev:arm64.
Preparing to unpack .../71-libffi-dev_3.4.6-1build1_arm64.deb ...
Unpacking libffi-dev:arm64 (3.4.6-1build1) ...
Selecting previously unselected package libglib2.0-dev-bin.
Preparing to unpack .../72-libglib2.0-dev-bin_2.80.0-6ubuntu3.8_arm64.deb ...
Unpacking libglib2.0-dev-bin (2.80.0-6ubuntu3.8) ...
Selecting previously unselected package uuid-dev:arm64.
Preparing to unpack .../73-uuid-dev_2.39.3-9ubuntu6.5_arm64.deb ...
Unpacking uuid-dev:arm64 (2.39.3-9ubuntu6.5) ...
Selecting previously unselected package libblkid-dev:arm64.
Preparing to unpack .../74-libblkid-dev_2.39.3-9ubuntu6.5_arm64.deb ...
Unpacking libblkid-dev:arm64 (2.39.3-9ubuntu6.5) ...
Selecting previously unselected package libsepol-dev:arm64.
Preparing to unpack .../75-libsepol-dev_3.5-2build1_arm64.deb ...
Unpacking libsepol-dev:arm64 (3.5-2build1) ...
Selecting previously unselected package libpcre2-16-0:arm64.
Preparing to unpack .../76-libpcre2-16-0_10.42-4ubuntu2.1_arm64.deb ...
Unpacking libpcre2-16-0:arm64 (10.42-4ubuntu2.1) ...
Selecting previously unselected package libpcre2-32-0:arm64.
Preparing to unpack .../77-libpcre2-32-0_10.42-4ubuntu2.1_arm64.deb ...
Unpacking libpcre2-32-0:arm64 (10.42-4ubuntu2.1) ...
Selecting previously unselected package libpcre2-posix3:arm64.
Preparing to unpack .../78-libpcre2-posix3_10.42-4ubuntu2.1_arm64.deb ...
Unpacking libpcre2-posix3:arm64 (10.42-4ubuntu2.1) ...
Selecting previously unselected package libpcre2-dev:arm64.
Preparing to unpack .../79-libpcre2-dev_10.42-4ubuntu2.1_arm64.deb ...
Unpacking libpcre2-dev:arm64 (10.42-4ubuntu2.1) ...
Selecting previously unselected package libselinux1-dev:arm64.
Preparing to unpack .../80-libselinux1-dev_3.5-2ubuntu2.1_arm64.deb ...
Unpacking libselinux1-dev:arm64 (3.5-2ubuntu2.1) ...
Selecting previously unselected package libmount-dev:arm64.
Preparing to unpack .../81-libmount-dev_2.39.3-9ubuntu6.5_arm64.deb ...
Unpacking libmount-dev:arm64 (2.39.3-9ubuntu6.5) ...
Selecting previously unselected package libglib2.0-dev:arm64.
Preparing to unpack .../82-libglib2.0-dev_2.80.0-6ubuntu3.8_arm64.deb ...
Unpacking libglib2.0-dev:arm64 (2.80.0-6ubuntu3.8) ...
Selecting previously unselected package libunwind-dev:arm64.
Preparing to unpack .../83-libunwind-dev_1.6.2-3build1.1_arm64.deb ...
Unpacking libunwind-dev:arm64 (1.6.2-3build1.1) ...
Selecting previously unselected package libgstreamer1.0-dev:arm64.
Preparing to unpack .../84-libgstreamer1.0-dev_1.24.2-1ubuntu0.1_arm64.deb ...
Unpacking libgstreamer1.0-dev:arm64 (1.24.2-1ubuntu0.1) ...
Selecting previously unselected package liborc-0.4-dev-bin.
Preparing to unpack .../85-liborc-0.4-dev-bin_1%3a0.4.38-1ubuntu0.1_arm64.deb ...
Unpacking liborc-0.4-dev-bin (1:0.4.38-1ubuntu0.1) ...
Selecting previously unselected package liborc-0.4-dev:arm64.
Preparing to unpack .../86-liborc-0.4-dev_1%3a0.4.38-1ubuntu0.1_arm64.deb ...
Unpacking liborc-0.4-dev:arm64 (1:0.4.38-1ubuntu0.1) ...
Selecting previously unselected package libx11-xcb-dev:arm64.
Preparing to unpack .../87-libx11-xcb-dev_2%3a1.8.7-1build1_arm64.deb ...
Unpacking libx11-xcb-dev:arm64 (2:1.8.7-1build1) ...
Selecting previously unselected package libwayland-server0:arm64.
Preparing to unpack .../88-libwayland-server0_1.22.0-2.1build1_arm64.deb ...
Unpacking libwayland-server0:arm64 (1.22.0-2.1build1) ...
Selecting previously unselected package libwayland-bin.
Preparing to unpack .../89-libwayland-bin_1.22.0-2.1build1_arm64.deb ...
Unpacking libwayland-bin (1.22.0-2.1build1) ...
Selecting previously unselected package libwayland-dev:arm64.
Preparing to unpack .../90-libwayland-dev_1.22.0-2.1build1_arm64.deb ...
Unpacking libwayland-dev:arm64 (1.22.0-2.1build1) ...
Selecting previously unselected package libudev-dev:arm64.
Preparing to unpack .../91-libudev-dev_255.4-1ubuntu8.15_arm64.deb ...
Unpacking libudev-dev:arm64 (255.4-1ubuntu8.15) ...
Selecting previously unselected package libgudev-1.0-dev:arm64.
Preparing to unpack .../92-libgudev-1.0-dev_1%3a238-5ubuntu1_arm64.deb ...
Unpacking libgudev-1.0-dev:arm64 (1:238-5ubuntu1) ...
Selecting previously unselected package libgstreamer-plugins-base1.0-dev.
Preparing to unpack .../93-libgstreamer-plugins-base1.0-dev_1.24.2-1ubuntu0.4_arm64.deb ...
Unpacking libgstreamer-plugins-base1.0-dev (1.24.2-1ubuntu0.4) ...
Selecting previously unselected package mesa-vulkan-drivers:arm64.
Preparing to unpack .../94-mesa-vulkan-drivers_25.2.8-0ubuntu0.24.04.1_arm64.deb ...
Unpacking mesa-vulkan-drivers:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Selecting previously unselected package python3-ply.
Preparing to unpack .../95-python3-ply_3.11-6_all.deb ...
Unpacking python3-ply (3.11-6) ...
Setting up libxcb-dri3-0:arm64 (1.15-1ubuntu2) ...
Setting up libglib2.0-dev-bin (2.80.0-6ubuntu3.8) ...
Setting up libpixman-1-0:arm64 (0.42.2-1build1) ...
Setting up libcdparanoia0:arm64 (3.10.2+debian-14build3) ...
Setting up libwayland-server0:arm64 (1.22.0-2.1build1) ...
Setting up libx11-xcb1:arm64 (2:1.8.7-1build1) ...
Setting up libpciaccess0:arm64 (0.17-3ubuntu0.24.04.2) ...
Setting up gir1.2-gstreamer-1.0:arm64 (1.24.2-1ubuntu0.1) ...
Setting up libdrm-nouveau2:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Setting up libdrm-etnaviv1:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Setting up libpciaccess-dev:arm64 (0.17-3ubuntu0.24.04.2) ...
Setting up libxcb-xfixes0:arm64 (1.15-1ubuntu2) ...
Setting up libogg0:arm64 (1.3.5-3build1) ...
Setting up libunwind-dev:arm64 (1.6.2-3build1.1) ...
Setting up libxrender1:arm64 (1:0.9.10-1.1build1) ...
Setting up libgirepository-2.0-0:arm64 (2.80.0-6ubuntu3.8) ...
Setting up libvisual-0.4-0:arm64 (0.4.2-2build1) ...
Setting up libxcb-render0:arm64 (1.15-1ubuntu2) ...
Setting up libdrm-radeon1:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Setting up libglvnd0:arm64 (1.7.0-1build1) ...
Setting up libxcb-glx0:arm64 (1.15-1ubuntu2) ...
Setting up python3-ply (3.11-6) ...
Setting up libxcb-shm0:arm64 (1.15-1ubuntu2) ...
Setting up libffi-dev:arm64 (3.4.6-1build1) ...
Setting up libpthread-stubs0-dev:arm64 (0.4-1build3) ...
Setting up libcairo2:arm64 (1.18.0-3build1) ...
Setting up libpcre2-16-0:arm64 (10.42-4ubuntu2.1) ...
Setting up libxxf86vm1:arm64 (1:1.1.4-1build4) ...
Setting up liborc-0.4-0t64:arm64 (1:0.4.38-1ubuntu0.1) ...
Setting up libxcb-present0:arm64 (1.15-1ubuntu2) ...
Setting up xtrans-dev (1.4.0-1) ...
Setting up libwayland-bin (1.22.0-2.1build1) ...
Setting up libpcre2-32-0:arm64 (10.42-4ubuntu2.1) ...
Setting up libgles2:arm64 (1.7.0-1build1) ...
Setting up libxcb-sync1:arm64 (1.15-1ubuntu2) ...
Setting up uuid-dev:arm64 (2.39.3-9ubuntu6.5) ...
Setting up libgles1:arm64 (1.7.0-1build1) ...
Setting up libopus0:arm64 (1.4-1build1) ...
Setting up gir1.2-gudev-1.0:arm64 (1:238-5ubuntu1) ...
Setting up libvorbis0a:arm64 (1.3.7-1build3) ...
Setting up libdrm-freedreno1:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Setting up libelf-dev:arm64 (0.190-1.1ubuntu0.1) ...
Setting up libllvm20:arm64 (1:20.1.2-0ubuntu1~24.04.2) ...
Setting up libudev-dev:arm64 (255.4-1ubuntu8.15) ...
Setting up libsepol-dev:arm64 (3.5-2build1) ...
Setting up libdrm-tegra0:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Setting up libvulkan1:arm64 (1.3.275.0-1build1) ...
Setting up libpcre2-posix3:arm64 (10.42-4ubuntu2.1) ...
Setting up libxshmfence1:arm64 (1.3-1build5) ...
Setting up libxcb-randr0:arm64 (1.15-1ubuntu2) ...
Setting up libtheora0:arm64 (1.1.1+dfsg.1-16.1build3) ...
Setting up xorg-sgml-doctools (1:1.11-1.1) ...
Setting up libwayland-egl1:arm64 (1.22.0-2.1build1) ...
Setting up libgraphene-1.0-0:arm64 (1.10.8-3build2) ...
Setting up libvorbisenc2:arm64 (1.3.7-1build3) ...
Setting up libdrm-amdgpu1:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Setting up libwayland-client0:arm64 (1.22.0-2.1build1) ...
Setting up mesa-vulkan-drivers:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Setting up libblkid-dev:arm64 (2.39.3-9ubuntu6.5) ...
Setting up mesa-libgallium:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Setting up libdrm-dev:arm64 (2.4.125-1ubuntu0.1~24.04.1) ...
Setting up libpcre2-dev:arm64 (10.42-4ubuntu2.1) ...
Setting up libgbm1:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Setting up libselinux1-dev:arm64 (3.5-2ubuntu2.1) ...
Setting up libgl1-mesa-dri:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Setting up liborc-0.4-dev-bin (1:0.4.38-1ubuntu0.1) ...
Setting up libgstreamer-plugins-base1.0-0:arm64 (1.24.2-1ubuntu0.4) ...
Setting up libdw-dev:arm64 (0.190-1.1ubuntu0.1) ...
Setting up libgbm-dev:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Setting up libegl-mesa0:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Setting up gstreamer1.0-plugins-base:arm64 (1.24.2-1ubuntu0.4) ...
Setting up libwayland-cursor0:arm64 (1.22.0-2.1build1) ...
Setting up libegl1:arm64 (1.7.0-1build1) ...
Setting up liborc-0.4-dev:arm64 (1:0.4.38-1ubuntu0.1) ...
Setting up libmount-dev:arm64 (2.39.3-9ubuntu6.5) ...
Setting up libglx-mesa0:arm64 (25.2.8-0ubuntu0.24.04.1) ...
Setting up libglx0:arm64 (1.7.0-1build1) ...
Setting up libwayland-dev:arm64 (1.22.0-2.1build1) ...
Setting up libgl1:arm64 (1.7.0-1build1) ...
Setting up libglib2.0-dev:arm64 (2.80.0-6ubuntu3.8) ...
Setting up libgstreamer-gl1.0-0:arm64 (1.24.2-1ubuntu0.4) ...
Setting up gstreamer1.0-gl:arm64 (1.24.2-1ubuntu0.4) ...
Setting up gir1.2-gst-plugins-base-1.0:arm64 (1.24.2-1ubuntu0.4) ...
Processing triggers for man-db (2.12.0-4build2) ...
Processing triggers for libglib2.0-0t64:arm64 (2.80.0-6ubuntu3.8) ...
No schema files found: doing nothing.
Processing triggers for sgml-base (1.31) ...
Processing triggers for install-info (7.1-3build2) ...
Setting up x11proto-dev (2023.2-1) ...
Setting up libxau-dev:arm64 (1:1.0.9-1build6) ...
Setting up libgstreamer1.0-dev:arm64 (1.24.2-1ubuntu0.1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
Setting up libgudev-1.0-dev:arm64 (1:238-5ubuntu1) ...
Setting up libxdmcp-dev:arm64 (1:1.1.3-0ubuntu6) ...
Setting up libxcb1-dev:arm64 (1.15-1ubuntu2) ...
Setting up libx11-dev:arm64 (2:1.8.7-1build1) ...
Setting up libglx-dev:arm64 (1.7.0-1build1) ...
Setting up libgl-dev:arm64 (1.7.0-1build1) ...
Setting up libx11-xcb-dev:arm64 (2:1.8.7-1build1) ...
Setting up libegl-dev:arm64 (1.7.0-1build1) ...
Setting up libgles-dev:arm64 (1.7.0-1build1) ...
Setting up libgstreamer-plugins-base1.0-dev (1.24.2-1ubuntu0.4) ...
Scanning processes...                                           
Scanning processor microcode...                                 
Scanning linux images...                                        

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on
 this host.
```

</details>

# Raspicam Dependencies 1

```bash
sudo apt install -y cmake libboost-program-options-dev libdrm-dev libexif-dev libepoxy-dev libjpeg-dev libtiff5-dev libpng-dev
```

<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ sudo apt install -y cmake libboost-program-options-dev libdrm-dev libexif-dev libepoxy-dev libjpeg-dev libtiff5-dev libpng-dev
[sudo] password for sona: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
cmake is already the newest version (3.28.3-1build7).
libdrm-dev is already the newest version (2.4.125-1ubuntu0.1~24.04.1).
libdrm-dev set to manually installed.
libjpeg-dev is already the newest version (8c-2ubuntu11).
libjpeg-dev set to manually installed.
libtiff5-dev is already the newest version (4.5.1+git230720-4ubuntu2.5).
The following packages were automatically installed and are no longer required:
  linux-image-6.8.0-1047-raspi linux-modules-6.8.0-1047-raspi
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libboost-program-options1.83-dev
  libboost-program-options1.83.0 libepoxy0 libexif-doc
  libexif12 libpng-tools
The following NEW packages will be installed:
  libboost-program-options-dev
  libboost-program-options1.83-dev
  libboost-program-options1.83.0 libepoxy-dev libepoxy0
  libexif-dev libexif-doc libexif12 libpng-dev libpng-tools
0 upgraded, 10 newly installed, 0 to remove and 0 not upgraded.
Need to get 1943 kB of archives.
After this operation, 12.8 MB of additional disk space will be used.
Get:1 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libboost-program-options1.83.0 arm64 1.83.0-2.1ubuntu3.2 [317 kB]
Get:2 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libboost-program-options1.83-dev arm64 1.83.0-2.1ubuntu3.2 [391 kB]
Get:3 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libboost-program-options-dev arm64 1.83.0.1ubuntu2 [4084 B]
Get:4 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libepoxy0 arm64 1.5.10-1build1 [240 kB]
Get:5 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libepoxy-dev arm64 1.5.10-1build1 [132 kB]
Get:6 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libexif12 arm64 0.6.24-1build2 [86.5 kB]
Get:7 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libexif-dev arm64 0.6.24-1build2 [111 kB]
Get:8 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libexif-doc all 0.6.24-1build2 [366 kB]
Get:9 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libpng-dev arm64 1.6.43-5ubuntu0.6 [268 kB]
Get:10 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 libpng-tools arm64 1.6.43-5ubuntu0.6 [28.0 kB]
Fetched 1943 kB in 0s (5845 kB/s)       
Selecting previously unselected package libboost-program-options1.83.0:arm64.
(Reading database ... 97604 files and directories currently installed.)
Preparing to unpack .../0-libboost-program-options1.83.0_1.83.0-2.1ubuntu3.2_arm64.deb ...
Unpacking libboost-program-options1.83.0:arm64 (1.83.0-2.1ubuntu3.2) ...
Selecting previously unselected package libboost-program-options1.83-dev:arm64.
Preparing to unpack .../1-libboost-program-options1.83-dev_1.83.0-2.1ubuntu3.2_arm64.deb ...
Unpacking libboost-program-options1.83-dev:arm64 (1.83.0-2.1ubuntu3.2) ...
Selecting previously unselected package libboost-program-options-dev:arm64.
Preparing to unpack .../2-libboost-program-options-dev_1.83.0.1ubuntu2_arm64.deb ...
Unpacking libboost-program-options-dev:arm64 (1.83.0.1ubuntu2) ...
Selecting previously unselected package libepoxy0:arm64.
Preparing to unpack .../3-libepoxy0_1.5.10-1build1_arm64.deb ...
Unpacking libepoxy0:arm64 (1.5.10-1build1) ...
Selecting previously unselected package libepoxy-dev:arm64.
Preparing to unpack .../4-libepoxy-dev_1.5.10-1build1_arm64.deb ...
Unpacking libepoxy-dev:arm64 (1.5.10-1build1) ...
Selecting previously unselected package libexif12:arm64.
Preparing to unpack .../5-libexif12_0.6.24-1build2_arm64.deb ...
Unpacking libexif12:arm64 (0.6.24-1build2) ...
Selecting previously unselected package libexif-dev:arm64.
Preparing to unpack .../6-libexif-dev_0.6.24-1build2_arm64.deb ...
Unpacking libexif-dev:arm64 (0.6.24-1build2) ...
Selecting previously unselected package libexif-doc.
Preparing to unpack .../7-libexif-doc_0.6.24-1build2_all.deb ...
Unpacking libexif-doc (0.6.24-1build2) ...
Selecting previously unselected package libpng-dev:arm64.
Preparing to unpack .../8-libpng-dev_1.6.43-5ubuntu0.6_arm64.deb ...
Unpacking libpng-dev:arm64 (1.6.43-5ubuntu0.6) ...
Selecting previously unselected package libpng-tools.
Preparing to unpack .../9-libpng-tools_1.6.43-5ubuntu0.6_arm64.deb ...
Unpacking libpng-tools (1.6.43-5ubuntu0.6) ...
Setting up libboost-program-options1.83.0:arm64 (1.83.0-2.1ubuntu3.2) ...
Setting up libpng-tools (1.6.43-5ubuntu0.6) ...
Setting up libpng-dev:arm64 (1.6.43-5ubuntu0.6) ...
Setting up libboost-program-options1.83-dev:arm64 (1.83.0-2.1ubuntu3.2) ...
Setting up libboost-program-options-dev:arm64 (1.83.0.1ubuntu2) ...
Setting up libepoxy0:arm64 (1.5.10-1build1) ...
Setting up libexif12:arm64 (0.6.24-1build2) ...
Setting up libexif-doc (0.6.24-1build2) ...
Setting up libexif-dev:arm64 (0.6.24-1build2) ...
Setting up libepoxy-dev:arm64 (1.5.10-1build1) ...
Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
Processing triggers for man-db (2.12.0-4build2) ...
Scanning processes...                                           
Scanning processor microcode...                                 
Scanning linux images...                                        

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on
 this host.
```

</details>


# Install V4L

This is the linux video driver

```bash
sudo apt install -y v4l-utils
```

<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming$ sudo apt install -y v4l-utils
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-image-6.8.0-1047-raspi linux-modules-6.8.0-1047-raspi
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libv4l-0t64 libv4l2rds0t64 libv4lconvert0t64
The following NEW packages will be installed:
  libv4l-0t64 libv4l2rds0t64 libv4lconvert0t64 v4l-utils
0 upgraded, 4 newly installed, 0 to remove and 0 not upgraded.
Need to get 842 kB of archives.
After this operation, 3828 kB of additional disk space will be used.
Get:1 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libv4lconvert0t64 arm64 1.26.1-4build3 [88.6 kB]
Get:2 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libv4l-0t64 arm64 1.26.1-4build3 [46.4 kB]
Get:3 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libv4l2rds0t64 arm64 1.26.1-4build3 [20.1 kB]
Get:4 http://ports.ubuntu.com/ubuntu-ports noble/universe arm64 v4l-utils arm64 1.26.1-4build3 [687 kB]
Fetched 842 kB in 1s (1562 kB/s)  
Selecting previously unselected package libv4lconvert0t64:arm64.
(Reading database ... 97845 files and directories currently installed.)
Preparing to unpack .../libv4lconvert0t64_1.26.1-4build3_arm64.deb ...
Unpacking libv4lconvert0t64:arm64 (1.26.1-4build3) ...
Selecting previously unselected package libv4l-0t64:arm64.
Preparing to unpack .../libv4l-0t64_1.26.1-4build3_arm64.deb ...
Unpacking libv4l-0t64:arm64 (1.26.1-4build3) ...
Selecting previously unselected package libv4l2rds0t64:arm64.
Preparing to unpack .../libv4l2rds0t64_1.26.1-4build3_arm64.deb ...
Unpacking libv4l2rds0t64:arm64 (1.26.1-4build3) ...
Selecting previously unselected package v4l-utils.
Preparing to unpack .../v4l-utils_1.26.1-4build3_arm64.deb ...
Unpacking v4l-utils (1.26.1-4build3) ...
Setting up libv4lconvert0t64:arm64 (1.26.1-4build3) ...
Setting up libv4l-0t64:arm64 (1.26.1-4build3) ...
Setting up libv4l2rds0t64:arm64 (1.26.1-4build3) ...
Setting up v4l-utils (1.26.1-4build3) ...
Processing triggers for libc-bin (2.39-0ubuntu8.7) ...
Processing triggers for man-db (2.12.0-4build2) ...
Scanning processes...                                                 
Scanning processor microcode...                                       
Scanning linux images...                                              

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this
 host.
```

</details>

# Install G++

```bash
sudo apt update
sudo apt install g++
```


<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/libcamera$ sudo apt update
Hit:1 http://ports.ubuntu.com/ubuntu-ports noble InRelease
Hit:2 http://ports.ubuntu.com/ubuntu-ports noble-updates InRelease
Hit:3 http://ports.ubuntu.com/ubuntu-ports noble-backports InRelease
Hit:4 http://ports.ubuntu.com/ubuntu-ports noble-security InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
sona@rpi4-orso-sdbh:~/libcamera$ sudo apt install g++
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-image-6.8.0-1047-raspi linux-modules-6.8.0-1047-raspi
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  g++-13 g++-13-aarch64-linux-gnu g++-aarch64-linux-gnu
Suggested packages:
  gcc-13-doc
The following NEW packages will be installed:
  g++ g++-13 g++-13-aarch64-linux-gnu g++-aarch64-linux-gnu
0 upgraded, 4 newly installed, 0 to remove and 0 not upgraded.
Need to get 10.9 MB of archives.
After this operation, 30.6 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 g++-13-aarch64-linux-gnu arm64 13.3.0-6ubuntu2~24.04.1 [10.9 MB]
Get:2 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 g++-13 arm64 13.3.0-6ubuntu2~24.04.1 [16.0 kB]
Get:3 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 g++-aarch64-linux-gnu arm64 4:13.2.0-7ubuntu1 [962 B]
Get:4 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 g++ arm64 4:13.2.0-7ubuntu1 [1082 B]
Fetched 10.9 MB in 1s (8123 kB/s)
Selecting previously unselected package g++-13-aarch64-linux-gnu.
(Reading database ... 97898 files and directories currently installed.)
Preparing to unpack .../g++-13-aarch64-linux-gnu_13.3.0-6ubuntu2~24.04.1_arm64.deb ...
Unpacking g++-13-aarch64-linux-gnu (13.3.0-6ubuntu2~24.04.1) ...
Selecting previously unselected package g++-13.
Preparing to unpack .../g++-13_13.3.0-6ubuntu2~24.04.1_arm64.deb ...
Unpacking g++-13 (13.3.0-6ubuntu2~24.04.1) ...
Selecting previously unselected package g++-aarch64-linux-gnu.
Preparing to unpack .../g++-aarch64-linux-gnu_4%3a13.2.0-7ubuntu1_arm64.deb ...
Unpacking g++-aarch64-linux-gnu (4:13.2.0-7ubuntu1) ...
Selecting previously unselected package g++.
Preparing to unpack .../g++_4%3a13.2.0-7ubuntu1_arm64.deb ...
Unpacking g++ (4:13.2.0-7ubuntu1) ...
Setting up g++-13-aarch64-linux-gnu (13.3.0-6ubuntu2~24.04.1) ...
Setting up g++-13 (13.3.0-6ubuntu2~24.04.1) ...
Setting up g++-aarch64-linux-gnu (4:13.2.0-7ubuntu1) ...
Setting up g++ (4:13.2.0-7ubuntu1) ...
update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mode
Processing triggers for man-db (2.12.0-4build2) ...
Scanning processes...                                                 
Scanning processor microcode...                                       
Scanning linux images...                                              

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this
 host.
```

</details>



# REBOOT

```bash
sudo reboot
```

# Clone Libcamera

```bash
cd
git clone https://github.com/raspberrypi/libcamera.git
cd libcamera
```

```bash
meson setup build --buildtype=release \
  -Dpipelines=rpi/vc4,rpi/pisp \
  -Dipas=rpi/vc4,rpi/pisp \
  -Dv4l2=true \
  -Dgstreamer=enabled \
  -Dtest=false \
  -Dlc-compliance=disabled \
  -Dcam=disabled \
  -Dqcam=disabled \
  -Ddocumentation=disabled \
  -Dpycamera=enabled
```

<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/libcamera$ meson setup build --buildtype=release \
  -Dpipelines=rpi/vc4,rpi/pisp \
  -Dipas=rpi/vc4,rpi/pisp \
  -Dv4l2=true \
  -Dgstreamer=enabled \
  -Dtest=false \
  -Dlc-compliance=disabled \
  -Dcam=disabled \
  -Dqcam=disabled \
  -Ddocumentation=disabled \
  -Dpycamera=enabled
The Meson build system
Version: 1.3.2
Source dir: /home/sona/libcamera
Build dir: /home/sona/libcamera/build
Build type: native build
meson_options.txt:76: WARNING: Keyword argument "value" defined multiple times.
WARNING: This will be an error in future Meson releases.
DEPRECATION: Option 'v4l2' value 'true' is replaced by 'enabled'
Project name: libcamera
Project version: 0.7.1
C compiler for the host machine: cc (gcc 13.3.0 "cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0")
C linker for the host machine: cc ld.bfd 2.42
C++ compiler for the host machine: c++ (gcc 13.3.0 "c++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0")
C++ linker for the host machine: c++ ld.bfd 2.42
Host machine cpu family: aarch64
Host machine cpu: aarch64
Header "unistd.h" has symbol "close_range" : YES 
Header "fcntl.h" has symbol "F_ADD_SEALS" : YES 
Header "unistd.h" has symbol "issetugid" : NO 
Header "locale.h" has symbol "locale_t" : YES 
Header "sys/mman.h" has symbol "memfd_create" : YES 
Header "stdlib.h" has symbol "secure_getenv" : YES 
Header "version" has symbol "_LIBCPP_VERSION" : NO 
Header "version" has symbol "__GLIBCXX__" : YES 
Message: Detected C++ standard library: libstdc++
Compiler for C supports arguments -Wno-c99-designator: NO 
Found pkg-config: YES (/usr/bin/pkg-config) 1.8.1
Found CMake: /usr/bin/cmake (3.28.3)
Run-time dependency lttng-ust found: NO (tried pkgconfig and cmake)
Program ./parser.py found: YES (/home/sona/libcamera/utils/codegen/ipc/./parser.py)
Program ./generate.py found: YES (/home/sona/libcamera/utils/codegen/ipc/./generate.py)
Program ./extract-docs.py found: YES (/home/sona/libcamera/utils/codegen/ipc/./extract-docs.py)
Configuring version.h using configuration
Program openssl found: YES (/usr/bin/openssl)
Run-time dependency libyuv found: NO (tried pkgconfig and cmake)
Has header "libyuv.h" : NO 
Library atomic found: YES
Run-time dependency threads found: YES
Run-time dependency libdw found: YES 0.190
Run-time dependency libunwind found: YES 1.6.2
Header "execinfo.h" has symbol "backtrace" : YES 
Library rt found: YES
Run-time dependency libpisp found: NO (tried pkgconfig and cmake)
Looking for a fallback subproject for the dependency libpisp
Cloning into 'libpisp'...
remote: Enumerating objects: 101, done.
remote: Counting objects: 100% (101/101), done.
remote: Compressing objects: 100% (92/92), done.
remote: Total 101 (delta 6), reused 47 (delta 6), pack-reused 0 (from 0)
Receiving objects: 100% (101/101), 114.55 KiB | 2.01 MiB/s, done.
Resolving deltas: 100% (6/6), done.

Executing subproject libpisp 

libpisp| DEPRECATION: Option 'v4l2' value 'true' is replaced by 'enabled'
libpisp| Project name: libpisp
libpisp| Project version: 1.3.0
libpisp| C compiler for the host machine: cc (gcc 13.3.0 "cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0")
libpisp| C linker for the host machine: cc ld.bfd 2.42
libpisp| C++ compiler for the host machine: c++ (gcc 13.3.0 "c++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0")
libpisp| C++ linker for the host machine: c++ ld.bfd 2.42
libpisp| Configuring pisp_build_config.h using configuration
libpisp| Run-time dependency nlohmann_json found: NO (tried pkgconfig and cmake)
libpisp| Looking for a fallback subproject for the dependency nlohmann_json
libpisp| Using subprojects/libpisp/subprojects/nlohmann_json.wrap
libpisp| Downloading nlohmann_json source from https://github.com/nlohmann/json/releases/download/v3.11.2/include.zip
Download size: 293810
Downloading: ..........

Executing subproject libpisp:nlohmann_json

nlohmann_json| DEPRECATION: Option 'v4l2' value 'true' is replaced by 'enabled'
nlohmann_json| Project name: nlohmann_json
nlohmann_json| Project version: 3.11.2
nlohmann_json| C++ compiler for the host machine: c++ (gcc 13.3.0 "c++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0")
nlohmann_json| C++ linker for the host machine: c++ ld.bfd 2.42
nlohmann_json| Build targets in project: 25
nlohmann_json| Subproject nlohmann_json finished.

libpisp| Dependency nlohmann_json from subproject subprojects/nlohmann_json-3.11.2 found: YES 3.11.2
libpisp| Dependency threads found: YES unknown (cached)
libpisp| Library dl found: YES
libpisp| Run-time dependency Boost (missing: log, log_setup, system, thread) found: NO (tried system)
libpisp| Build targets in project: 27
libpisp| Subproject libpisp finished.

Dependency libpisp from subproject subprojects/libpisp found: YES 1.3.0
Run-time dependency dl found: YES
Run-time dependency libudev found: YES 255
Run-time dependency yaml-0.1 found: NO (tried pkgconfig and cmake)
Looking for a fallback subproject for the dependency yaml-0.1
Downloading libyaml source from https://pyyaml.org/download/libyaml/yaml-0.2.5.tar.gz
Download size: 609454
Downloading: ..........
Downloading libyaml patch from https://wrapdb.mesonbuild.com/v2/libyaml_0.2.5-1/get_patch
Download size: 2092
Downloading: ..........

Executing subproject libyaml 

libyaml| DEPRECATION: Option 'v4l2' value 'true' is replaced by 'enabled'
libyaml| Project name: yaml-0.1
libyaml| Project version: 0.2.5
libyaml| C compiler for the host machine: cc (gcc 13.3.0 "cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0")
libyaml| C linker for the host machine: cc ld.bfd 2.42
libyaml| Configuring config.h using configuration
libyaml| Build targets in project: 31
libyaml| Subproject libyaml finished.

Dependency yaml-0.1 from subproject subprojects/yaml-0.2.5 found: YES 0.2.5
Run-time dependency gnutls found: YES 3.8.3
Dependency libexif skipped: feature android disabled
Dependency libjpeg skipped: feature android disabled
Run-time dependency tensorflow-lite found: NO (tried pkgconfig and cmake)
Dependency libevent_pthreads skipped: feature cam disabled
Dependency libevent_pthreads skipped: feature lc-compliance disabled
Run-time dependency libtiff-4 found: YES 4.5.1
Dependency gtest skipped: feature lc-compliance disabled
Dependency qt6 (modules: Core, Gui, OpenGL, OpenGLWidgets, Widgets) skipped: feature qcam disabled
Run-time dependency glib-2.0 found: YES 2.80.0
Run-time dependency gstreamer-video-1.0 found: YES 1.24.2
Run-time dependency gstreamer-allocators-1.0 found: YES 1.24.2
Program python3 found: YES (/usr/bin/python3)
Run-time dependency pybind11 found: YES 2.11.1
Run-time dependency python found: YES 3.12
Configuring libcamerify using configuration
Program doxygen skipped: feature documentation disabled
Program dot skipped: feature documentation disabled
Program sphinx-build-3 sphinx-build skipped: feature documentation disabled
Configuring config.h using configuration
Build targets in project: 56

libcamera 0.7.1

  Versions
    Sources                  : 0.7.1+rpt20260429

  Paths
    LIBCAMERA_DATA_DIR       : "/usr/local/share/libcamera"
    LIBCAMERA_SYSCONF_DIR    : "/usr/local/etc/libcamera"
    IPA_PROXY_DIR            : "/usr/local/libexec/libcamera"
    IPA_CONFIG_DIR           : "/usr/local/etc/libcamera/ipa:/usr/local/share/libcamera/ipa"
    IPA_MODULE_DIR           : "/usr/local/lib/libcamera/ipa"

  Configuration
    SoftISP support          : NO
    IPA modules signed with  : gnutls
    Enabled pipelines        : rpi/vc4
                               rpi/pisp
    Enabled IPA modules      : rpi/vc4
                               rpi/pisp
    Controls files           : control_ids_core.yaml
                               control_ids_debug.yaml
                               control_ids_draft.yaml
                               control_ids_rpi.yaml
    Properties files         : property_ids_draft.yaml
                               property_ids_core.yaml
    Hotplug support          : YES
    Tracing support          : NO
    Android support          : NO
    GStreamer support        : YES
    Python bindings          : YES
    V4L2 emulation support   : YES
    Unit tests               : NO

  Applications
    cam application          : NO
    cam options              :
    DNG output support       : YES
    qcam application         : NO
    lc-compliance application: NO

  Subprojects
    libpisp                  : YES 1 warnings
    libyaml                  : YES
    nlohmann_json            : YES (from libpisp)

  User defined options
    buildtype                : release
    cam                      : disabled
    documentation            : disabled
    gstreamer                : enabled
    ipas                     : rpi/vc4,rpi/pisp
    lc-compliance            : disabled
    pipelines                : rpi/vc4,rpi/pisp
    pycamera                 : enabled
    qcam                     : disabled
    test                     : false
    v4l2                     : true

Found ninja-1.11.1 at /usr/bin/ninja
```

</details>

```bash
ninja -C build
```

<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/libcamera$ ninja -C build
ninja: Entering directory `build'
[19/275] Generating src/ipa-priv-key with a custom command
..+...+.......+...+..+.........+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*...+..+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+......+...+.........+.+.........+.....+.......+...........+....+.....+...+.+............+..+...+....+.....+...+...+.............+...........+......+.......+.....+......+.+....................+..................+..........+...+........+......+.+.....+...+.........+.+..+....+.........+......+...............+...+...+...+...........+.+..+...+...+.+...+.................+.........+..........+..+.........+...+...+..........+...+......+...+..+.+...+......+.....+..........+.....+...+..........+........+...+.......+.................+...............+.+.....+.+.....+....+......+..............+......+......+.......+...........+....+..+....+........................+...+..+......+....+..+..........+.....+...+.+..+....+..............+...............+......+.+..+...+....+.....+....+......+........+...+..................+.........+.......+.....+.+..+.......+.........+.....+......+......+.......+...........+.......+.....+...+.+...+............+......+.........+......+..................+..............+...............+...+...+.+......+...+.........+..+...+................+......+.....+.............+..+................+..+.+...........+.........+.+......+.....+....+...+.....+.+............+...+.....+............+..........+...+.........+............+...+......+..+...+....+.....+............+...+......+.+......+..+......+...............+.+...+...+..............+...+..........+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
........+..+....+...+...+...+......+......+..+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.....+...+...+.....+...+......+.+.....+.......+.....+.............+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+.....+...+.........+...+...+.+...+......+..+...+......+...+.+.........+......+.........+.................+.+..+.+.....................+...+..+...+...+...+....+...+.....+..........+..+...............+...+.......+.....+...+.......+...+...+......+...........+...+.......+........+..........+...........+.+....................+............+.+..+...+.+.....+.+.........+.....+.+........+.+..............+.+........................+......+...+.....+.+..+...................+...+.....+.+.....+............+....+.....+......+...+....+...........+....+..+.+..+...+...............+...+.+........+.+.....+.+......+........+.+.....+.........+.+......+..+............+....+...........+....+...........+......+.............+..+........................+......+.........+...+..........+...........+.......+............+...........+....+...+............+...+..+.+.....+.......+..+......+......+..........+.........+..............+...+.......+.....+.+..+...+............+....+...+.....+.+.....+.+.....+.+.....+..........+..................+..+.......+..+....+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
[69/275] Compiling C object subpr...sts/test-reader.p/test-reader.c.o
../subprojects/yaml-0.2.5/tests/test-reader.c: In function ‘check_boms’:
../subprojects/yaml-0.2.5/tests/test-reader.c:187:31: warning: comparison of integer expressions of different signedness: ‘size_t’ {aka ‘long unsigned int’} and ‘int’ [-Wsign-compare]
  187 |             if (parser.unread != check) {
      |                               ^~
[72/275] Compiling C object subpr...2.5/libyaml-0.a.p/src_emitter.c.o
../subprojects/yaml-0.2.5/src/emitter.c: In function ‘yaml_emitter_write_plain_scalar’:
../subprojects/yaml-0.2.5/src/emitter.c:28:6: warning: value computed is not used [-Wunused-value]
   28 |      && ((emitter->line_break == YAML_CR_BREAK ?                                \
      |      ^~
../subprojects/yaml-0.2.5/src/emitter.c:56:11: note: in expansion of macro ‘PUT_BREAK’
   56 |          (PUT_BREAK(emitter),                                                   \
      |           ^~~~~~~~~
../subprojects/yaml-0.2.5/src/emitter.c:1962:18: note: in expansion of macro ‘WRITE_BREAK’
 1962 |             if (!WRITE_BREAK(emitter, string)) return 0;
      |                  ^~~~~~~~~~~
../subprojects/yaml-0.2.5/src/emitter.c: In function ‘yaml_emitter_write_single_quoted_scalar’:
../subprojects/yaml-0.2.5/src/emitter.c:28:6: warning: value computed is not used [-Wunused-value]
   28 |      && ((emitter->line_break == YAML_CR_BREAK ?                                \
      |      ^~
../subprojects/yaml-0.2.5/src/emitter.c:56:11: note: in expansion of macro ‘PUT_BREAK’
   56 |          (PUT_BREAK(emitter),                                                   \
      |           ^~~~~~~~~
../subprojects/yaml-0.2.5/src/emitter.c:2019:18: note: in expansion of macro ‘WRITE_BREAK’
 2019 |             if (!WRITE_BREAK(emitter, string)) return 0;
      |                  ^~~~~~~~~~~
../subprojects/yaml-0.2.5/src/emitter.c: In function ‘yaml_emitter_write_literal_scalar’:
../subprojects/yaml-0.2.5/src/emitter.c:28:6: warning: value computed is not used [-Wunused-value]
   28 |      && ((emitter->line_break == YAML_CR_BREAK ?                                \
      |      ^~
../subprojects/yaml-0.2.5/src/emitter.c:56:11: note: in expansion of macro ‘PUT_BREAK’
   56 |          (PUT_BREAK(emitter),                                                   \
      |           ^~~~~~~~~
../subprojects/yaml-0.2.5/src/emitter.c:2285:18: note: in expansion of macro ‘WRITE_BREAK’
 2285 |             if (!WRITE_BREAK(emitter, string)) return 0;
      |                  ^~~~~~~~~~~
../subprojects/yaml-0.2.5/src/emitter.c: In function ‘yaml_emitter_write_folded_scalar’:
../subprojects/yaml-0.2.5/src/emitter.c:28:6: warning: value computed is not used [-Wunused-value]
   28 |      && ((emitter->line_break == YAML_CR_BREAK ?                                \
      |      ^~
../subprojects/yaml-0.2.5/src/emitter.c:56:11: note: in expansion of macro ‘PUT_BREAK’
   56 |          (PUT_BREAK(emitter),                                                   \
      |           ^~~~~~~~~
../subprojects/yaml-0.2.5/src/emitter.c:2334:18: note: in expansion of macro ‘WRITE_BREAK’
 2334 |             if (!WRITE_BREAK(emitter, string)) return 0;
      |                  ^~~~~~~~~~~
[75/275] Generating src/libcamera...pub_key_cpp with a custom command
writing RSA key
[76/275] Generating src/libcamera...der-headers with a custom command
[SHADER-GEN] bayer_1x_packed_frag
[SHADER-GEN] bayer_unpacked_frag
[SHADER-GEN] bayer_unpacked_vert
[SHADER-GEN] identity_vert
[275/275] Linking target src/py/l....cpython-312-aarch64-linux-gnu.so
```

</details>


```bash
sudo ninja -C build install
```


<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/libcamera$ sudo ninja -C build install
[sudo] password for sona: 
ninja: Entering directory `build'
[5/6] Installing files.
Installing include/libcamera/ipa/core_ipa_interface.h to /usr/local/include/libcamera/libcamera/ipa
Installing include/libcamera/ipa/raspberrypi_ipa_interface.h to /usr/local/include/libcamera/libcamera/ipa
Installing include/libcamera/control_ids.h to /usr/local/include/libcamera/libcamera
Installing include/libcamera/property_ids.h to /usr/local/include/libcamera/libcamera
Installing include/libcamera/formats.h to /usr/local/include/libcamera/libcamera
Installing include/libcamera/libcamera.h to /usr/local/include/libcamera/libcamera
Installing src/libcamera/base/libcamera-base.so.0.7.1 to /usr/local/lib
Installing subprojects/libpisp/src/libpisp.so.1.3.0 to /usr/local/lib
Installing subprojects/yaml-0.2.5/libyaml-0.a to /usr/local/lib
Installing src/libcamera/libcamera.so.0.7.1 to /usr/local/lib
Installing src/libcamera/proxy/worker/raspberrypi_ipa_proxy to /usr/local/libexec/libcamera
Installing src/ipa/rpi/vc4/ipa_rpi_vc4.so to /usr/local/lib/libcamera/ipa
Installing src/ipa/rpi/pisp/ipa_rpi_pisp.so to /usr/local/lib/libcamera/ipa
Installing src/gstreamer/libgstlibcamera.so to /usr/local/lib/gstreamer-1.0
Installing src/py/libcamera/_libcamera.cpython-312-aarch64-linux-gnu.so to /usr/local/lib/python3/dist-packages/libcamera
Installing src/v4l2/v4l2-compat.so to /usr/local/libexec/libcamera
Installing /home/sona/libcamera/include/libcamera/base/bound_method.h to /usr/local/include/libcamera/libcamera/base
Installing /home/sona/libcamera/include/libcamera/base/class.h to /usr/local/include/libcamera/libcamera/base
Installing /home/sona/libcamera/include/libcamera/base/flags.h to /usr/local/include/libcamera/libcamera/base
Installing /home/sona/libcamera/include/libcamera/base/object.h to /usr/local/include/libcamera/libcamera/base
Installing /home/sona/libcamera/include/libcamera/base/shared_fd.h to /usr/local/include/libcamera/libcamera/base
Installing /home/sona/libcamera/include/libcamera/base/signal.h to /usr/local/include/libcamera/libcamera/base
Installing /home/sona/libcamera/include/libcamera/base/span.h to /usr/local/include/libcamera/libcamera/base
Installing /home/sona/libcamera/include/libcamera/base/unique_fd.h to /usr/local/include/libcamera/libcamera/base
Installing /home/sona/libcamera/include/libcamera/ipa/ipa_controls.h to /usr/local/include/libcamera/libcamera/ipa
Installing /home/sona/libcamera/include/libcamera/ipa/ipa_interface.h to /usr/local/include/libcamera/libcamera/ipa
Installing /home/sona/libcamera/include/libcamera/ipa/ipa_module_info.h to /usr/local/include/libcamera/libcamera/ipa
Installing /home/sona/libcamera/include/libcamera/camera.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/camera_manager.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/color_space.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/controls.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/fence.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/framebuffer.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/framebuffer_allocator.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/geometry.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/logging.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/orientation.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/pixel_format.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/request.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/stream.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/include/libcamera/transform.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/common/pisp_common.h to /usr/local/include/libpisp/common
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/common/logging.hpp to /usr/local/include/libpisp/common
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/common/shm_mutex.hpp to /usr/local/include/libpisp/common
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/common/utils.hpp to /usr/local/include/libpisp/common
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/common/version.hpp to /usr/local/include/libpisp/common
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/variants/variant.hpp to /usr/local/include/libpisp/variants
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/frontend/frontend.hpp to /usr/local/include/libpisp/frontend
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/frontend/pisp_fe_config.h to /usr/local/include/libpisp/frontend
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/frontend/pisp_statistics.h to /usr/local/include/libpisp/frontend
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/backend/backend.hpp to /usr/local/include/libpisp/backend
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/backend/pisp_be_config.h to /usr/local/include/libpisp/backend
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/backend/tiling/pisp_tiling.hpp to /usr/local/include/libpisp/backend/tiling
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/backend/tiling/types.hpp to /usr/local/include/libpisp/backend/tiling
Installing /home/sona/libcamera/subprojects/libpisp/src/helpers/backend_device.hpp to /usr/local/include/libpisp/helpers
Installing /home/sona/libcamera/subprojects/libpisp/src/helpers/device_fd.hpp to /usr/local/include/libpisp/helpers
Installing /home/sona/libcamera/subprojects/libpisp/src/helpers/media_device.hpp to /usr/local/include/libpisp/helpers
Installing /home/sona/libcamera/subprojects/libpisp/src/helpers/v4l2_device.hpp to /usr/local/include/libpisp/helpers
Installing /home/sona/libcamera/subprojects/yaml-0.2.5/include/yaml.h to /usr/local/include
Installing /home/sona/libcamera/utils/libcamera-bug-report to /usr/local/bin
Installing /home/sona/libcamera/build/include/libcamera/version.h to /usr/local/include/libcamera/libcamera
Installing /home/sona/libcamera/build/meson-private/libcamera-base.pc to /usr/local/lib/pkgconfig
Installing /home/sona/libcamera/src/libcamera/pipeline/rpi/vc4/data/example.yaml to /usr/local/share/libcamera/pipeline/rpi/vc4
Installing /home/sona/libcamera/src/libcamera/pipeline/rpi/vc4/data/rpi_apps.yaml to /usr/local/share/libcamera/pipeline/rpi/vc4
Installing /home/sona/libcamera/subprojects/libpisp/src/libpisp/backend/backend_default_config.json to /usr/local/share/libpisp
Installing /home/sona/libcamera/build/meson-private/libpisp.pc to /usr/local/lib/pkgconfig
Installing /home/sona/libcamera/src/libcamera/pipeline/rpi/pisp/data/example.yaml to /usr/local/share/libcamera/pipeline/rpi/pisp
Installing /home/sona/libcamera/build/meson-private/yaml-0.1.pc to /usr/local/lib/pkgconfig
Installing /home/sona/libcamera/build/meson-private/libcamera.pc to /usr/local/lib/pkgconfig
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx219.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx219_noir.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx283.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx290.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx296.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx296_mono.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx327.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx335.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx378.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx415.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx415_b0569.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx462.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx477.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx477_noir.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx477_scientific.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx500.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx519.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx708.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx708_noir.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx708_wide.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/imx708_wide_noir.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/ov5647.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/ov5647_noir.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/ov64a40.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/ov7251_mono.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/ov9281_mono.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/se327m12.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/uncalibrated.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/vd55g1.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/vd55g1_mono.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/vd56g3.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/vc4/data/vd56g3_mono.json to /usr/local/share/libcamera/ipa/rpi/vc4
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx219.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx219_noir.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx283.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx290.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx296.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx296_mono.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx335.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx378.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx415.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx415_b0569.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx462.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx477.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx477_noir.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx477_scientific.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx500.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx519.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx708.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx708_noir.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx708_wide.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/imx708_wide_noir.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/ov5647.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/ov5647_noir.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/ov64a40.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/ov9281_mono.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/se327m12.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/uncalibrated.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/vd55g1.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/vd55g1_mono.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/vd56g3.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/ipa/rpi/pisp/data/vd56g3_mono.json to /usr/local/share/libcamera/ipa/rpi/pisp
Installing /home/sona/libcamera/src/py/libcamera/__init__.py to /usr/local/lib/python3/dist-packages/libcamera
Installing /home/sona/libcamera/build/src/v4l2/libcamerify to /usr/local/bin
Installing symlink pointing to libcamera-base.so.0.7.1 to /usr/local/lib/libcamera-base.so.0.7
Installing symlink pointing to libcamera-base.so.0.7 to /usr/local/lib/libcamera-base.so
Installing symlink pointing to libpisp.so.1.3.0 to /usr/local/lib/libpisp.so.1
Installing symlink pointing to libpisp.so.1 to /usr/local/lib/libpisp.so
Installing symlink pointing to libcamera.so.0.7.1 to /usr/local/lib/libcamera.so.0.7
Installing symlink pointing to libcamera.so.0.7 to /usr/local/lib/libcamera.so
Running custom install script '/home/sona/libcamera/src/ipa/ipa-sign-install.sh /home/sona/libcamera/build/src/ipa-priv-key.pem lib/libcamera/ipa/ipa_rpi_vc4.so lib/libcamera/ipa/ipa_rpi_pisp.so'
Regenerating IPA modules signatures
Running custom install script '/usr/bin/python3 /home/sona/libcamera/build/meson-private/pycompile.py python-3.12-installed.json 0'
Compiling '/usr/local/lib/python3/dist-packages/libcamera/__init__.py'..
```

</details>

```bash
cd
```


# Clone C++ Raspicam Application

```bash
cd 
git clone https://github.com/raspberrypi/rpicam-apps.git
cd rpicam-apps
```

<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/HowTo-Ubuntu24S-Raspicam-Webserver-Streaming/rpicam-apps$ cd
sona@rpi4-orso-sdbh:~$ git clone https://github.com/raspberrypi/rpicam-apps.git
Cloning into 'rpicam-apps'...
remote: Enumerating objects: 4704, done.
remote: Counting objects: 100% (168/168), done.
remote: Compressing objects: 100% (60/60), done.
remote: Total 4704 (delta 118), reused 108 (delta 108), pack-reused 4536 (from 3)
Receiving objects: 100% (4704/4704), 253.49 MiB | 10.31 MiB/s, done.
Resolving deltas: 100% (3102/3102), done.
sona@rpi4-orso-sdbh:~$ cd rpicam-apps
```

</details>

# Configure Build

```bash
meson setup build \
  -Denable_libav=disabled \
  -Denable_drm=enabled \
  -Denable_egl=disabled \
  -Denable_qt=disabled \
  -Denable_opencv=disabled \
  -Denable_tflite=disabled \
  -Denable_hailo=disabled
```

<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/rpicam-apps$ meson setup build \
  -Denable_libav=disabled \
  -Denable_drm=enabled \
  -Denable_egl=disabled \
  -Denable_qt=disabled \
  -Denable_opencv=disabled \
  -Denable_tflite=disabled \
  -Denable_hailo=disabled
The Meson build system
Version: 1.3.2
Source dir: /home/sona/rpicam-apps
Build dir: /home/sona/rpicam-apps/build
Build type: native build
Project name: rpicam-apps
Project version: 1.12.0
C compiler for the host machine: cc (gcc 13.3.0 "cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0")
C linker for the host machine: cc ld.bfd 2.42
C++ compiler for the host machine: c++ (gcc 13.3.0 "c++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0")
C++ linker for the host machine: c++ ld.bfd 2.42
Host machine cpu family: aarch64
Host machine cpu: aarch64
Run-time dependency dl found: YES
Found pkg-config: YES (/usr/bin/pkg-config) 1.8.1
Run-time dependency libcamera found: YES 0.7.1
Run-time dependency Boost (found: program_options) found: YES 1.83.0 (/usr)
Run-time dependency threads found: YES
Dependency libavcodec skipped: feature enable_libav disabled
Run-time dependency libexif found: YES 0.6.24
Run-time dependency libjpeg found: YES 2.1.5
Run-time dependency libtiff-4 found: YES 4.5.1
Run-time dependency libpng found: YES 1.6.43
Dependency opencv4 skipped: feature enable_opencv disabled
Dependency HailoRT (modules: HailoRT::libhailort) skipped: feature enable_hailo disabled
Dependency hailo-tappas-core skipped: feature enable_hailo disabled
Run-time dependency libdrm found: YES 2.4.125
Dependency x11 skipped: feature enable_egl disabled
Dependency epoxy skipped: feature enable_egl disabled
Configuring config.h using configuration
Build targets in project: 9

rpicam-apps 1.12.0

  libcamera
    location             : /usr/local/lib
    version              : 0.7.1

  Build configuration
    libav encoder        : NO
    drm preview          : YES
    egl preview          : NO
    qt preview           : NO
    OpenCV postprocessing: NO
    TFLite postprocessing: NO
    Hailo postprocessing : NO
    IMX500 postprocessing: NO

  User defined options
    enable_drm           : enabled
    enable_egl           : disabled
    enable_hailo         : disabled
    enable_libav         : disabled
    enable_opencv        : disabled
    enable_qt            : disabled
    enable_tflite        : disabled

Found ninja-1.11.1 at /usr/bin/ninja
```

</details>





```bash
meson compile -C build
```

<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/rpicam-apps$ meson compile -C build
INFO: autodetecting backend as ninja
INFO: calculating backend command to run: /usr/bin/ninja -C /home/sona/rpicam-apps/build
ninja: Entering directory `/home/sona/rpicam-apps/build'
[45/45] Linking target apps/rpicam-raw
```

</details>


```bash
sudo meson install -C build
```

<details>
<summary>Log</summary>

```bash
sona@rpi4-orso-sdbh:~/rpicam-apps$ sudo meson install -C build
Dropping privileges to 'sona' before running ninja...
ninja: Entering directory `/home/sona/rpicam-apps/build'
[4/9] Generating symbol file l...ibrpicam_app.so.1.12.0.symbols
Installing post_processing_stages/core-postproc.so to /usr/local/lib/rpicam-apps-postproc
Installing preview/drm-preview.so to /usr/local/lib/rpicam-apps-preview
Installing librpicam_app.so.1.12.0 to /usr/local/lib
Installing apps/rpicam-still to /usr/local/bin
Installing apps/rpicam-vid to /usr/local/bin
Installing apps/rpicam-hello to /usr/local/bin
Installing apps/rpicam-raw to /usr/local/bin
Installing apps/rpicam-jpeg to /usr/local/bin
Installing /home/sona/rpicam-apps/core/buffer_sync.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/completed_request.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/dl_lib.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/dma_heaps.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/frame_info.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/rpicam_app.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/rpicam_encoder.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/logging.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/metadata.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/options.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/post_processor.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/still_options.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/stream_info.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/version.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/core/video_options.hpp to /usr/local/include/rpicam-apps/core
Installing /home/sona/rpicam-apps/encoder/encoder.hpp to /usr/local/include/rpicam-apps/encoder
Installing /home/sona/rpicam-apps/encoder/h264_encoder.hpp to /usr/local/include/rpicam-apps/encoder
Installing /home/sona/rpicam-apps/encoder/mjpeg_encoder.hpp to /usr/local/include/rpicam-apps/encoder
Installing /home/sona/rpicam-apps/encoder/null_encoder.hpp to /usr/local/include/rpicam-apps/encoder
Installing /home/sona/rpicam-apps/image/image.hpp to /usr/local/include/rpicam-apps/image
Installing /home/sona/rpicam-apps/output/circular_output.hpp to /usr/local/include/rpicam-apps/output
Installing /home/sona/rpicam-apps/output/file_output.hpp to /usr/local/include/rpicam-apps/output
Installing /home/sona/rpicam-apps/output/net_output.hpp to /usr/local/include/rpicam-apps/output
Installing /home/sona/rpicam-apps/output/output.hpp to /usr/local/include/rpicam-apps/output
Installing /home/sona/rpicam-apps/post_processing_stages/histogram.hpp to /usr/local/include/rpicam-apps/post_processing_stages
Installing /home/sona/rpicam-apps/post_processing_stages/object_detect.hpp to /usr/local/include/rpicam-apps/post_processing_stages
Installing /home/sona/rpicam-apps/post_processing_stages/post_processing_stage.hpp to /usr/local/include/rpicam-apps/post_processing_stages
Installing /home/sona/rpicam-apps/post_processing_stages/pwl.hpp to /usr/local/include/rpicam-apps/post_processing_stages
Installing /home/sona/rpicam-apps/post_processing_stages/segmentation.hpp to /usr/local/include/rpicam-apps/post_processing_stages
Installing /home/sona/rpicam-apps/post_processing_stages/tf_stage.hpp to /usr/local/include/rpicam-apps/post_processing_stages
Installing /home/sona/rpicam-apps/preview/preview.hpp to /usr/local/include/rpicam-apps/preview
Installing /home/sona/rpicam-apps/assets/hdr.json to /usr/local/share/rpi-camera-assets
Installing /home/sona/rpicam-apps/assets/motion_detect.json to /usr/local/share/rpi-camera-assets
Installing /home/sona/rpicam-apps/assets/negate.json to /usr/local/share/rpi-camera-assets
Installing /home/sona/rpicam-apps/assets/acoustic_focus.json to /usr/local/share/rpi-camera-assets
Installing /home/sona/rpicam-apps/utils/camera-bug-report to /usr/local/bin
Installing /home/sona/rpicam-apps/build/meson-private/rpicam_app.pc to /usr/local/lib/pkgconfig
Installing symlink pointing to librpicam_app.so.1.12.0 to /usr/local/lib/librpicam_app.so.1
Installing symlink pointing to librpicam_app.so.1 to /usr/local/lib/librpicam_app.so
```

</details>

# Camera CSI Config File

```bash
cat /boot/firmware/config.txt
```

```bash
sona@rpi4-orso-sdbh:~$ cat /boot/firmware/config.txt
[all]
arm_64bit=1
kernel=vmlinuz
cmdline=cmdline.txt
initramfs initrd.img followkernel

# Enable the audio output, I2C and SPI interfaces on the GPIO header. As these
# parameters related to the base device-tree they must appear *before* any
# other dtoverlay= specification
dtparam=audio=on
dtparam=i2c_arm=on
dtparam=spi=on

# Comment out the following line if the edges of the desktop appear outside
# the edges of your display
disable_overscan=1

# If you have issues with audio, you may try uncommenting the following line
# which forces the HDMI output into HDMI mode instead of DVI (which doesn't
# support audio output)
#hdmi_drive=2

# Enable the KMS ("full" KMS) graphics overlay, leaving GPU memory as the
# default (the kernel is in control of graphics memory with full KMS)
dtoverlay=vc4-kms-v3d
disable_fw_kms_setup=1

# Enable the serial pins
enable_uart=1

# Autoload overlays for any recognized cameras or displays that are attached
# to the CSI/DSI ports. Please note this is for libcamera support, *not* for
# the legacy camera stack
camera_auto_detect=1
display_auto_detect=1

# Config settings specific to arm64
dtoverlay=dwc2

[pi4]
max_framebuffers=2
arm_boost=1

[pi3+]
# Use a smaller contiguous memory area, specifically on the 3A+ to avoid an
# OOM oops on boot. The 3B+ is also affected by this section, but it shouldn't
# cause any issues on that board
dtoverlay=vc4-kms-v3d,cma-128

[pi02]
# The Zero 2W is another 512MB board which is occasionally affected by the same
# OOM oops on boot.
dtoverlay=vc4-kms-v3d,cma-128

[cm4]
# Enable the USB2 outputs on the IO board (assuming your CM4 is plugged into
# such a board)
dtoverlay=dwc2,dr_mode=host

[all]
```

### overlay

Not sure what this does

```bash
# For Camera Module 3
dtoverlay=imx708

# For other cameras, use:
# dtoverlay=imx477  # HQ Camera
# dtoverlay=imx296  # GS Camera
# dtoverlay=imx519  # 16MP Camera
```

# Reboot


```bash
sudo ldconfig
sudo reboot
```

# Test rpicam application

```bash
sona@rpi4-orso-sdbh:~$ rpicam-hello --version
rpicam-apps build: v1.12.0 9d41d4b7a83d 30-05-2026 (09:12:53)
rpicam-apps capabilites: egl:0 qt:0 drm:1 libav:0
libcamera build: v0.7.1+rpt20260429
```

# EOL


```bash
```


<details>
<summary>Log</summary>

```bash
xxx
```

</details>

