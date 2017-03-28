---
layout: default
---

# 2016 Entries

All of the entries from the 2016 Challenge. Enjoy!

<p>
{% assign sorted_pages = (site.categories.2016 | sort: 'title') %}
  {% for post in sorted_pages %}
      <strong><a href="{{ post.url }}">
        {{ post.title }}
      </a>&emsp;•&emsp;</strong>
  {% endfor %}
</p>
