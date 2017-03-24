---
layout: default
---

# 2016 Entries

Here are the entries from the 2016 Challenge, listed in alphabetical order. Enjoy!

<h3>
  {% for post in site.categories.2016 %}
      <a href="{{ post.url }}">
        {{ post.title }}
      </a> • 
  {% endfor %}
</h3>