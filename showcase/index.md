---
layout: page
navbar: no
title: News
---

<div class="home">

  <h1>All Showcase</h1>

  <ul class="posts">
    {% for post in site.showcase %}
      <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/showcase.xml" | prepend: site.baseurl }}">via RSS</a></p>

</div>
