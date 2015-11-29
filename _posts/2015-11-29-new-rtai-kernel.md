---
layout: post
title: 'New RTAI kernel: Linux 3.16.7 with RTAI 5.0-test1'
date: 2015-11-29 10:33:31.000000000 -07:00
---
New RTAI kernel packages are available for Debian Jessie, based on Linux
3.16.7 and RTAI 5.0-test1.

This new realtime kernel is not ready for widespread deployment yet.
I'm soliciting early testing from developers and advanced users who
are comfortable manipulating apt sources, installing kernel packages,
and building linuxcnc from source.

In order to test it, you need to install
Jessie (i386) using the regular [debian.org
installer](http://cdimage.debian.org/debian-cd/8.2.0/i386/iso-cd/), add
"deb http://linuxcnc.org jessie base" to your sources.list, install the
linux-image and rtai-modules packages from there, and reboot.

There are no debian packages of LinuxCNC for this new platform yet, but
the branch "rtai-5" in our git repo works on it.

Report any results, success or failure, on IRC (#linuxcnc-devel) or on
the developers mailing list.
