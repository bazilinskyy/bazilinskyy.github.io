---
title: "Talks"
layout: gridlay
sitemap: false
permalink: /talks/
---

# Chairing duties for conferences

{% if site.data.chairing_autoui %}
## AutoUI
<div class="rowl1" style="padding-top: 10px;">

{% for session in site.data.chairing_autoui %}
{{ forloop.index }}. {% if session.link %}<a href="{{ session.link }}" target="_blank">{% endif %}<strong>{{ session.title }}</strong>{% if session.link %}</a>{% endif %} ({{ session.year }}) – {{ session.location }}.{% if session.subtitle %}</br>{{ session.subtitle }}{% endif %}
{% endfor %}
</div>
{% endif %}

{% if site.data.chairing_roman %}
## IEEE RO-MAN
<div class="rowl1" style="padding-top: 10px;">

{% for session in site.data.chairing_roman %}
{{ forloop.index }}. {% if session.link %}<a href="{{ session.link }}" target="_blank">{% endif %}<strong>{{ session.title }}</strong>{% if session.link %}</a>{% endif %} ({{ session.year }}) – {{ session.location }}.{% if session.subtitle %}</br>{{ session.subtitle }}{% endif %}
{% endfor %}
</div>
{% endif %}

# Talks

{% if site.data.conference_talks %}
## Conference presentations
<div class="rowl1" style="padding-top: 10px;">

{% for talk in site.data.conference_talks %}
{{ forloop.index }}. <strong>{{ talk.title }}</strong> <br/> <i>{{ talk.authors }}</i>, {{ talk.conf }} ({{ talk.year }}).
{% endfor %}
</div>
{% endif %}

{% if site.data.invited_talks %}
## Talks and webinars
<div class="rowl1" style="padding-top: 10px;">

{% for talk in site.data.invited_talks %}
{{ forloop.index }}. {% if talk.link %}<a href="{{ talk.link }}" target="_blank">{% endif %}<strong>{{ talk.title }}</strong>{% if talk.link %}</a>{% endif %} ({{ talk.year }}){% if talk.subtitle %}<br>{{ talk.subtitle }}{% endif %}.
{% endfor %}
</div>
{% endif %}

{% if site.data.chairing_sessions %}
## Chairing sessions
<div class="rowl1" style="padding-top: 10px;">

{% for session in site.data.chairing_sessions %}
{{ forloop.index }}. {% if session.link %}<a href="{{ session.link }}" target="_blank">{% endif %}<strong>{{ session.title }}</strong>{% if session.link %}</a>{% endif %} ({{ session.year }}){% if session.subtitle %} {{ session.subtitle }}{% endif %}<br/>{{ session.conf }}.
{% endfor %}
</div>
{% endif %}

{% if site.workshops %}
## Workshops
<div class="rowl1" style="padding-top: 10px;">

{% for workshop in site.workshops %}
{{ forloop.index }}. <a href="{{ workshop.url | replace:'.html', '' }}" target="_blank"><strong>{{ workshop.title }}</strong></a> ({{ workshop.year }})<br/> {{workshop.conf}}, {{workshop.place}}{% if workshop.online %} (online){% endif %}.
{% endfor %}
</div>
{% endif %}

{% if site.data.outreach %}
## Outreach activities
<div class="rowl1" style="padding-top: 10px;">

{% for outreach in site.data.outreach %}
{{ forloop.index }}. <a href="{{ outreach.url | replace:'.html', '' }}" target="_blank"><strong>{{ outreach.title }}</strong></a> ({{ outreach.year }})<br/> {{outreach.event}}, {{outreach.place}}{% if workshop.online %} (online){% endif %}.
{% endfor %}
</div>
{% endif %}
