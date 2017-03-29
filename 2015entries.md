---
layout: default
---
# 2015 Entries

The 2015 Challenge allowed pictures and fancy layouts, so all of these entries are images, not text. Enjoy!

<p>
{% assign sorted_pages = (site.categories.2015 | sort: 'title') %}
  {% for post in sorted_pages %}
      <strong><a href="{{ post.url }}">
        {{ post.title }}
      </a>&emsp;•&emsp;</strong>
  {% endfor %}
</p>
