---
layout: default
---
# Design a role-playing game using 200 words or less.

### Why 200 Words?

A 200 word limit encourages creativity and demands the very best of your editing and writing abilities. While making a game in 200 words can be difficult, it’s less of a daunting commitment than editing and proofing 85 pages of rules, complete with art and layout.

Conceiving, designing, and publishing a 200 word game is a great first step toward completing larger game design projects.

### Plaintext?

Visual presentation can be a large and scary problem. Very few people are masters of writing, editing, art direction, graphic design, layout, and marketing. It usually takes a village to make a game. We want participants to focus solely on the challenge of creative writing and brutal editing.

### Connect with Creators

Making and sharing a game is a great way to showcase your ideas and connect with new and more experienced game designers. Do you see a game that inspires you? The 200 Word RPG Challenge is a forge for new collaborations! All entries are protected under the [Creative Commons license]({{site.baseurl}}/licensing).

<hr>

# Random Entry of the Day
  
<a class="twitter-timeline" data-tweet-limit="1" data-chrome="noheader nofooter noscrollbar" data-dnt="true" href="https://twitter.com/200WordRPG">Tweets by 200WordRPG</a> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<hr>
# News and Updates

<ul>
{% assign sorted_pages = (site.categories.news | sort: 'date') | reverse %}
  {% for post in sorted_pages %}
      <li><h3><strong><a href="{{ post.url }}">
        {{ post.title }}
      </a></strong></h3></li>
  {% endfor %}
</ul>

