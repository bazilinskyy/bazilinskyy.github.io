---
title: "CV"
description: "Curriculum vitae of Pavlo Bazilinskyy: positions, grants, awards, teaching, supervision, talks and conference service."
layout: gridlay
permalink: /cv/
---

{%- comment -%}
Everything here is rendered from the same YAML the rest of the site uses, so the
CV cannot drift from the pages it summarises. Add a grant or a talk to _data and
it appears here too. Nothing on this page is written twice.
{%- endcomment -%}

# CV

{% for member in site.data.pi %}
<div class="cv-head" markdown="0">
  <p class="cv-name">{{ member.name }}</p>
  <p class="cv-role">{{ member.info }}</p>
  <p class="cv-links">
    {% if member.email %}<a href="mailto:{{ member.email }}">{{ member.email }}</a>{% endif %}
    {% if member.scholar %} · <a href="{{ member.scholar }}" target="_blank">Google Scholar</a>{% endif %}
    {% if member.orcid %} · <a href="{{ member.orcid }}" target="_blank">ORCID</a>{% endif %}
    {% if member.github %} · <a href="{{ member.github }}" target="_blank">GitHub</a>{% endif %}
    {% if member.linkedin %} · <a href="{{ member.linkedin }}" target="_blank">LinkedIn</a>{% endif %}
    {% if member.researchgate %} · <a href="{{ member.researchgate }}" target="_blank">ResearchGate</a>{% endif %}
    {% if member.cv %} · <a href="{{ member.cv }}" target="_blank">PDF version</a>{% endif %}
  </p>
</div>

## Positions and education

<div class="rowl1 cv-list">
{% for n in (1..member.number_educ) %}
{%- capture key -%}education{{ n }}{%- endcapture -%}
{{ forloop.index }}. {{ member[key] }}
{% endfor %}
</div>
{% endfor %}

{% assign journals = site.publications | where_exp: "p", "p.tags contains 'journal'" | size %}
{% assign conferences = site.publications | where_exp: "p", "p.tags contains 'conference'" | size %}
{% assign preprints = site.publications | where_exp: "p", "p.tags contains 'preprint'" | size %}
{% assign theses = site.publications | where_exp: "p", "p.tags contains 'thesis'" | size %}

## Publications

<div class="rowl1 cv-list" markdown="0">
  <p><strong>{{ site.publications | size }}</strong> in total — {{ journals }} journal, {{ conferences }} conference, {{ preprints }} preprint, {{ theses }} thesis. The full list, searchable and with BibTeX, is on the <a href="{{ site.url }}{{ site.baseurl }}/p/">publications page</a>.</p>
</div>

{% if site.data.grants %}
## Grants

<div class="rowl1 cv-list">
{% for grant in site.data.grants %}
{{ forloop.index }}. {% if grant.name_url %}<a href="{{ grant.name_url }}" target="_blank">{% endif %}<strong>{{ grant.name }}</strong>{% if grant.name_url %}</a>{% endif %} ({{ grant.year }}){% if grant.organisation %} – {% if grant.organisation_url %}<a href="{{ grant.organisation_url }}" target="_blank">{% endif %}{{ grant.organisation }}{% if grant.organisation_url %}</a>{% endif %}{% endif %}.
{% endfor %}
</div>
{% endif %}

{% if site.data.awards %}
## Awards

<div class="rowl1 cv-list">
{% for award in site.data.awards %}
{{ forloop.index }}. {% if award.name_url %}<a href="{{ award.name_url }}" target="_blank">{% endif %}<strong>{{ award.name }}</strong>{% if award.name_url %}</a>{% endif %} ({{ award.year }}){% if award.organisation %} – {% if award.organisation_url %}<a href="{{ award.organisation_url }}" target="_blank">{% endif %}{{ award.organisation }}{% if award.organisation_url %}</a>{% endif %}{% endif %}.{% if award.subtitle %}<br/><em>{{ award.subtitle }}</em>{% endif %}
{% endfor %}
</div>
{% endif %}

## Teaching

<div class="rowl1 cv-list">
{% assign courses = site.courses | sort: "year_start" | reverse %}
{% for course in courses %}
{{ forloop.index }}. {% if course.name_url %}<a href="{{ course.name_url }}" target="_blank">{% endif %}<strong>{{ course.name }}</strong>{% if course.name_url %}</a>{% endif %} ({{ course.year_start }}{% if course.year_end %}–{{ course.year_end }}{% endif %}) – {{ course.institution }}{% if course.type %}, {{ course.type | upcase }}{% endif %}.
{% endfor %}
{% for lecture in site.data.lectures %}
{{ courses | size | plus: forloop.index }}. {{ lecture.name }} ({{ lecture.year }}).
{% endfor %}
</div>

## Supervision

<div class="rowl1 cv-list" markdown="0">
  <p>
    {{ site.data.supervision_phd | size }} PhD ·
    {{ site.data.supervision_msc | size }} MSc ·
    {{ site.data.supervision_bsc | size }} BSc ·
    {{ site.data.supervision_internship | size }} internship ·
    {{ site.data.supervision_defence | size }} doctoral committee.
    Full lists are on the <a href="{{ site.url }}{{ site.baseurl }}/education/">education page</a>.
  </p>
</div>

<div class="rowl1 cv-list">
{% for student in site.data.supervision_phd %}
{{ forloop.index }}. {% if student.name_url %}<a href="{{ student.name_url }}" target="_blank">{% endif %}<strong>{{ student.name }}</strong>{% if student.name_url %}</a>{% endif %} ({{ student.year }}–) – <em>{{ student.project }}</em>.
{% endfor %}
</div>

{% if site.data.invited_talks %}
## Invited talks

<div class="rowl1 cv-list">
{% for talk in site.data.invited_talks %}
{{ forloop.index }}. {% if talk.link %}<a href="{{ talk.link }}" target="_blank">{% endif %}<strong>{{ talk.title }}</strong>{% if talk.link %}</a>{% endif %} ({{ talk.year }}).{% if talk.subtitle %}<br/><em>{{ talk.subtitle }}</em>{% endif %}
{% endfor %}
</div>
{% endif %}

{% if site.data.conference_talks %}
## Conference talks

<div class="rowl1 cv-list">
{% for talk in site.data.conference_talks %}
{{ forloop.index }}. <strong>{{ talk.title }}</strong> ({{ talk.year }}).<br/>{{ talk.authors }}<br/><em>{{ talk.conf }}</em>
{% endfor %}
</div>
{% endif %}

## Conference service

<div class="rowl1 cv-list">
{% assign chaired = 0 %}
{% for session in site.data.chairing_autoui %}
{% assign chaired = chaired | plus: 1 %}
{{ chaired }}. {% if session.link %}<a href="{{ session.link }}" target="_blank">{% endif %}<strong>{{ session.title }}</strong>{% if session.link %}</a>{% endif %} ({{ session.year }}) – AutoUI, {{ session.location }}.
{% endfor %}
{% for session in site.data.chairing_roman %}
{% assign chaired = chaired | plus: 1 %}
{{ chaired }}. {% if session.link %}<a href="{{ session.link }}" target="_blank">{% endif %}<strong>{{ session.title }}</strong>{% if session.link %}</a>{% endif %} ({{ session.year }}) – IEEE RO-MAN, {{ session.location }}.
{% endfor %}
{% for session in site.data.chairing_sessions %}
{% assign chaired = chaired | plus: 1 %}
{{ chaired }}. {% if session.link %}<a href="{{ session.link }}" target="_blank">{% endif %}<strong>{{ session.title }}</strong>{% if session.link %}</a>{% endif %} ({{ session.year }}) – {{ session.conf }}.
{% endfor %}
</div>

{% if site.data.research_visits %}
## Research visits

<div class="rowl1 cv-list">
{% for visit in site.data.research_visits %}
{{ forloop.index }}. {% if visit.institution_url %}<a href="{{ visit.institution_url }}" target="_blank">{% endif %}<strong>{{ visit.institution }}</strong>{% if visit.institution_url %}</a>{% endif %}, {{ visit.location }} ({{ visit.period }}).
{% endfor %}
</div>
{% endif %}

{% if site.data.outreach %}
## Outreach

<div class="rowl1 cv-list">
{% for item in site.data.outreach %}
{{ forloop.index }}. {% if item.url %}<a href="{{ item.url }}" target="_blank">{% endif %}<strong>{{ item.title }}</strong>{% if item.url %}</a>{% endif %} ({{ item.year }}) – {{ item.event }}, {{ item.place }}.
{% endfor %}
</div>
{% endif %}
