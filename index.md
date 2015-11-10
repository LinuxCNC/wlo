---
layout: page
---

{% if site.data.version %}<!-- site built from {{ site.data.version }} -->{% endif %}

<div><img src="images/linuxcnc-screenshot-small.png" border="0" alt="" style="float:right"/></div>

LinuxCNC controls CNC machines.  It can drive milling machines, lathes, 3d
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

* Full source code available under under the terms of the [GNU GPLv2
  (General Public License version 2)][GPLv2].

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
