---
layout: post
title: 'Report: LinuxCNC Meetup near Oslo'
date: 2025-07-12 23:33:00.000000000 +01:00
---

We just completed a LinuxCNC-intense weekend, kindly hosted by Petter in his shop near the Oslo airport and also kindly sponsored by [NUUG](https://www.nuug.no) and [Redpill-Linpro](https://www.redpill-linpro.com/en). 
Petter's shop is quite a mechanic's resort.

(If you are upset to have missed it, then it is very likely that the event will be repeated next year at around the same time)

One of the more tangible outcomes of our gathering is a decision to pimp our LinuxCNC gear - Dominic and Asle drafted an idea for LinuxCNC T-shirt. Please have a look at https://sprd.co/tdhbvfn (attention, not write-protected!) and send in your ideas to improve on it or links to alternative shirt designs. Impressive for all attendees was how Andy, René and Petter addressed the LinuxCNCification of Petter's retrofitted mill. Andy pulled an impressive collection of Mesa cards (for which he created many of the drivers) from his magic bag and in the end it was a custom firmware kindly provided by Mr. Mesa himself that optimized Petter's setup using three smart-serial Rx channels as differntial encoder inputs. 

One of the many side-projects over the weekend was the investigation how a LinuxCNC Live-USB stick could possibly be produced with the Live-Helper (https://live-team.pages.debian.net/live-manual/html/live-manual.en.html) tools of Debian. The real-time kernel is indeed provided, which was thought to be the largest hurdle. There is some hope that the Debian community could offer such an image directly. But the question is - which packages should be shipping with it? FreeCAD, basic UNIX bits, text editors, web browser, maybe all that is collected in https://blends.debian.org/3dprinter/tasks/cad, https://blends.debian.org/3dprinter/tasks/gcode, https://wiki.debian.org/DebianScience/Engineering, KiCad, ... we would like to start a discussion on this topic. The benefit for LinuxCNC to be shipping with a wider selection of tools is an increased awareness by other communities, and vice versa.

The documentation literally did not let us sleep too much. Weblate has a new champion, i.e. Tamil. The only concern is that the translations translate bits that should not be translated. Those bits likely should not be in weblate in the first place, but they are, and not straight-forward to exclude. It is mostly the `troff` text style instructions that are blocking po4a when syntactically challenging. We have some first scripts to detect such issues and set the .po entry to "fuzzy". But this will take some more iterations.

Discussion points at the meeting

Suggestions on how to improve the community experience
1. Revive our Video conferences (René, Steffen, Petter) - Steffen starts an invite, followed by René, Andy, Petter and Dominic
    Migrating to BigBlueButton on https://www.senfcall.de/.
    - Close gaps in communication between LinuxCNC forums and developers
    - Discuss upcoming development milestones
    + Integrating (or not) regular SmoothStepper
    + Custom firmware for SmoothStepper
2. LinuxCNC-gear (Steffen, René, Dominic
    Idea to find a site shipping directly that has a good quality
    * T-Shirts  (Link to a possible T-Shirt design: https://sprd.co/tdhbvfn // please comment - is this good in your opinion? - Dominic)
    * Stickers
3. Debian LiveCD with real-time kernel and LinuxCNC (plus usable CAD/CAM) - any volunteers?
4. Reference to local user groups
    - Hackspace in Hamburg (D) with Dominic
5. Translations - update with newer version of po4a (Petter, Steffen)
    - Fixed newline-error for false-positive itemizations 

How to improve our developers' experience
1. Documentation
   - Folks do not like to have a large repository with too many languages, especially so as only fragments tend to be translated
   - Unclear when and how the documentation on web page is updated

2. BuildBot2 to substitute BuildBot - The main buildbot can probably be retired, it is now only building for out-of-support OS variants. 

3. Have all HAL-pins implemented as 64bit (Andy)
    - Reduces complexity
    - No effect on real time computing
    - It is the HAL pins, not the internal compute of whatever complex data schemes LinuxCNC may be confronted with
    - Perfect compatibility with all existing HAL files (unlike the current situation in Master with both 32 and 64-bit pins treated separately)
    
4. Use Pybind11 to auto-derive Python wrappers of C++ code - Rene
    - https://github.com/pybind/pybind11 
    - Reduces some 2000+ lines of wrapper code to 85 lines
    
Features that LinuxCNC is missing (or not?)
1. Not: Embedded template library for real-time parts (Steffen)
    No dynamic memory is used in our real-time code

We had tons of joint discussions that not necessarily contributed to operational consequences but were always educational and something rubs off on whoever stands by or spans yet another discourse with a follow-up question. In our perpetual quest to identify and augment LinuxCNC's unique selling points, Andy pointed out that the motivation by NIST to come up with the LinuxCNC precursor EMC as to move from electronic black boxes that shipped with the machine to software and general computers. And they wanted a reference implementation for the G-code someone injected. While there was no alternative at the time, we now have many smaller microcontrollers that could interpret G-code. René then kindly reminded us that Jogging a mill would be not possible e.g. with GRBL because of ... and not trivial to add. And yes, for anything small that shall be moving in some well-defined manner, LinuxCNC is not required. But it gives flexibillity. The RPi is possibly important to help with any such transition. Mach 4 is seen, but not Open Source. LinuxCNC brings access to any level of detail of a machine as so desired, also during its run time - because it is Open Source and because of HAL..  Andy stressed that he wanted LinuxCNC to be more useful for those for whom LinuxCNC is already the best tool to use.

Another ongoing discussion is on Andy's intent to have HAL pins always as 64 bit, also if representing only a single bit to simplify everything. No internal data structure is affected. And it should not affect anything or anyone. Should. In an Open Source world it is just difficult to know what exactly is done in the field. This may be ameliorated by the idea is to improve the links between users (and devs with them) a bit more be restarting the Video meetings we once had not too long ago. Steffen volunteered to host the first, everyone strongly objecting the idea to have a single-individual hosting it, so we pass it around again.

René updated his patch introducing Pybind11 to semi-autmatically create Python interfaces for our C++ code. That reduces some 2000+ lines of code. Hm. The key drawback is that pins that never change, i.e. "parameters", would need to go. 

In the context of Petter getting a new VHDL-implemented firmware for the Xilinx chip on the Mesa card, René and Steffen revisited the Yosys website and found that it now supports Spartan 6 https://yosyshq.readthedocs.io/projects/yosys/en/0.46/cmd/synth_xilinx.html. And there is a plugin for GHDL (https://ghdl.free.fr/) for it. Seems like we are not too far away from producing the Mesa firmware with Open Source tools? Would anyone be up to investigate how far we can get already?




