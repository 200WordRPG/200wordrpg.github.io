---
layout: default
---

# 2017 Entries

## No entries yet! The challenge [hasn't started]({{site.baseurl}}/2017details)!

<p>
{% assign sorted_pages = (site.categories.2017 | sort: 'date') %}
  {% for post in sorted_pages %}
      <strong><a href="{{ post.url }}">
        {{ post.title }}
      </a> •</strong>
  {% endfor %}
</p>