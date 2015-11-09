---
layout: default
---

<div><img src="images/screen_thumb.png" border="0"
  alt=" " width="350" height="250" style="float:right" /></div>
Welcome to the home of **LinuxCNC**.

LinuxCNC is Free software licensed under the terms of the [GNU
GPLv2 (General Public License version 2][GPLv2] for realtime control of 
machines such as milling machines, lathes, plasma cutters, cutting machines,
robots, hexapods, etc.

Our community-maintained [wiki][wiki] contains lots of information and examples about configuration and using LinuxCNC.

LinuxCNC uses a Hardware Abstraction layer that allows you to adapt it to many
kinds of machinery, and includes a software PLC controller and an advanced
trajectory planner.

Note: Do Not upgrade the Linux operating system from the installed version as it will prevent LinuxCNC from working as a specific kernel is required.

# News

  <ul class="posts">
    {% for post in site.posts limit:4 %}
      <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>

 [GPLv2]: http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
 [wiki]: http://wiki.linuxcnc.org/
