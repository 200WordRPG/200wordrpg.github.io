---
layout: default
---

# 2017 Entries

## No entries yet! The challenge [hasn't started]({{site.baseurl}}/2017details)!

<h2>
  {% for post in site.categories.2017 %}
      <a href="{{ post.url }}">
        {{ post.title }}
      </a> • 
  {% endfor %}
</h2>