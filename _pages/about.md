---
title: "About"
layout: gridlay
sitemap: false
permalink: /about/
---

## About 


{% for member in site.data.pi %}

<div class="row">
  <img src="{{ site.url }}{{ site.baseurl }}/images/team/{{ member.photo-large }}" class="img-responsive avatar-about" />
  <h3>{{ member.name }}</h3>
  <i style="font-size:20px">{{ member.info }}</i><br>

  {% if member.website %}<a href="{{ member.website }}" target="_blank"><i class="fa fa-home fa-3x"></i></a> {% endif %}
  {% if member.email %}<a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-3x"></i></a> {% endif %}
  {% if member.cv %} <a href="{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-3x"></i></a> {% endif %}
  {% if member.orcid %} <a href="{{ member.orcid }}" target="_blank"><i class="ai ai-orcid-square ai-3x"></i></a> {% endif %}
  {% if member.linkedin %} <a href="{{ member.linkedin }}" target="_blank"><i class="fa fa-linkedin-square fa-3x"></i></a> {% endif %}
  {% if member.scholar %} <a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-3x"></i></a> {% endif %}
  {% if member.researchgate %} <a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-3x"></i></a> {% endif %}
  {% if member.github %} <a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-3x"></i></a> {% endif %}
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

  {% if member.number_educ == 6 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  <li> {{ member.education6 }} </li>
  {% endif %}

  </ul>
</div>

{% endfor %}

## Short biography

<div class="short-bio">
  Pavlo Bazilinskyy is an assistant professor at TU Eindhoven focusing on AI-driven interaction between automated vehicles and other road users. He finished his PhD at TU Delft in auditory feedback for automated driving as a Marie Curie Fellow, where he also worked as a postdoc. He was the head of data research at NEXTdriver. Pavlo is a treasurer of the Marie Curie Alumni Association (MCAA) and was a director of the Research and Innovation unit of the Erasmus Mundus Association (EMA).
</div>

{% if site.data.awards %}
## Awards
<div class="rowl1" style="padding-top: 10px;">

{% for award in site.data.awards %}
{{ forloop.index }}. {% if award.name_url %}<a href="{{ award.name_url }}" target="_blank">{% endif %}<strong>{{ award.name }}</strong>{% if award.name_url %}</a>{% endif %} {% if award.organisation %} from {% if award.organisation_url %}<a href="{{ award.organisation_url }}" target="_blank">{% endif %} {{ award.organisation }}{% if award.organisation_url %}</a>{% endif %}{% endif %}{% if award.subtitle %}: {{ award.subtitle }}{% endif %} ({{ award.year }}).
{% endfor %}
</div>
{% endif %}

{% if site.data.grants %}
## Grants
<div class="rowl1" style="padding-top: 10px;">

{% for grant in site.data.grants %}
{{ forloop.index }}. {% if grant.name_url %}<a href="{{ grant.name_url }}" target="_blank">{% endif %}<strong>{{ grant.name }}</strong>{% if grant.name_url %}</a>{% endif %} {% if grant.organisation %} from {% if grant.organisation_url %}<a href="{{ grant.organisation_url }}" target="_blank">{% endif %} {{ grant.organisation }}{% if grant.organisation_url %}</a>{% endif %}{% endif %}{% if grant.subtitle %}: {{ grant.subtitle }}{% endif %} ({{ grant.year }}).
{% endfor %}
</div>
{% endif %}

{% if site.data.collaborators %}
## Collaborations
<div class="rowl1" style="padding-top: 10px;">

{% for collaborator in site.data.collaborators %}
{{ forloop.index }}. {% if collaborator.name_url %}<a href="{{ collaborator.name_url }}" target="_blank">{% endif %}<strong>{{ collaborator.name }}</strong>{% if collaborator.name_url %}</a>{% endif %} ({{ collaborator.field }}, {% if collaborator.institution_url %}<a href="{{ collaborator.institution_url }}" target="_blank">{% endif %}{{ collaborator.institution }}{% if collaborator.institution_url %}</a>{% endif %}).
{% endfor %}
</div>
{% endif %}

{% if site.data.collaborators %}
## Invited speakers at my group
<div class="rowl1" style="padding-top: 10px;">

{% for invited_speaker in site.data.invited_speakers %}
{{ forloop.index }}. {% if invited_speaker.name_url %}<a href="{{ invited_speaker.name_url }}" target="_blank">{% endif %}<strong>{{ invited_speaker.name }}</strong>{% if invited_speaker.name_url %}</a>{% endif %} ({{ invited_speaker.field }}, {% if invited_speaker.institution_url %}<a href="{{ invited_speaker.institution_url }}" target="_blank">{% endif %}{{ invited_speaker.institution }}{% if invited_speaker.institution_url %}</a>{% endif %}){% if invited_speaker.venue %} – at {{ invited_speaker.venue }}{% endif %}{% if invited_speaker.date %}, {{ invited_speaker.date }}{% endif %}.
{% endfor %}
</div>
{% endif %}
