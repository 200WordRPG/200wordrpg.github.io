---
layout: default
---

# 2016 Entries

The 2016 challenge featured two categories: **Supplements** and **rpgs**. There were some incredible submissions in both categories, all of which are listed below.

<p>
{% assign sorted_pages = (site.categories.2016 | sort: 'title') %}
  {% for post in sorted_pages %}
      <strong>&emsp;•&emsp;<a href="{{ post.url }}">
        {{ post.title }}
      </a></strong>
  {% endfor %}
</p>
