---
layout: page
title: LinuxCNC
---

{% if site.data.version %}<!-- site built from {{ site.data.version }} -->{% endif %}

<div><img src="images/screen_thumb.png" border="0" alt=" " width="350"
height="250" style="float:right" /></div>

LinuxCNC controls CNC machines. It can drive milling machines, lathes, 3D
printers, laser cutters, plasma cutters, robot arms, hexapods, and more.

* Runs under Linux (optionally with realtime extensions).

* Simple installation on Debian and Ubuntu, or via our Live/Install
  DVD/USB images.

* Accepts G-code input, drives CNC machines in response.

* Active user community.

* Several different GUIs available.

* Compatible with many popular machine control hardware interfaces.

* Supports rigid tapping, cutter compensation, and many other advanced
  control features.

* Full source code available under the terms of the GNU <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">GPLv2 (General Public License version 2)</a>

<table width="100%">
<colgroup>
<col width="45%" />
<col width="10%" />
<col width="45%" />
</colgroup>
<tbody>
<tr>
<td valign=top>
<h2>CAD</h2>

The Computer-Aided Design (CAD) is typically the initiation of a project that involves LinuxCNC. It provides a static picture of what shall be produced and describes this in a 2D or 3D model. A series of Open Source tools are available to craft a design, like<br>

* FreeCAD<br>
* Blender<br>
* Inkscape<br>
* ...<br>

but Linux is also compatible with all commercial software solutions like<br>

* SolidWorkds<br>
* Fusion360<br>
* ...<br>

LinuxCNC does not know how its input is generated. Also, it does not do any planning. If your machine needs to react to changes in the environment while it is running, then you want to look into robotics libraries to substitute what CAD and CAM are providing. But you can still use LinuxCNC to control the machine and read out data from it - all in real time.
</td>
<td valign=center align=center> -> </td>
<td valign=top>
<h2>CAM</h2>

Computer-Aided Manufactoring (CAM) reads the design and knows hot to get the work done. This involves<br>

* what tool to use for what metal with what speed and what depth<br>
* along what coordinates<br>

Much of that process is automated. But CAM has no cameras, i.e. it does not know what dimensions that block of material has that is in the machine. The output of CAM is a file that LinuxCNC can understand, typically this is G-Code. Some CAD tools also help with CAM, in the Open Source world this typically is

* FreeCAD.

but any tool providing G-Code will be fine. It should be noted that CAM already needs to know about the functionality of the machine. The tools available for one, but also the number of axes that are available for the processing.
</td>
</tr>
<tr><td colspan=2></td><td align=center valign=center>|<br>v</td></tr>
<tr>
<td colspan=3>
<h2>LinuxCNC</h2>
LinuxCNC comes to play once all instructions what traces to follow with what tool at what speed are known and now LinuxCNC becomes the operator of the machine to actually perform the work.
This involves prepatory processes like<br>

* the homing of the machine to specific coordinates<br>
* calibration to matche distances to the number of steps on a motor or the pulse width for a servo<br>
* error correction to compensate e.g. for a backlash and/or latencies in the communication<br>

Together with its GUI, LinuxCNC nicely substitutes the control units one finds attached to the side of CNC lathes or mills, with extra flexibility for customisations, you can log in remotely, and script it.
</td>
</tr>
<tr>
<td align=center><br>^<br>|</td>
<td></td>
<td align=center><br>^<br>|</td>
</tr>
<tr>
<td valign=top><h2>Control panel</h2>
A monitor attached to the computer running LinuxCNC may well substitute the CNC control panel that originally shipped with a machine, like a SINUMERIK, Heinzmann, Heidenhain, Rexroth - you name them. That said, older CNC panels have their own historic value we encourage their maintenance if that is an option for a retrofit.
The LinuxCNC GUI can be modified to present custom data on the screen, e.g. from additional sensors. And scripts performing the execution can be made dependent on these data.
</td>
<td></td>
<td valign=top><h2>Machine</h2>
There is no conceptional constraint on what machines can be controlled with LinuxCNC. With its real-time functionality, LinuxCNC reacts as fast as computers can react and can be programmed to anticipate the position of the machine in the future to coordinate all axes in a timely manner for best precision.
<br>
Communication with the machine is likely bidirectional. Emergency stop, end switches - a series of sensors are typically built into machines that can be read-out and presented back to LinuxCNC, which reacts to it and updates the control panel, too.
</td>
</tr>
</tbody>
</table>

<div id="site-news">
  <h1>News</h1>
  <ul class="posts">
    {% for post in site.posts limit:10 %}
      <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </li>
    {% endfor %}
      <li><a class="post-link" href="news/">Older news…</a></li>
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>
</div>

<div class="posts" id="site-showcase">
  <h1>Showcases</h1>
    {% comment %}
        A bug in liquid means you have to do this dance to reverse and
        limit or offset a list. There is no fix upstream for it due to backwards
        compatibility concerns. https://github.com/Shopify/liquid/pull/456
    {% endcomment %}
    {% assign showcase = site.showcase | sort: 'date' | reverse %}
  {% for post in showcase reversed limit:1 %}
    <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
    <h2>
      <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">
        {{ post.title }}
      </a>
    </h2>
    <div class="content">
    {{post.content | markdownify }}
    </div>
  {% endfor %}
  <ul class="posts">
    {% for post in showcase limit:4 offset:1 %}
      <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </li>
    {% endfor %}
      <li><a class="post-link" href="showcase/">Older showcases…</a></li>
  </ul>
  <p class="rss-subscribe">subscribe to Showcases <a href="{{ "/showcase.xml" | prepend: site.baseurl }}">via RSS</a></p>
</div>
