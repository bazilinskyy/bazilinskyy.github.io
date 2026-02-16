---
title: "Education"
layout: gridlay
sitemap: false
permalink: /education/
---

# Education

{% if site.courses %}
<!-- Sort courses by year -->
{% assign courses = site.courses | sort: 'year_start' | reverse %}

## Courses
<div class="rowl1" style="padding-top: 10px;">

{% for course in courses %}
{{ forloop.index }}. {% if course.url %}<a href="{{ course.url }}" target="_blank">{% endif %} <strong>{{ course.name }}</strong> {% if course.name_url %}</a>{% endif %} ({{ course.institution }}, {{ course.year_start }}–{{ course.year_end }}) {% if course.type == 'bsc' %}<button class="btn-completed">BSc</button>{% endif %}{% if course.type == 'msc' %}<button class="btn-inprogress">MSc</button>{% endif %}{% if course.type == 'phd' %}<button class="btn-notstarted">PhD</button>{% endif %}{% if course.comment %} – {{ course.comment }}{% endif %}
<br/>
<i>{{ course.code }}. {{ course.subheading }}</i>.

{% endfor %}

</div>
{% endif %}

{% if site.data.lectures %}
<!-- Sort lectures by year -->
{% assign lectures = site.data.lectures | sort: 'year' | reverse %}

## Guest lectures
<div class="rowl1" style="padding-top: 10px;">

{% for lecture in lectures %}
  {{ forloop.index }}. {{ lecture.name }} ({{ lecture.year }}).
{% endfor %}

</div>
{% endif %}

{% if site.data.supervision_phd %}
<!-- Sort students by year -->
{% assign students = site.data.supervision_internship | sort: 'year' | reverse %}
## Supervision of PhD students
<div class="rowl1" style="padding-top: 10px;">

{% for student in site.data.supervision_phd %}

{{ forloop.index }}. {% if student.name_url %}<a href="{{ student.name_url }}" target="_blank">{% endif %} <strong>{{ student.name }}</strong> {% if student.name_url %}</a>{% endif %} ({{ student.year }}) {% if student.comment %} – {{ student.comment }}{% endif %}
<br/>
<i>{{ student.project }}</i>{% if student.project_url %} (<a href="{{ student.project_url }}" target="_blank">link</a>){% endif %}.

{% endfor %}
</div>
{% endif %}

{% if site.data.supervision_msc %}
<!-- Sort courses by year -->
{% assign students = site.data.supervision_msc | sort: 'year' | reverse %}
## Supervision of MSc students and student groups
<div class="rowl1" style="padding-top: 10px;">

{% for student in students %}
  {% assign pdffile = false %}
  {% if student.project_url %}
      {% if student.project_url contains '://' %}
        {% assign pdffile = student.project_url %}
      {% else %}
        {% assign pdffile = "/publications/students/" | append:  student.project_url  | append: ".pdf" %}
      {% endif %}
  {% endif %}

{{ forloop.index }}. {% if student.name_url %}<a href="{{ student.name_url }}" target="_blank">{% endif %} <strong>{{ student.name }}</strong> {% if student.name_url %}</a>{% endif %} ({{ student.year }}) {% if student.comment %} – {{ student.comment }}{% endif %}
<br/>
<i>{{ student.project }}</i>{% if pdffile %} (<a href="{{ pdffile }}" target="_blank">link</a>){% endif %}.

{% endfor %}
</div>
{% endif %}

{% if site.data.supervision_bsc %}
<!-- Sort students by year -->
{% assign students = site.data.supervision_bsc | sort: 'year' | reverse %}
## Supervision of BSc students and student groups
<div class="rowl1" style="padding-top: 10px;">

{% for student in students %}
  {% assign pdffile = false %}
  {% if student.project_url %}
      {% if student.project_url contains '://' %}
        {% assign pdffile = student.project_url %}
      {% else %}
        {% assign pdffile = "/publications/students/" | append:  student.project_url  | append: ".pdf" %}
      {% endif %}
  {% endif %}

{{ forloop.index }}. {% if student.name_url %}<a href="{{ student.name_url }}" target="_blank">{% endif %} <strong>{{ student.name }}</strong> {% if student.name_url %}</a>{% endif %} ({{ student.year }}) {% if student.comment %} – {{ student.comment }}{% endif %}
<br/>
<i>{{ student.project }}</i>{% if pdffile %} (<a href="{{ pdffile }}" target="_blank">link</a>){% endif %}.

{% endfor %}
</div>
{% endif %}

{% if site.data.supervision_internship %}
<!-- Sort students by year -->
{% assign students = site.data.supervision_internship | sort: 'year' | reverse %}
## Supervision of internships
<div class="rowl1" style="padding-top: 10px;">

{% for student in students %}
  {% assign pdffile = false %}
  {% if student.project_url %}
      {% if student.project_url contains '://' %}
        {% assign pdffile = student.project_url %}
      {% else %}
        {% assign pdffile = "/publications/students/" | append:  student.project_url  | append: ".pdf" %}
      {% endif %}
  {% endif %}

{{ forloop.index }}. {% if student.name_url %}<a href="{{ student.name_url }}" target="_blank">{% endif %} <strong>{{ student.name }}</strong> {% if student.name_url %}</a>{% endif %} ({{ student.year }}) {% if student.comment %} – {{ student.comment }}{% endif %}
<br/>
<i>{{ student.project }}</i>{% if pdffile %} (<a href="{{ pdffile }}" target="_blank">link</a>){% endif %}.

{% endfor %}
</div>
{% endif %}

{% if site.data.supervision_defence %}
<!-- Sort students by year -->
{% assign students = site.data.supervision_defence | sort: 'year' | reverse %}
## Defence committees
<div class="rowl1" style="padding-top: 10px;">
{% if student.status == 'fail' %}<button class="btn-notstarted">FAIL</button>{% endif %}
{% for student in students %}
  {% assign pdffile = false %}
  {% if student.project_url %}
      {% if student.project_url contains '://' %}
        {% assign pdffile = student.project_url %}
      {% else %}
        {% assign pdffile = "/publications/students/" | append:  student.project_url  | append: ".pdf" %}
      {% endif %}
  {% endif %}

{{ forloop.index }}. {% if student.name_url %}<a href="{{ student.name_url }}" target="_blank">{% endif %} <strong>{{ student.name }}</strong> {% if student.name_url %}</a>{% endif %} ({% if student.degree %}{{ student.degree }}, {% endif %}{{ student.year }}) {% if student.institution %} – at {{ student.institution }} {% endif %}
<br/>
<i>{{ student.project }}</i>{% if pdffile %} (<a href="{{ pdffile }}" target="_blank">link</a>){% endif %}.

{% endfor %}
</div>
{% endif %}
