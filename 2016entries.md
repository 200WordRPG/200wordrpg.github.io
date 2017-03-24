---
layout: default
---

# 2016 Entries

All of the entries from the 2016 Challenge. Enjoy!

<h2>
  {% for post in site.categories.2016 %}
      <a href="{{ post.url }}">
        {{ post.title }}
      </a> • 
  {% endfor %}
</h2>