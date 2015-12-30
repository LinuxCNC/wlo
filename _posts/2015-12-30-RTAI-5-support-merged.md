---
layout: post
title: 'RTAI 5.0 support merged'
date: 2015-12-30 12:11:50.000000000 -07:00
---
Support for RTAI 5 has been merged into LinuxCNC 2.7 (and into the
"master" development branch).

RTAI kernel packages are available for Debian Jessie, based on Linux
3.16.7 and RTAI 5.0-test1.  At this time only i386 (686-pae) is supported,
we're still having trouble with amd64.

In order to use it, you need to install
Jessie (i386) using the regular [debian.org
installer](http://cdimage.debian.org/debian-cd/8.2.0/i386/iso-cd/), add
"deb http://linuxcnc.org jessie base" to your sources.list, install the
linux-image and rtai-modules packages from there, and reboot.

There are debian packages of LinuxCNC available from the
[buildbot](http://buildbot.linuxcnc.org/index.html) for this new platform,
for 2.7 and master (the development branch).
