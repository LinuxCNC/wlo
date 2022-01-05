---
layout: page
title: Community
navbar: true
joomla_id: 4
joomla_url: community
date: 2006-02-27 14:42:54.000000000 -07:00
---

<center><em>
All interactions in the LinuxCNC community are governed by the <a href="/CODE_OF_CONDUCT/">Code of Conduct</a>
</em></center>

## Users

<center><em>
Use these methods for help setting up and using LinuxCNC, and for general
CNC topics.
</em></center>

* The LinuxCNC [Forum](https://forum.linuxcnc.org/) is a user maintained
  place to discuss LinuxCNC.

* There is a [users' mailing
  list](http://lists.sourceforge.net/lists/listinfo/emc-users) hosted
  and [archived](https://sourceforge.net/p/emc/mailman/emc-users/)
  at SourceForge.

* Our primary real-time chat is in the *#linuxcnc* channel on [irc.libera.chat](https://libera.chat).
  You can use [web chat](https://web.libera.chat/#linuxcnc) or
  [connect with your own client](https://libera.chat/guides/connect).
  The chat is [logged](http://tom-itx.no-ip.biz:81/~tom-itx/irc/logs/%23linuxcnc/index.html) by
  community member Tom L. Logs can be accessed on the IRC with `log` for todays
  log or `index` for the calendar index.
  
* A community member has registered a Matrix room, [#LCNC:matrix.org (link joins via riot.im)](https://riot.im/app/#/room/#LCNC:matrix.org). This room is bridged to the libera.chat *#linuxcnc* channel.

* A community member has created a [Discord](https://discord.gg/SbskPKPJc6) server.

* The LinuxCNC [Wiki](http://wiki.linuxcnc.org/cgi-bin/emcinfo.pl)
  contains a wealth of user contributed information about LinuxCNC and
  CNC in general.

* [Issues](https://github.com/LinuxCNC/linuxcnc/issues) and [Pull Requests](https://github.com/LinuxCNC/linuxcnc/pulls) are handled by github.

* Translations of software and documentation are a [community effort on weblate](https://hosted.weblate.org/languages/de/linuxcnc/).


## Developers

<center><em>
Use these methods to contribute to the development of LinuxCNC, including
documentation, translation, new drivers and components.
</em></center>

* Learn more about [Contributing to
LinuxCNC](/docs/html/code/contributing-to-linuxcnc.html).

* The primary means of communication is the [developers' mailing
  list](http://lists.sourceforge.net/lists/listinfo/emc-developers) hosted
  and [archived](https://sourceforge.net/p/emc/mailman/emc-developers/)
  at SourceForge.

* Our primary real-time chat is in the *#linuxcnc-devel* channel on [irc.libera.chat](https://libera.chat).
  You can use [web chat](https://web.libera.chat/) or
  [connect with your own client](https://libera.chat/guides/connect).
  The chat is [logged](http://tom-itx.no-ip.biz:81/~tom-itx/irc/logs/%23linuxcnc-devel/index.html) by community member Tom L.
  The chat is [logged](http://tom-itx.no-ip.biz:81/~tom-itx/irc/libera/logs/%23linuxcnc-devel/index.html) by community member Tom L., and historical logs from freenode are [also available](http://tom-itx.no-ip.biz:81/~tom-itx/irc/logs/%23linuxcnc-devel/index.html).

## Forks

LinuxCNC has spawned derivative projects. You may be interested to learn about what is different to LinuxCNC with
 * [OpenCN](https://mecatronyx.gitlab.io/opencnc/opencn/)
   - Different trajectory planner with focus on minimal variation of force imposed on spindle
   - [Asymmetric Multi-Processing](https://mecatronyx.gitlab.io/opencnc/opencn/architecture/architecture.html) (AMP) assigns individual CPU cores to particular functions to single-out one core with hard realtime activities that is not affected by the Linux kernel's soft interrupts
 * [MachineKit](https://www.machinekit.io/) - expected to appeal more to developers
   - Trying to decouple the parts into isolated functional blocks: The focus is no longer the CNC controller, but the CNC is just one application.
     There is - for example - the [hal\_ros\_control](github.com/tormach/hal_ros_control) for connecting to the [Robot Operating System](https://www.ros.org/).
   - The Machinetalk remote communication protocol
   - Different (some may say "more clear") repository structure
 * ? Contact us for what we are missing.

Forks are much appreciated as a means to tailor LinuxCNC to the needs of our users.
And forks foster steady improvements as all forks compete for eyeballs, ideas and implementations.

Please inform us about projects that should be added to this list.
