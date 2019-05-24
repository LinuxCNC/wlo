---
layout: page
title: Downloads
navbar: true
joomla_id: 5
joomla_url: downloads
date: 2006-02-27 14:42:54.000000000 -07:00
---



## LinuxCNC 2.7 Downloads

The Debian 7 Wheezy ISO uses RTAI which LinuxCNC has used as the Realtime layer
since the very beginning. This gives the best real-time performance and is
generally a better choice for software stepping using a parallel port. However
making a stable version of a 4.x Kernel for Stretch (and eventually Buster) has
proven difficult, which is partly why we still distribute the EOL Wheezy. This
is compatable with Mesa PCI and PCIe and Pico interface boards but is not
compatable with Mesa Ethernet interface boards.

* LinuxCNC 2.7.14 [Debian 7 Wheezy](http://www.linuxcnc.org/iso/linuxcnc-2.7.14-wheezy.iso)

The Debian 9 Stretch ISO uses a PREEMPT-RT patch which is closer to mainstream
Linux but does not, in some cases, give quite such good realtime performance.
It is very often more than good enough. It should probably be the first version
tried even if using a parallel port. This is compatable with all Mesa and Pico
interface boards.

* LinuxCNC Uspace 2.7.0 [Debian 9 Stretch](http://www.linuxcnc.org/testing-stretch-rtpreempt/)

The LinuxCNC Buildbot builds several different versions of OS's and is the best
way to get the 2.8 (master) version. If you have a gantry type of machine the
2.8 supports dual motor gantry homing.

* [LinuxCNC Buildbot](http://buildbot.linuxcnc.org/)

More information on downloading and installing is in the
[LinuxCNC Documents](http://linuxcnc.org/docs/2.7/html/getting-started/getting-linuxcnc.html)


