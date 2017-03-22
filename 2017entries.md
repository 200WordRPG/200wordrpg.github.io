---
layout: default
---

# 2017 Entries

The 2017 challenge was the largest yet, featuring nearly 700 entries! They are all listed below, along with author comments. Enjoy!

{% assign sorted_pages = site.categories.2017 | sort:"title" %}
<table>{% for post in sorted_pages %}
  {% assign loopindex = forloop.index | modulo: 3 %}
  {% if loopindex == 1 %}
    <tr><td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% elsif loopindex == 0 %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td></tr>
  {% else %}
    <td id="entries"><strong><a href="{{ post.url }}">{{ post.title }}</a></strong></td>
  {% endif %}
 {% endfor %}
    {% if loopindex == 0 %}
    </table>
  {% else %}
    </tr></table>
  {% endif %}
