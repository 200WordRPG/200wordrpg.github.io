---
layout: default
---
# 2015 Entries

The 2015 Challenge allowed images and fancy layouts, so all of these entries are images, not text. We are uploading them as fast as we can, but it might be a while before they are ALL here. Until then you can view all of the 2015 Winners, Finalists, and Entries [**here**](http://schirduans.com/david/2015/04/200-word-rpg-challenge.html)

<p>
{% assign sorted_pages = (site.categories.2015 | sort: 'title') %}
  {% for post in sorted_pages %}
      <strong><a href="{{ post.url }}">
        {{ post.title }}
      </a> •</strong>
  {% endfor %}
</p>