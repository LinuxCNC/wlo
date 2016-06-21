---
layout: page
navbar: no
title: News
---

Do you have a machine or project you'd like to see featured on the showcase?
Post it in the [forum's "show your stuff" section][forum] or create an issue on
our [website's github repository][github].  Submissions should consist of at
least one photo or video, a short explanation, and include a link to the forum
or a personal blog with more information.

The showcase is not for promoting commercial products that use or include
LinuxCNC, it is for promoting things that the LinuxCNC software enables
our users to do.

 [github]: https://github.com/LinuxCNC/wlo/issues/new
 [forum]: https://forum.linuxcnc.org/forum/show-your-stuff

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
