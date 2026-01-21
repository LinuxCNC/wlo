---
layout: page
title: Downloads
navbar: true
joomla_id: 5
joomla_url: downloads
date: 2006-02-27 14:42:54.000000000 -07:00
---

This page links to installers that will create a full, new Linux
installation.

For alternative installation methods, or instructions on installing these
files see: 
[Getting LinuxCNC](http://linuxcnc.org/docs/stable/html/getting-started/getting-linuxcnc.html)

## LinuxCNC 2.9 Downloads

LinuxCNC requires a realtime kernel if it is to be used to control machinery. 
There are two versions of the package, "linuxcnc-uspace" and "linuxcnc"

"linuxcnc-uspace" is compatible with the preempt-rt realtime kernel, which
is close to standard Linux. This version runs in userspace like most
other applications and will run with any preempt-rt kernel. 

"linuxcnc-uspace" will also run on a standard Linux kernel for use as a
simulator, but it should not be used to control hardware. 

"linuxcnc" (without a suffix) is a package which runs in kernel space 
and needs a specific RTAI kernel, which we also supply. (ie the exact
kernel version installed must match that which the package was built
against.) The RTAI kernel is available from the LinuxCNC software repository
and should be installed automatially as a dependency of the "linuxcnc" package.
In many cases the RTAI kernel will give better latency performance than
preempt-rt, but note that it is only parallel-port controlled systems
using software-based  stepping and/or encoder counting that need particularly
good latency performance 

It is also possible to run linuxcnc-uspace, in user-space, with the RTAI
kernel if the helper package "linuxcnc-uspace-rtai" is installed. This is
something of a half-way house between the other two versions. A similar
package can be built for the Xenomai realtime kernel, but is not available
as a pre-built package. 

The links below point to the latest released images. Older releases can still be
found [here](https://www.linuxcnc.org/iso/)

### LinuxCNC 2.9.8 Debian 13 Trixie PREEMPT-RT ISO

[Debian 13 Trixie PREEMPT-RT ISO](https://www.linuxcnc.org/iso/linuxcnc_2.9.8-amd64.hybrid.iso)
The Debian 13 Trixie ISO will install a full Debian system with the required
realtime kernel and the linuxcnc-uspace application. It uses a PREEMPT-RT
patched kernel  which is close to mainstream Linux but does not, in some
cases, give quite such good realtime performance as the previous RTAI
kernel. It is very often more than good enough. It should probably be
the first version tried even if using a parallel port.
This is compatible with all Mesa and Pico interface boards.

### LinuxCNC 2.9.8 Debian 13 Trixie RTAI

The more adventurous can install the Trixie ISO and then install the
experimental RTAI kernel as described in 
[2.9 documents](http://linuxcnc.org/docs/2.9/html/getting-started/getting-linuxcnc.html#cha:Installing-RTAI)
The kernel-mode RTAI installation can not be used with Mesa Ethernet-interfaced cards.
In addition to the RTAI kernel you will also need the rtai-modules package and the linuxcnc package. Both can
be downloaded by adding the linuxcnc 2.9-rt package repository as described in the link above. 


### LinuxCNC 2.9.8 Raspberry Pi 4/5 OS based on Debian Trixie

[Raspberry Pi 4/5 SD Card Image](https://www.linuxcnc.org/iso/image_2026-01-21-raspios-lcnc-2.9.8-trixie-arm64.zip)] (MD5SUM 705b7f3c2f7b385f6cb094d05e01070e)
Complete SD Card image for the Raspberry Pi 4/5 (It is not recommended to run LinuxCNC on the Pi3 or earlier) "Uspace" version compatible with Mesa Ethernet and SPI interface boards. The base install uses 6.5GB, but 16GB minimum SD card capacity is reoommended.

The .zip file is directly readable by the [Raspberry Pi imager application](https://www.raspberrypi.com/software/)
A setup wizard will run on startup to configure username, password, WiFi etc. 

More information on downloading and installing is in the
[LinuxCNC Documents](http://linuxcnc.org/docs/stable/html/getting-started/getting-linuxcnc.html)


## LinuxCNC Packages

LinuxCNC debian packages aka .deb files can be installed on a system with dpkg
from the command line or with GDebi as a graphical install method. You will need
to have a compatible realtime kernel to control machinery.

* [LinuxCNC Uspace 2.9.8 amd64 (PC)](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-uspace_2.9.8_amd64.deb)
* [LinuxCNC Uspace 2.9.8 arm64 (Pi)](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-arm64/linuxcnc-uspace_2.9.8_arm64.deb)
* LinuxCNC Docs [English](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-all/linuxcnc-doc-en_2.9.8_all.deb) - [Spanish](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-all/linuxcnc-doc-es_2.9.8_all.deb) - [French](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-all/linuxcnc-doc-fr_2.9.8_all.deb) - [German](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-all/linuxcnc-doc-de_2.9.8_all.deb) - [Chinese](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-all/linuxcnc-doc-zh-cn_2.9.8_all.deb)
* LinuxCNC Uspace 2.9.8 Dev Package [AMD64](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-uspace-dev_2.9.8_amd64.deb) - [ARM64](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-arm64/linuxcnc-uspace-dev_2.9.8_arm64.deb)

* [LinuxCNC package for RTAI kernel 5.4.279-rtai-amd64](https://www.linuxcnc.org/dists/trixie/2.9-rt/binary-amd64/linuxcnc_2.9.8_amd64.deb))
* [RTAI Kernel 5.4.279](https://www.linuxcnc.org/dists/trixie/base/binary-amd64/linux-image-5.4.279-rtai-amd64_5.4.279-rtai-amd64-1_amd64.deb)
* [RTAI modules](https://www.linuxcnc.org/dists/trixie/base/binary-amd64/rtai-modules-5.4.279_5.3.3-linuxcnc_amd64.deb)
* [Kernel Headers](https://www.linuxcnc.org/dists/trixie/base/binary-amd64/linux-headers-5.4.279-rtai-amd64_5.4.290-rtai-amd64-1_amd64.deb)

