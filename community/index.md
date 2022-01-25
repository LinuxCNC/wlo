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
  The chat is [logged](http://tom-itx.no-ip.biz:81/~tom-itx/irc/libera/logs/%23linuxcnc-devel/index.html) by community member Tom L., and historical logs from freenode are [also available](http://tom-itx.no-ip.biz:81/~tom-itx/irc/logs/%23linuxcnc-devel/index.html).

## Related products

LinuxCNC or its derivatives are not the only CNC motion controllers.
There are many alternatives - coming in all shades from very Open Source to stricly commercial.
Also, all these CNC controllers will likely be embedded in larger workflows for which these are post-processors of data from CAD/CAM software.
And every piece of software has its very own community.

### Simulators

 * [CAMotics](https://camotics.org/) shows how G-code is executed

### CNC controllers

Controlling the motors themselves, access steppers/servos (or their drivers) directly or via non-intelligent cards like EtherCat or parallel ports.

 * [GRBL](https://github.com/gnea/grbl) OpenSource, for use on Arduino
 * [LinuxCNC](https://www.linuxcnc.org) OpenSource, for Linux, low-latency with real-time kernel
 * [Mach3](https://www.machsupport.com/software/mach3/) non-free, low-cost, for Windows
 * [Mach4](https://www.machsupport.com/software/mach4/) non-free, low-cost, for Windows
 * [Marlin](https://marlinfw.org/) Open Source, for use on Arduino or the [BigTreeTech GRC](https://www.biqu.equipment/de/products/bigtreetech-gtr-v1-0-bigtreetech-m5-v1-0-11-axis-3d-printer-motherboard)
 * [KMotion](https://www.dynomotion.com/software.html)
 * [OpenBuilds CONTROL](https://software.openbuilds.com/#) OpenSource
 * [RoboticSys](https://roboticsys.com/rmp-ethercat-motion-controller/)
 * [TurboCNC](http://www.dakeng.com/turbo.html) OpenSource, for DOS

In need of specialized hardware

 * [Acorn CNC](https://www.centroidcnc.com/centroid_diy/acorn_cnc_controller.html) non-free, low-cost, for Windows
 * [Duet](https://www.duet3d.com/) Open Source, connects via SPI to an RPi or also features its own web interface.
   Board includes drivers for steppers, under control of a modern TMC5160 chip.
   Provides its own G-code interface, with changes for adapting [from a 3D Printing background to CNC](https://duet3d.dozuki.com/Wiki/Configuring_RepRapFirmware_for_a_CNC_machine).
 * [Drufel](https://drufelcnc.com)
 * [Estlcam](https://estlcam.de/) hardware is Open Source, software not, for Windows
 * [EdingCNC](https://edingcnc.com)
 * [KineticNC](https://www.cnc-step.de/cnc-software/kinetic-nc-netzwerk-steuerungssoftware/) from CNC-STEP needs ZERO-3 interface
 * [nccad](http://www.max-computer.de/x5e/index.html) non-free, for Windows
 * [ShopBot](https://www.shopbottools.com/support/control-software) needs a Control-Box

High-end
 
 * [Fanuc](https://www.fanuc.eu/de/de/cnc/cnc-system)
 * [Heidenhein](https://www.heidenhain.de/)
 * [Isel](https://www.isel.com) [Remote-NC](https://www.isel.com/de/remote-nc.html) and [Pal-PC](https://www.isel.com/de/pal-pc.html)
 * [Sinumerik](https://new.siemens.com/de/de/produkte/automatisierung/systeme/cnc-sinumerik/cnc-steuerungen.html)


### CAM
 
Contol an interface that interprets its output, likely G-code, with no direct contact to the machine performing the milling

 * [Alibre](https://www.alibre.com/)
 * [Aspire](https://www.cnc-step.de/cnc-software/aspire/)
 * [BlenderCAM](https://github.com/vilemduha/blendercam/wiki) OpenSource
 * [BobCAD-CAM](https://bobcad.com/) non-free CAM modules for SolidWorks
 * [CamBam](http://www.cambam.co.uk/) non-free
 * [DeskCNC](http://www.deskcnc.com/Features.html) non-free
 * [Dolphin](https://www.dolphincadcam.com/) non-free
 * [EdgeCAM](https://www.edgecam.com/)
 * [Estlcam](https://estlcam.de/)
 * [Fusion360](https://www.autodesk.com) non-free
 * [FreeMill](https://mecsoft.com/freemill/) free
 * [GibbsCAM](https://www.gibbscam.com/)
 * [MasterCAM](https://www.mastercam.com/)
 * [MeshCAM](http://www.grzsoftware.com/)
 * [nccad](http://www.max-computer.de/x5e/index.html)
 * [OpenBuilds CAM](https://software.openbuilds.com/#)
 * [OpenCAMLib](https://github.com/aewallin/opencamlib) OpenSource Python library to generate toolpaths, compatible with BlenderCAM
 * [OneCNC](https://onecnc.net/) non-free
 * [SprutCAM](https://sprutcam.com/) non-free
 * [VisualCADCAM](https://mecsoft.com/visualcadcam/) non-free
 * [WinPC-NC](https://www.lewetz.de/de/sample-sites-2/winpc-nc/uebersicht)

### CAD

Software that crafts something from which then CAM can generate G-code

 * [AutoCAD](https://www.autodesk.com/products/autocad/overview) non-free
 * [Blender](https://www.blender.org/) OpenSource, known for the nice movies
 * [BobCAD-CAM](https://bobcad.com/products/cad-design-software) non-free CAM modules for SolidWorks
 * [CorelCAD](https://www.coreldraw.com/en/product/corel-cad/) for Windows and Mac
 * [DesKAM](http://www.deskam.com/) non-free Windows for engraving
 * [Dolphin](https://www.dolphincadcam.com/) non-free
 * [FreeCAD](https://www.freecad.org) OpenSource
 * [Fusion360](https://www.autodesk.com) non-free
 * [Moi](http://moi3d.com/) non-free
 * [nccad](http://www.max-computer.de/x5e/index.html)
 * [OneCNC](https://onecnc.net/) non-free
 * [Rhino](https://www.rhino3d.com/) non-free for Windows and Mac
 * [SketchUp](http://sketchup.google.com/) non-free
 * [SolidEdge](https://solidedge.siemens.com/) non-free
 * [SolidWorks](https://www.solidworks.com/) non-free, low-cost entry price, physics simulations
 * [TinkerCAD](https://www.tinkercad.com/) free as in beer, web-only
 * [TrueSpace](https://download.cnet.com/TrueSpace/3000-6677_4-10187286.html) free as in beer
 * [TurboCAD](https://www.turbocad.com/) non-free
 * [VisualCADCAM](https://mecsoft.com/visualcadcam/) non-free
 * [Wings 3D](http://www.wings3d.com/) Open Source
