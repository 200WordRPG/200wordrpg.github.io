---
layout: default
---

# 2017 Entries

Submissions are open until April 23rd! [Click for Submission Form]({{site.baseurl}}/2017submission)

I'm posting them up as fast as I can, but don't panic if it takes a day or two before your entry is on this list. Entries are listed in the order that they were submitted.

<p>
{% assign sorted_pages = (site.categories.2017 | sort: 'date') %}
  {% for post in sorted_pages %}
      <strong><a href="{{ post.url }}">
        {{ post.title }}
      </a>&emsp;•&emsp;</strong>
  {% endfor %}
</p>

