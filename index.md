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

* Full source code available under the terms of the [GNU GPLv2
  (General Public License version 2)][GPLv2].

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

[GPLv2]: http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
