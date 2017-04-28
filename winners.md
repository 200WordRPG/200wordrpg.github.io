---
layout: default
---

# Winners
Chosen by the [Judges]({{site.baseurl}}/judges), these entries were particularly creative and engaging! There are no 1st, 2nd, or 3rd places, only top three winners in no particular order.

### 2017: Winners will be announced May 8th!

### 2016 RPGs: [Deconstruction]({{site.baseurl}}{% post_url 2016-04-12-Deconstruction %}) • [Stardust]({{site.baseurl}}{% post_url 2016-04-09-Stardust %}) • [Time Travel Thaw]({{site.baseurl}}{% post_url 2016-04-14-TimeTravelThaw %})
 
### 2016 Supplements: [The College Animalia]({{site.baseurl}}{% post_url 2016-04-06-TheCollegeAnimalia %}) • [First Steps]({{site.baseurl}}{% post_url 2016-04-17-FirstStepsAdventuringWorkshop %}) • [Foam Dart RPG]({{site.baseurl}}{% post_url 2016-04-07-FoamDartRPG %})

### 2015: [All Fall Down]({{site.baseurl}}{% post_url 2015-04-01-AllFallDown %}) • [Escape Pod One]({{site.baseurl}}{% post_url 2015-04-01-EscapePodOne %}) • [LOVEINT]({{site.baseurl}}{% post_url /2015/2015-04-01-LOVEINT %})

# 2017 Finalists 
[Will be announced soon!](https://200wordrpg.github.io/news/2017/04/24/submissionsclosed.html)

# 2016 Finalists
Entries selected by a [panel of judges]({{site.baseurl}}/judges) from the 2016 Challenge.

<p>
{% assign sorted_pages = (site.categories.finalist | sort: 'title') %}
  {% for post in sorted_pages %}
    {% if post.categories contains '2016' %}
      <strong><a href="{{ post.url }}">
        {{ post.title }}
      </a>&emsp;•&emsp;</strong>
        {% endif %}
  {% endfor %}
</p>

# 2015 Finalists
Entries selected by a [panel of judges]({{site.baseurl}}/judges) from the 2015 Challenge.

<p>
{% assign sorted_pages = (site.categories.finalist | sort: 'title') %}
  {% for post in sorted_pages %}
    {% if post.categories contains '2015' %}
      <strong><a href="{{ post.url }}">
        {{ post.title }}
      </a>&emsp;•&emsp;</strong>
        {% endif %}
  {% endfor %}
</p>
