---
title: "Team"
description: "Research team and open positions for PhD students, postdocs and master students at TU Eindhoven."
layout: gridlay
permalink: /team/
---

# Team

 **We are  looking for new PhD students, Postdocs, and Master students to join the team** [(get in touch)](mailto:p.bazilinskyy@tue.nl) **!**

<!--- Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors). -->

## PI

{% for member in site.data.pi %}

<div class="row">
  {% if member.photo-small %}<img src="{{ site.url }}{{ site.baseurl }}/images/team/{{ member.photo-small }}" alt="{{ member.name }}" class="img-responsive" width="18%" style="float: left" />{% endif %}
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }}</i><br>

  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-2x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %}
  <a href="{{ site.url }}{{ site.baseurl }}/cv/"><i class="ai ai-cv-square ai-2x"></i></a> 
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a> {% endif %}
  {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-2x"></i></a> {% endif %}
  <ul style="overflow: hidden">

  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  <li> {{ member.education6 }} </li>

  </ul>
</div>

{% endfor %}


## Current Students and Postdocs
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  {% if member.photo %}<img loading="lazy" src="{{ site.url }}{{ site.baseurl }}/images/team/{{ member.photo }}" alt="{{ member.name }}" class="img-responsive" width="25%" style="float: left" />{% endif %}
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }}<br></i>

  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-2x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a> {% endif %}
  {% if member.cv %} <a href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a> {% endif %}
  {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-2x"></i></a> {% endif %}
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


{% if site.data.alumni_members %}
## Alumni

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  {% if member.photo %}<img loading="lazy" src="{{ site.url }}{{ site.baseurl }}/images/team/{{ member.photo }}" alt="{{ member.name }}" class="img-responsive" width="25%" style="float: left" />{% endif %}
  <h4>{{ member.name }}</h4>
  <i>{{ member.duration }} <br> Role: {{ member.info }}</i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
{% endif %}


{% if site.data.alumni_visitors %}
## Former M.S./B.S Students, Visitors
<div class="row">
<div class="col-sm-6 clearfix">
{% for member in site.data.alumni_visitors %}
{{ member.name }}
{% endfor %}
</div>
</div>
{% endif %}



