---
title: "Publications"
layout: gridlay
sitemap: false
permalink: /publications/
---

# Publications

<div id="pub-filters">
<div class="filter-group">
  <span class="filter-label">Type</span>
  <button class="filter-btn active" data-filter="all">All</button>
  <button class="filter-btn" data-filter="journal">Journal</button>
  <button class="filter-btn" data-filter="conference">Conference</button>
    <button class="filter-btn" data-filter="thesis">Thesis</button>
  <button class="filter-btn" data-filter="preprint">Preprint</button>
  <!-- <button class="filter-btn" data-filter="poster">Poster</button> -->
</div>
<div class="filter-group">
  <span class="filter-label">Method</span>
  <button class="filter-btn active" data-filter="all">All</button>
  <button class="filter-btn" data-filter="design">Design</button>
  <button class="filter-btn" data-filter="meta">Meta</button>
  <button class="filter-btn" data-filter="lab">Lab</button>
  <button class="filter-btn" data-filter="simulator">Simulator</button>
  <button class="filter-btn" data-filter="crowdsourcing">Crowdsourcing</button>
  <button class="filter-btn" data-filter="woz">Wizard of Oz</button>
  <button class="filter-btn" data-filter="eye-tracking">Eye tracking</button>
  <button class="filter-btn" data-filter="virtual-reality">Virtual reality</button>
  <button class="filter-btn" data-filter="extended-reality">Extended reality</button>
  <button class="filter-btn" data-filter="on-road">On-road</button>
  <button class="filter-btn" data-filter="survey">Survey</button>
  <button class="filter-btn" data-filter="naturalistic">Naturalistic</button>
  <button class="filter-btn" data-filter="dashcam">Dashcam</button>
  <button class="filter-btn" data-filter="artificial-intelligence">Artificial intelligence</button>
  <button class="filter-btn" data-filter="computer-vision">Computer vision</button>
  <button class="filter-btn" data-filter="sensor">Sensor</button>
  <button class="filter-btn" data-filter="interview">Interview</button>
  <button class="filter-btn" data-filter="diary">Diary</button>
  <button class="filter-btn" data-filter="interview">Workshop</button>
</div>
<div class="filter-group">
  <span class="filter-label">User</span>
  <button class="filter-btn active" data-filter="all">All</button>
  <button class="filter-btn" data-filter="driver">Driver</button>
  <button class="filter-btn" data-filter="passenger">Passenger</button>
  <button class="filter-btn" data-filter="pedestrian">Pedestrian</button>
  <button class="filter-btn" data-filter="cyclist">Cyclist</button>
  <button class="filter-btn" data-filter="motorcyclist">Motorcyclist</button>
  <button class="filter-btn" data-filter="bystander">Bystander</button>
</div>
<div class="filter-group">
  <span class="filter-label">Topic</span>
  <button class="filter-btn active" data-filter="all">All</button>
  <button class="filter-btn" data-filter="automated-driving">Automated driving</button>
  <button class="filter-btn" data-filter="drone">Drones</button>
  <button class="filter-btn" data-filter="dataset">Dataset</button>
  <button class="filter-btn" data-filter="ehmi">eHMI</button>
  <button class="filter-btn" data-filter="ihmi">iHMI</button>
  <button class="filter-btn" data-filter="sound">Sound</button>
  <button class="filter-btn" data-filter="visual">Visual</button>
  <button class="filter-btn" data-filter="haptic">Haptic</button>
  <button class="filter-btn" data-filter="takeover">Takeover</button>
  <button class="filter-btn" data-filter="electric-vehicles">Electric vehicles</button>
  <button class="filter-btn" data-filter="trust">Trust</button>
  <button class="filter-btn" data-filter="uncertainty">Uncertainty</button>
  <button class="filter-btn" data-filter="robotics">Robotics</button>
  <button class="filter-btn" data-filter="mutli-agent">Multi-agent</button>
  <button class="filter-btn" data-filter="computer-science">Computer science</button>
  <button class="filter-btn" data-filter="open-science">Open science</button>
</div>
<div class="filter-group">
  <button class="filter-btn" id="reset-filters">Reset filters</button>
  <span id="pub-count"></span>
</div>
</div>

{% assign yeartest = true %}
{% for publi in site.publications %}
{% if publi.year %}{% else %}
{% assign yeartest = false %}
{% endif %}
{% endfor %}

{% if yeartest == false %}
## Working documents
{% endif %}

{% for publi in site.publications %}

{% assign pdfpresent = false %}
{% if publi.pdf %}
{% assign pdfpresent = true %}
{% assign pdffile = publi.pdf | append: ".pdf" %}
{% endif %}

{% if publi.year %}{% else %}
{% assign bibpresent = false %}
{% if publi.pdf %}
{% assign bibpresent = true %}
{% assign bibfile = publi.pdf | append: ".txt" %}
{% endif %}

{% assign tag_string = publi.tags | join: " " | downcase %}

<div class="well-sm publication-entry" data-tags="{{ tag_string }}">
<ul class="flex-container">
<li class="flex-item1">
{% if publi.image %}
<img src="{{ site.url }}{{ site.baseurl }}/publications/{{ publi.image }}" class="img-responsive"/>
{% endif %}
</li>
<li class="flex-item2">
{% if publi.pdf %}<a href="{{ publi.pdf }}" target="_blank">{% endif %}<strong>{{ publi.title }}</strong>{% if publi.pdf %}</a>{% endif %} {% if publi.tags %}{% for tag in publi.tags %}<span class="pub-tag {{ tag | downcase }}">{{ tag }}</span>{% endfor %}{% endif %}<br/>
{{ publi.authors }}<br/>
<em>{{ publi.display }}</em><br/>
{% if publi.abstract %}<a data-bs-toggle="collapse" href="#{{publi.image | remove: '.jpg'}}" class="btn-abstract" style="text-decoration:none;color:#ebebeb;" role="button" aria-expanded="false" aria-controls="{{publi.image | remove: '.jpg'}}">ABSTRACT</a>{% endif %}
{% if bibpresent == true %}<a data-bs-toggle="collapse" href="#{{publi.pdf}}2" class="btn-bib" style="text-decoration:none;color:#ebebeb;" role="button" aria-expanded="false" aria-controls="{{publi.pdf}}2">BIB</a>{% endif %}
{% if pdfpresent == true %}<a href="{{ pdffile }}" target="_blank"><button class="btn-pdf">PDF</button></a>{% endif %}
{% if publi.doi %}<a href="https://doi.org/{{ publi.doi }}" target="_blank"><button class="btn-doi">DOI</button></a>{% endif %}
{% if publi.arxiv %}<a href="https://arxiv.org/abs/{{ publi.arxiv }}" target="_blank"><button class="btn-arxiv">ARXIV</button></a>{% endif %}
{% if publi.code %}<a href="{{ publi.code }}" target="_blank"><button class="btn-code">CODE</button></a>{% endif %}
{% if publi.suppmat %}<a href="{{ publi.suppmat }}" target="_blank"><button class="btn-suppmat">SUPPLEMENT</button></a>{% endif %}
{% if publi.abstract %}
<div class="collapse" id="{{publi.image | remove: '.jpg'}}"><div class="well-abstract">
{{publi.abstract}}
</div></div>
{% endif %}
{% if bibpresent == true %}
<div class="collapse" id="{{publi.pdf}}2"><div class="well-bib">
<iframe src='{{site.url}}{{site.baseurl}}/publications/{{publi.pdf}}.txt' scrolling="yes" width="100%" height="210" frameborder="0"></iframe>
</div></div>
{% endif %}
</li>
</ul>
</div>
{% endif %}
{% endfor %}

{% if site.group_pub_by_year == true %}{% else %}
## Journal papers and proceedings
{% endif %}

{% for myyear in site.data.years %}

{% assign yeartest = false %}
{% for publi in site.publications %}
{% if publi.year == myyear.year %}
{% assign yeartest = true %}
{% endif %}
{% endfor %}

{% if site.group_pub_by_year == true %}
{% if yeartest == true %}
## {{ myyear.year }}
{% endif %}
{% endif %}

{% for publi in site.publications %}

{% assign pdfpresent = false %}
{% if publi.pdf %}
{% assign pdfpresent = true %}
{% assign pdffile = publi.pdf | append: ".pdf" %}
{% endif %}

{% if publi.year == myyear.year %}
{% assign bibpresent = false %}
{% if publi.pdf %}
{% assign bibpresent = true %}
{% assign bibfile = publi.pdf | append: ".txt" %}
{% endif %}

{% assign tag_string = publi.tags | join: " " | downcase %}

<div class="well-sm publication-entry" data-tags="{{ tag_string }}">
<ul class="flex-container">
<li class="flex-item1">
{% if publi.image %}
<img src="{{ site.url }}{{ site.baseurl }}/publications/{{ publi.image }}" class="img-responsive"/>
{% endif %}
</li>
<li class="flex-item2">
{% if publi.pdf %}<a href="{{ publi.pdf }}" target="_blank">{% endif %}<strong>{{ publi.title }}</strong>{% if publi.pdf %}</a>{% endif %} {% if publi.tags %}{% for tag in publi.tags %}<span class="pub-tag {{ tag | downcase }}">{{ tag }}</span>{% endfor %}{% endif %}<br />
{{ publi.authors }}<br />
<em>{{ publi.display }}</em>{% if publi.year %} ({{publi.year}}){% endif %}<br/>
{% if publi.abstract %}<a data-bs-toggle="collapse" href="#{{publi.image | remove: '.jpg'}}" class="btn-abstract" style="text-decoration:none;color:#ebebeb;" role="button" aria-expanded="false" aria-controls="{{publi.image | remove: '.jpg'}}">ABSTRACT</a>{% endif %}
{% if bibpresent == true %}<a data-bs-toggle="collapse" href="#{{publi.pdf}}2" class="btn-bib" style="text-decoration:none;color:#ebebeb;" role="button" aria-expanded="false" aria-controls="{{publi.pdf}}2">BIB</a>{% endif %}
{% if pdfpresent == true %}<a href="{{ pdffile }}" target="_blank"><button class="btn-pdf">PDF</button></a>{% endif %}
{% if publi.doi %}<a href="http://doi.org/{{ publi.doi }}" target="_blank"><button class="btn-doi">DOI</button></a>{% endif %}
{% if publi.arxiv %}<a href="https://arxiv.org/abs/{{ publi.arxiv }}" target="_blank"><button class="btn-arxiv">ARXIV</button></a>{% endif %}
{% if publi.code %}<a href="{{ publi.code }}" target="_blank"><button class="btn-code">CODE</button></a>{% endif %}
{% if publi.suppmat %}<a href="{{ publi.suppmat }}" target="_blank"><button class="btn-suppmat">SUPPLEMENT</button></a>{% endif %}
{% if publi.abstract %}
<br/>
<div class="collapse" id="{{publi.image | remove: '.jpg'}}"><div class="well-abstract">
{{publi.abstract}}
</div></div>
{% endif %}
{% if bibpresent == true %}
<div class="collapse" id="{{publi.image | remove: '.jpg'}}2"><div class="well-bib">
<iframe src="{{site.url}}{{site.baseurl}}/publications/{{publi.image | remove: '.jpg'}}.txt" scrolling="yes" width="100%" height="210" frameborder="0"></iframe>
</div></div>
{% endif %}
</li>
</ul>
</div>
{% endif %}
{% endfor %}

{% endfor %}

Download all papers in bib file <a href="{{ site.url }}{{ site.baseurl }}/publications/bazilinskyy.bib">here</a>.

\* Joint first author.

<script>
(function () {
var groups = document.querySelectorAll('.filter-group');
// each group holds a Set of active filters; empty Set = "all"
var activeFilters = Array.from(groups).map(function () { return new Set(); });
function applyFilters() {
var required = [];
activeFilters.forEach(function (set) { set.forEach(function (f) { required.push(f); }); });
var entries = document.querySelectorAll('.publication-entry');
var visible = 0;
entries.forEach(function (entry) {
var tags = (entry.getAttribute('data-tags') || '').split(/\s+/).filter(Boolean);
var match = required.every(function (f) { return tags.indexOf(f) !== -1; });
entry.classList.toggle('hidden', !match);
if (match) visible++;
});
var countEl = document.getElementById('pub-count');
if (countEl) countEl.textContent = visible + ' paper' + (visible !== 1 ? 's' : '');
document.querySelectorAll('h2').forEach(function (h2) {
var hasPaper = false;
var el = h2.nextElementSibling;
while (el && el.tagName !== 'H2') {
if (el.classList.contains('publication-entry') && !el.classList.contains('hidden')) { hasPaper = true; break; }
el = el.nextElementSibling;
}
h2.style.display = hasPaper ? '' : 'none';
});
}
function syncAllBtn(group, set) {
var allBtn = group.querySelector('.filter-btn[data-filter="all"]');
if (allBtn) allBtn.classList.toggle('active', set.size === 0);
}
groups.forEach(function (group, groupIndex) {
var set = activeFilters[groupIndex];
group.querySelectorAll('.filter-btn[data-filter]').forEach(function (btn) {
btn.addEventListener('click', function () {
var f = btn.getAttribute('data-filter');
if (f === 'all') {
set.clear();
group.querySelectorAll('.filter-btn[data-filter]').forEach(function (b) { b.classList.remove('active'); });
} else {
if (set.has(f)) {
set.delete(f);
btn.classList.remove('active');
} else {
set.add(f);
btn.classList.add('active');
}
}
syncAllBtn(group, set);
applyFilters();
});
});
});
document.getElementById('reset-filters').addEventListener('click', function () {
groups.forEach(function (group, i) {
activeFilters[i].clear();
group.querySelectorAll('.filter-btn[data-filter]').forEach(function (btn) {
btn.classList.toggle('active', btn.getAttribute('data-filter') === 'all');
});
});
applyFilters();
});
applyFilters();
})();
</script>
