---
layout: default
---

# Winners
Chosen by the [Judges]({{site.baseurl}}/judges), these entries were particularly creative and engaging! There are no 1st, 2nd, or 3rd places, only top three winners in no particular order. **Some of the winners received fancy graphic designs that can be found on the [Downloads Page]({{sire.baseurl}}/downloads).**

### **2019** :&emsp;[Hey, this song reminds me of you]({% post_url /2019/2019-10-12-Heythissongremindsmeofyou %})&emsp;•&emsp;[Past Your Bedtime]({% post_url /2019/2019-10-12-PastYourBedtime %})&emsp;•&emsp;[002: License to Eavesdrop]({% post_url /2019/2019-10-12-002LicensetoEavesdrop %})

### **2018** :&emsp;[#WinterIntoSpring]({% post_url /2018/2018-05-17-WinterIntoSpring %})&emsp;•&emsp;[Dear Elizabeth...]({% post_url /2018/2018-05-28-DearElizabeth %})&emsp;•&emsp;[Sidewalkia!]({% post_url /2018/2018-05-18-Sidewalkia %})

### **2017** :&emsp;[MECHANICAL ORYX]({% post_url /2017/2017-04-15-MECHANICALORYX %})&emsp;•&emsp;[Memories]({% post_url /2017/2017-04-21-Memories %})&emsp;•&emsp;[Route Clearance]({% post_url /2017/2017-04-22-RouteClearance %})

### **2016** RPGs:&emsp;[Deconstruction]({{site.baseurl}}{% post_url /2016/2016-04-12-Deconstruction %})&emsp;•&emsp;[Stardust]({{site.baseurl}}{% post_url /2016/2016-04-09-Stardust %})&emsp;•&emsp;[Time Travel Thaw]({{site.baseurl}}{% post_url /2016/2016-04-14-TimeTravelThaw %})
 
### **2016** Supplements:&emsp;[The College Animalia]({{site.baseurl}}{% post_url /2016/2016-04-06-TheCollegeAnimalia %})&emsp;•&emsp;[First Steps]({{site.baseurl}}{% post_url /2016/2016-04-17-FirstStepsAdventuringWorkshop %})&emsp;•&emsp;[Foam Dart RPG]({{site.baseurl}}{% post_url /2016/2016-04-07-FoamDartRPG %})

### **2015**:&emsp;[All Fall Down]({{site.baseurl}}{% post_url /2015/2015-04-01-AllFallDown %})&emsp;•&emsp;[Escape Pod One]({{site.baseurl}}{% post_url /2015/2015-04-01-EscapePodOne %})&emsp;•&emsp;[LOVEINT]({{site.baseurl}}{% post_url /2015/2015-04-01-LOVEINT %})

# 2019 Judge Spotlights

*Each judge picked an entry to feature and write a short blurb. These are independent of the winners.*

**Chris' Spotlight:** [Past Your Bedtime]({% post_url /2019/2019-10-12-PastYourBedtime %})

> I love this game! It features my favorite parts of RPGs: the storytelling elements and the closeness of a small group. The game could easily encompass an additional few players as siblings. It also relates to me as a parent and is a game I may try with my own kid this week.  

**Kathleen's Spotlight:** [The Waiting Room, Your Partner Is In Surgery]({% post_url 2019/2019-10-12-TheWaitingRoomYourPartnerisinSurgery %})

> Over a series of three letters to a partner in surgery across a span of hours, this RPG makes solo work within a real-time framework over several hours. This game could have a transformative effect on one's relationship with a significant other, family member, or friend if used as a tool of reflection.

**Mariam's Spotlight:** [Hey, this song reminds me of you]({% post_url /2019/2019-10-12-Heythissongremindsmeofyou %})

> This is a great two-person game that combines the fun of discovering songs of personal significance with a guided prompt for role-playing two characters connected through music.

**Cheyenne's Spotlight:** [We Love You Nino's Pizza]({% post_url /2019/2019-10-02-WeLoveYouNinosPizza %})

> I love the sign mechanic element of the game. Sure to be the one of the more memorable aspects of the game. Super engaging.

# 2019 Finalists

These were chosen by a [dedicated group of Readers]({{site.baseurl}}/readers) to be among the best of 2019.

{% assign sorted_pages = site.categories.2019 | where_exp: "post", "post.categories contains 'finalist'" | sort:"title" %}
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

# 2018 Finalists

Out of nearly 800 entries, these were chosen by a [dedicated group of Readers]({{site.baseurl}}/readers) to be among the best of 2018.

{% assign sorted_pages = site.categories.2018 | where_exp: "post", "post.categories contains 'finalist'" | sort:"title" %}
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

# 2017 Finalists

Out of nearly 700 entries, these were chosen by a [panel of judges]({{site.baseurl}}/judges) to be among the best of 2017:

{% assign sorted_pages = site.categories.2017 | where_exp: "post", "post.categories contains 'finalist'" | sort:"title" %}
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

# 2016 Finalists

Out of over 300 entries, these were chosen by a [panel of judges]({{site.baseurl}}/judges) to be among the best of 2016:

{% assign sorted_pages = site.categories.2016 | where_exp: "post", "post.categories contains 'finalist'" | sort:"title" %}
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

# 2015 Finalists

Out of nearly 250 entries, these were chosen by a [panel of judges]({{site.baseurl}}/judges) to be among the best of 2015:

{% assign sorted_pages = site.categories.2015 | where_exp: "post", "post.categories contains 'finalist'" | sort:"title" %}
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
