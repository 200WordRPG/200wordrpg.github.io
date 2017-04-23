---
layout: default
title: News!
---

Testing to see if the automated news feed works!

<ul>
{% assign sorted_pages = (site.categories.news | sort: 'date') | reverse %}
  {% for page in sorted_pages %}
      <li><strong><a href="{{ page.url }}">
        {{ page.title }}
      </a></strong></li>
  {% endfor %}
</ul>