---
layout: default
---
# 2015 Entries

The 2015 Challenge was the first year! We allowed pictures and fancy layouts, so all of these entries are images, not text, which makes them stand out from future entries.

<p>
{% assign sorted_pages = (site.categories.2015 | sort: 'title') %}
  {% for post in sorted_pages %}
      <strong>&emsp;•&emsp;<a href="{{ post.url }}">
        {{ post.title }}
      </a></strong>
  {% endfor %}
</p>
