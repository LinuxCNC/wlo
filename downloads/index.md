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
against.) At the present moment we do not have a linuxcnc package
available for the RTAI kernel, but it is possible to build from source. 
The RTAI kernel is available from the LinuxCNC software repository, however.
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

* LinuxCNC 2.9.1 [Debian 12 Bookworm PREEMPT-RT ISO](https://www.linuxcnc.org/iso/linuxcnc_2.9.1-amd64.hybrid.iso)

The Debian 12 Bookworm ISO will install a full Debian system with the required
realtime kernel and the linuxcnc-uspace application. It uses a PREEMPT-RT
patched kernel  which is close to mainstream Linux but does not, in some
cases, give quite such good realtime performance as the previous RTAI
kernel. It is very often more than good enough. It should probably be
the first version tried even if using a parallel port.
This is compatible with all Mesa and Pico interface boards.

* LinuxCNC 2.8.4 Debian 10 Buster RTAI

The more adventurous can install the Bookworm ISO and then install the
experimental RTAI kernel as described in 
[2.9 documents](http://linuxcnc.org/docs/2.9/html/getting-started/getting-linuxcnc.html#cha:Installing-RTAI)
The kernel-mode RTAI installation can not be used with Mesa Ethernet-interfaced cards.
There is not currently a packaged LinuxCNC application image for RTAI (work in progress) but
building from source is supported and working. 


* LinuxCNC 2.9.1 [Raspberry Pi OS based on Debian 12 Bookworm](https://www.linuxcnc.org/iso/linuxcnc-2.9.1-bookworm-rpi4.img.xz)

Raspberry Pi 4 Uspace compatible with Mesa Ethernet and SPI interface boards.
This .xz file is directly readable by the [Raspberry Pi imager application](https://www.raspberrypi.com/software/)


Regular development builds (several times a day) can be found here. 
* [LinuxCNC Buildbot](http://buildbot.linuxcnc.org/)

More information on downloading and installing is in the
[LinuxCNC Documents](http://linuxcnc.org/docs/stable/html/getting-started/getting-linuxcnc.html)


## LinuxCNC Packages

LinuxCNC debian packages aka .deb files can be installed on a system with dpkg
from the command line or with GDebi as a graphical install method. You will need
to have a compatible realtime kernel to control machinery.

* [LinuxCNC Uspace 2.9.1 64bit](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-uspace_2.9.1_amd64.deb)
* [LinuxCNC Uspace 2.9.1 arm64](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-arm64/linuxcnc-uspace_2.9.1_arm64.deb)
* LinuxCNC Docs [English](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-doc-en_2.9.1_all.deb) [Spanish](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-doc-es_2.9.1_all.deb) [French](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-doc-fr_2.9.1_all.deb) [German](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-doc-de_2.9.1_all.deb) [Chinese](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-doc-zh-cn_2.9.1_all.deb)
* [LinuxCNC Uspace 2.9.1 Dev AMD64](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-amd64/linuxcnc-uspace-dev_2.9.1_amd64.deb) [ARM64](https://www.linuxcnc.org/dists/bookworm/2.9-uspace/binary-arm64/linuxcnc-uspace-dev_2.9.1_arm64.deb)

* [RTAI Kernel 5.4.258](https://www.linuxcnc.org/dists/bookworm/base/binary-amd64/linux-image-5.4.258-rtai-amd64_5.4.258-rtai-amd64-2_amd64.deb)
* [RTAI modules](https://www.linuxcnc.org/dists/bookworm/base/binary-amd64/rtai-modules-5.4.258_5.3.3-linuxcnc-delta_amd64.deb)

The following are work-in-progress and should follow in a few weeks (after 29 Oct 2023)
* [LinuxCNC RTAI 2.8.4 for kernel 4.9.195](https://www.linuxcnc.org/dists/buster/2.8-rt/binary-amd64/linuxcnc_2.8.4_amd64.deb)
* [LinuxCNC uspace helper for RTAI kernel](https://www.linuxcnc.org/dists/buster/2.8-rtpreempt/binary-amd64/linuxcnc-uspace-rtai_2.8.4_amd64.deb)
