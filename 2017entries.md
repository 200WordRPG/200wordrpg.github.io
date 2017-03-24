---
layout: default
---

# 2017 Entries

<h2>
  {% for post in site.categories.2017 %}
      <a href="{{ post.url }}">
        {{ post.title }}
      </a> • 
  {% endfor %}
</h2>