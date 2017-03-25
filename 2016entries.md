---
layout: default
---

# 2016 Entries

All of the entries from the 2016 Challenge. Enjoy!

<p>
  {% for post in site.categories.2016 %}
      <a href="{{ post.url }}">
        {{ post.title }}
      </a> • 
  {% endfor %}
</p>