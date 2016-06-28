---
layout: post
title: 'Joints/Axes branch finally merged!'
date: 2016-06-27 18:41:00.000000-06:00
---
The joints-axes branch has been merged into the master branch!

Joints/axes was a project to separate "joints" (roughly: motors) from
"axes" (roughly: cartesian coordinates), in order to better support
machines where a single motor does not directly drive motion along
an axis, such as gantry machines, delta robots, robot arms, hexapods,
and similar.

Everyone running the development version of LinuxCNC (what's tentatively
called "2.8~pre") will be affected by this change.

This new separation of joints and axes requires changes to both .ini
and .hal config files.  In most cases your configuration will be
automatically upgraded when you try to open the config with the new
version.  Please report any config conversion failures on the [github
issue tracker][github], [in email][email], or [on the forum][forum],
so that the conversion script can be improved.

Details on the changes are in the documentation here:

http://linuxcnc.org/docs/devel/html/getting-started/updating-linuxcnc.html

Please keep an extra careful eye out for bugs and help us stabilize it
for the next release.

 [github]: https://github.com/LinuxCNC/linuxcnc/issues
 [email]: https://sourceforge.net/p/emc/mailman
 [forum]: http://forum.linuxcnc.org/
