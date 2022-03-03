---
layout: post
title: 'LinuxCNC is in Debian'
date: 2022-03-03 10:32:00.000 -07:00
---
[LinuxCNC has been accepted into the main Debian
distribution](https://packages.debian.org/linuxcnc-uspace).  This means it
is now possible to install a fully functioning LinuxCNC system, including
a [Preempt-RT realtime kernel](https://packages.debian.org/linux-image-rt)
suitable for running real hardware, entirely from official Debian package
repositories.

This is a huge milestone and I'm very grateful to Steffen Möller and
Petter Reinholdtsen from the Debian project for joining us and providing
extensive help and support in this effort.

LinuxCNC is currently in Debian's "unstable" distribution (aka "sid",
the kid who breaks your toys).  We're expecting to transition into
"testing" (aka "bookworm") in the next few days, and possibly into
"stable" ("bullseye") some time after that.

We at linuxcnc.org will continue to provide up-to-date packages for older
distributions (ie buster and older), and hopefully for newer distributions
at some point in the future.  You can continue to get the latest packages
from our [buildbot](http://buildbot.linuxcnc.org).

The version of LinuxCNC that got into Debian is our 2.9 *prerelease*,
from our experimental master branch.  We should look towards stabilizing
this branch and making a real 2.9 release (or 3.0, or something) this
spring and summer.  It will be relatively straight-forward to update the
version of LinuxCNC that's distributed by Debian, now that the initial
heavy lifting has been done.
