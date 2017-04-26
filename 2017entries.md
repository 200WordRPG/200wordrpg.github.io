---
layout: default
---

# 2017 Entries

The 2017 challenge was the largest yet, featuring nearly 700 entries! They are all listed below, along with author comments. Enjoy!

<p>
{% assign sorted_pages = (site.categories.2017 | sort: 'title') %}
  {% for post in sorted_pages %}
      <strong><a href="{{ post.url }}">
        {{ post.title }}
      </a>&emsp;•&emsp;</strong>
  {% endfor %}
</p>