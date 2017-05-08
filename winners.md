---
layout: default
---

# Winners
Chosen by the [Judges]({{site.baseurl}}/judges), these entries were particularly creative and engaging! There are no 1st, 2nd, or 3rd places, only top three winners in no particular order.

### **2017** :&emsp;[MECHANICAL ORYX]({{site.baseurl}}{% post_url 2017-04-15-MECHANICALORYX %})&emsp;•&emsp;[Memories]({{site.baseurl}}{% post_url 2017-04-21-Memories %})&emsp;•&emsp;[Route Clearance]({{site.baseurl}}{% post_url 2017-04-22-RouteClearance %})

### **2016** RPGs:&emsp;[Deconstruction]({{site.baseurl}}{% post_url 2016-04-12-Deconstruction %})&emsp;•&emsp;[Stardust]({{site.baseurl}}{% post_url 2016-04-09-Stardust %})&emsp;•&emsp;[Time Travel Thaw]({{site.baseurl}}{% post_url 2016-04-14-TimeTravelThaw %})
 
### **2016** Supplements:&emsp;[The College Animalia]({{site.baseurl}}{% post_url 2016-04-06-TheCollegeAnimalia %})&emsp;•&emsp;[First Steps]({{site.baseurl}}{% post_url 2016-04-17-FirstStepsAdventuringWorkshop %})&emsp;•&emsp;[Foam Dart RPG]({{site.baseurl}}{% post_url 2016-04-07-FoamDartRPG %})

### **2015**:&emsp;[All Fall Down]({{site.baseurl}}{% post_url 2015-04-01-AllFallDown %})&emsp;•&emsp;[Escape Pod One]({{site.baseurl}}{% post_url 2015-04-01-EscapePodOne %})&emsp;•&emsp;[LOVEINT]({{site.baseurl}}{% post_url /2015/2015-04-01-LOVEINT %})

<hr>

# 2017 Finalists
Out of nearly 700 entries, these were chosen by a [panel of judges]({{site.baseurl}}/judges) to be among the best of 2017:

<p>
{% assign sorted_pages = (site.categories.finalist | sort: 'title') %}
  {% for post in sorted_pages %}
    {% if post.categories contains '2017' %}
      <strong>&emsp;•&emsp;<a href="{{ post.url }}">
        {{ post.title }}
      </a></strong>
        {% endif %}
  {% endfor %}
</p>

<hr>

# 2016 Finalists
Out of over 300 entries, these were chosen by a [panel of judges]({{site.baseurl}}/judges) to be among the best of 2016:

<p>
{% assign sorted_pages = (site.categories.finalist | sort: 'title') %}
  {% for post in sorted_pages %}
    {% if post.categories contains '2016' %}
      <strong>&emsp;•&emsp;<a href="{{ post.url }}">
        {{ post.title }}
      </a></strong>
        {% endif %}
  {% endfor %}
</p>

<hr>

# 2015 Finalists
Out of nearly 250 entries, these were chosen by a [panel of judges]({{site.baseurl}}/judges) to be among the best of 2015:

<p>
{% assign sorted_pages = (site.categories.finalist | sort: 'title') %}
  {% for post in sorted_pages %}
    {% if post.categories contains '2015' %}
      <strong>&emsp;•&emsp;<a href="{{ post.url }}">
        {{ post.title }}
      </a></strong>
        {% endif %}
  {% endfor %}
</p>
