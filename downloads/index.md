---
layout: page
title: Downloads
navbar: true
joomla_id: 5
joomla_url: downloads
date: 2006-02-27 14:42:54.000000000 -07:00
---

## LinuxCNC 2.8 Downloads

* LinuxCNC 2.8.0 [Debian 10 Buster PREEMPT-RT ISO](http://www.linuxcnc.org/iso/linuxcnc-2.8.0-buster.iso)

The Debian 10 Buster ISO uses a PREEMPT-RT patch which is close to mainstream
Linux but does not, in some cases, give quite such good realtime performance as
the previous RTAI kernel. It is very often more than good enough. It should
probably be the first version tried even if using a parallel port.
This is compatible with all Mesa and Pico interface boards.

* LinuxCNC 2.8.0 Debian 7 Wheezy RTAI

Users requiring a known-stable RTAI installation can install the
[Debian 7 Wheezy ISO](http://www.linuxcnc.org/iso/linuxcnc-2.7.14-wheezy.iso)
and then upgrade as described in 
[2.8 documents](http://linuxcnc.org/docs/2.8/html/getting-started/updating-linuxcnc.html).

* LinuxCNC 2.8.0 Debian 10 Buster RTAI

The more adventurous can install the Buster ISO and then install the
experimental RTAI kernel as described in 
[2.8 documents](http://linuxcnc.org/docs/2.8/html/getting-started/getting-linuxcnc.html#cha:Installing-RTAI)

* LinuxCNC 2.8.1 [Raspberry Pi OS based on Debian 10 Buster](https://www.linuxcnc.org/iso/linuxcnc-2.8.1-pi4.zip)

Raspberry Pi 4 Uspace compatable with Mesa Ethernet and SPI interface boards.

## LinuxCNC 2.7 Downloads

The Debian 7 Wheezy ISO uses RTAI which LinuxCNC has used as the Realtime layer
since the very beginning. This gives the best real-time performance and is
generally a better choice for software stepping using a parallel port. However
making a stable version of a 4.x Kernel for Stretch (and eventually Buster) has
proven difficult, which is partly why we still distribute the EOL Wheezy. This
is compatible with Mesa PCI and PCIe and Pico interface boards but is not
compatable with Mesa Ethernet interface boards.

* LinuxCNC 2.7.14 [Debian 7 Wheezy](http://www.linuxcnc.org/iso/linuxcnc-2.7.14-wheezy.iso)

The Debian 9 Stretch ISO uses a PREEMPT-RT patch which is closer to mainstream
Linux but does not, in some cases, give quite such good realtime performance.
It is very often more than good enough. It should probably be the first version
tried even if using a parallel port. This is compatible with all Mesa and Pico
interface boards.

* LinuxCNC Uspace 2.7.0 [Debian 9 Stretch](http://www.linuxcnc.org/testing-stretch-rtpreempt/)

The LinuxCNC Buildbot builds several different versions of OS's and is the best
way to get the 2.8 (master) version. If you have a gantry type of machine the
2.8 supports dual motor gantry homing.

* [LinuxCNC Buildbot](http://buildbot.linuxcnc.org/)

More information on downloading and installing is in the
[LinuxCNC Documents](http://linuxcnc.org/docs/2.7/html/getting-started/getting-linuxcnc.html)


## LinuxCNC Packages

LinuxCNC debian packages aka .deb files can be installed on a system with dpkg
from the command line or with GDebi as a graphical install method. You will need
to have a Preempt RT kernel to run Uspace.

* [LinuxCNC Uspace 2.8.1 64bit](https://www.linuxcnc.org/dists/buster/2.8-rtpreempt/binary-amd64/linuxcnc-uspace_2.8.1_amd64.deb)

* [LinuxCNC Uspace 2.8.1 32bit](https://www.linuxcnc.org/dists/buster/2.8-rtpreempt/binary-i386/linuxcnc-uspace_2.8.1_i386.deb)
* 
* [LinuxCNC Uspace 2.8.1 armhf](https://www.linuxcnc.org/dists/buster/2.8-rtpreempt/binary-armhf/linuxcnc-uspace_2.8.1_armhf.deb)

* [LinuxCNC Uspace 2.8.1 Docs](https://www.linuxcnc.org/dists/buster/2.8-rtpreempt/binary-amd64/linuxcnc-doc-en_2.8.1_all.deb)

* [LinuxCNC Uspace 2.8.1 Dev](https://www.linuxcnc.org/dists/buster/2.8-rtpreempt/binary-amd64/linuxcnc-uspace-dev_2.8.1_amd64.deb)
