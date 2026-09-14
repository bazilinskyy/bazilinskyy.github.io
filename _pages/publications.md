---
title: "Publications"
description: "Searchable list of peer-reviewed papers, preprints and theses on automated driving, eHMI design, human factors and multi-agent traffic interaction."
layout: gridlay
permalink: /p/
---

# Publications

<div id="pub-filters">
<div class="filter-group">
  <span class="filter-label">Search</span>
  <input type="search" id="pub-search" placeholder="title, author, venue, year…" aria-label="Search publications" autocomplete="off" />
</div>
<div class="filter-group">
  <span class="filter-label">Type</span>
  <button class="filter-btn active" data-filter="all">All</button>
  <button class="filter-btn" data-filter="conference">Conference</button>
  <button class="filter-btn" data-filter="journal">Journal</button>
  <!-- <button class="filter-btn" data-filter="poster">Poster</button> -->
  <button class="filter-btn" data-filter="preprint">Preprint</button>
  <button class="filter-btn" data-filter="thesis">Thesis</button>
</div>
<div class="filter-group">
  <span class="filter-label">Method</span>
  <button class="filter-btn active" data-filter="all">All</button>
  <button class="filter-btn" data-filter="artificial-intelligence">Artificial intelligence</button>
  <button class="filter-btn" data-filter="computer-vision">Computer vision</button>
  <button class="filter-btn" data-filter="crowdsourcing">Crowdsourcing</button>
  <button class="filter-btn" data-filter="dashcam">Dashcam</button>
  <button class="filter-btn" data-filter="design">Design</button>
  <button class="filter-btn" data-filter="diary">Diary</button>
  <button class="filter-btn" data-filter="extended-reality">Extended reality</button>
  <button class="filter-btn" data-filter="eye-tracking">Eye tracking</button>
  <button class="filter-btn" data-filter="interview">Interview</button>
  <button class="filter-btn" data-filter="lab">Lab</button>
  <button class="filter-btn" data-filter="meta">Meta</button>
  <button class="filter-btn" data-filter="naturalistic">Naturalistic</button>
  <button class="filter-btn" data-filter="on-road">On-road</button>
  <button class="filter-btn" data-filter="sensor">Sensor</button>
  <button class="filter-btn" data-filter="simulator">Simulator</button>
  <button class="filter-btn" data-filter="survey">Survey</button>
  <button class="filter-btn" data-filter="virtual-reality">Virtual reality</button>
  <button class="filter-btn" data-filter="wizard-of-oz">Wizard of Oz</button>
  <button class="filter-btn" data-filter="workshop">Workshop</button>
</div>
<div class="filter-group">
  <span class="filter-label">User</span>
  <button class="filter-btn active" data-filter="all">All</button>
  <button class="filter-btn" data-filter="bystander">Bystander</button>
  <button class="filter-btn" data-filter="cyclist">Cyclist</button>
  <button class="filter-btn" data-filter="driver">Driver</button>
  <button class="filter-btn" data-filter="motorcyclist">Motorcyclist</button>
  <button class="filter-btn" data-filter="passenger">Passenger</button>
  <button class="filter-btn" data-filter="pedestrian">Pedestrian</button>
</div>
<div class="filter-group">
  <span class="filter-label">Topic</span>
  <button class="filter-btn active" data-filter="all">All</button>
  <button class="filter-btn" data-filter="automated-driving">Automated driving</button>
  <button class="filter-btn" data-filter="computer-science">Computer science</button>
  <button class="filter-btn" data-filter="dataset">Dataset</button>
  <button class="filter-btn" data-filter="drone">Drones</button>
  <button class="filter-btn" data-filter="ehmi">eHMI</button>
  <button class="filter-btn" data-filter="electric-vehicles">Electric vehicles</button>
  <button class="filter-btn" data-filter="haptic">Haptic</button>
  <button class="filter-btn" data-filter="ihmi">iHMI</button>
  <button class="filter-btn" data-filter="multi-agent">Multi-agent</button>
  <button class="filter-btn" data-filter="open-science">Open science</button>
  <button class="filter-btn" data-filter="robotics">Robotics</button>
  <button class="filter-btn" data-filter="sound">Sound</button>
  <button class="filter-btn" data-filter="takeover">Takeover</button>
  <button class="filter-btn" data-filter="trust">Trust</button>
  <button class="filter-btn" data-filter="uncertainty">Uncertainty</button>
  <button class="filter-btn" data-filter="visual">Visual</button>
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
{% assign search_string = publi.title | append: " " | append: publi.authors | append: " " | append: publi.display | append: " " | append: publi.year | append: " " | append: tag_string | downcase %}

<div class="well-sm publication-entry" data-tags="{{ tag_string }}" data-search="{{ search_string | escape }}">
<ul class="flex-container">
<li class="flex-item1">
{% if publi.image %}
<img loading="lazy" src="{{ site.url }}{{ site.baseurl }}/p/{{ publi.image }}" alt="" class="img-responsive"/>
{% endif %}
</li>
<li class="flex-item2">
{% if publi.pdf %}<a href="{{ site.url }}{{ site.baseurl }}/p/{{ publi.pdf }}" target="_blank">{% endif %}<strong class="pub-title">{{ publi.title }}</strong>{% if publi.pdf %}</a>{% endif %} {% if publi.tags %}{% for tag in publi.tags %}<span class="pub-tag {{ tag | downcase }}">{{ tag }}</span>{% endfor %}{% endif %}<br/>
<span class="pub-authors">{{ publi.authors }}</span><br/>
<em class="pub-venue">{{ publi.display }}</em><br/>
{% if publi.abstract %}<a data-bs-toggle="collapse" href="#{{publi.image | remove: '.jpg'}}" class="btn-abstract" style="text-decoration:none;color:#ebebeb;" role="button" aria-expanded="false" aria-controls="{{publi.image | remove: '.jpg'}}">ABSTRACT</a>{% endif %}
{% if bibpresent == true %}<a data-bs-toggle="collapse" href="#{{publi.pdf}}2" class="btn-bib" style="text-decoration:none;color:#ebebeb;" role="button" aria-expanded="false" aria-controls="{{publi.pdf}}2">BIB</a>{% endif %}
{% if pdfpresent == true %}<a href="{{ site.url }}{{ site.baseurl }}/p/{{ pdffile }}" target="_blank"><button class="btn-pdf">PDF</button></a>{% endif %}
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
<iframe data-src='{{site.url}}{{site.baseurl}}/p/{{publi.pdf}}.txt' scrolling="yes" width="100%" height="210" frameborder="0"></iframe>
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
{% assign search_string = publi.title | append: " " | append: publi.authors | append: " " | append: publi.display | append: " " | append: publi.year | append: " " | append: tag_string | downcase %}

<div class="well-sm publication-entry" data-tags="{{ tag_string }}" data-search="{{ search_string | escape }}">
<ul class="flex-container">
<li class="flex-item1">
{% if publi.image %}
<img loading="lazy" src="{{ site.url }}{{ site.baseurl }}/p/{{ publi.image }}" alt="" class="img-responsive"/>
{% endif %}
</li>
<li class="flex-item2">
{% if publi.pdf %}<a href="{{ site.url }}{{ site.baseurl }}/p/{{ publi.pdf }}" target="_blank">{% endif %}<strong class="pub-title">{{ publi.title }}</strong>{% if publi.pdf %}</a>{% endif %} {% if publi.tags %}{% for tag in publi.tags %}<span class="pub-tag {{ tag | downcase }}">{{ tag }}</span>{% endfor %}{% endif %}<br />
<span class="pub-authors">{{ publi.authors }}</span><br />
<em class="pub-venue">{{ publi.display }}</em>{% if publi.year %} (<span class="pub-year">{{publi.year}}</span>){% endif %}<br/>
{% if publi.abstract %}<a data-bs-toggle="collapse" href="#{{publi.image | remove: '.jpg'}}" class="btn-abstract" style="text-decoration:none;color:#ebebeb;" role="button" aria-expanded="false" aria-controls="{{publi.image | remove: '.jpg'}}">ABSTRACT</a>{% endif %}
{% if bibpresent == true %}<a data-bs-toggle="collapse" href="#{{publi.pdf}}2" class="btn-bib" style="text-decoration:none;color:#ebebeb;" role="button" aria-expanded="false" aria-controls="{{publi.pdf}}2">BIB</a>{% endif %}
{% if pdfpresent == true %}<a href="{{ site.url }}{{ site.baseurl }}/p/{{ pdffile }}" target="_blank"><button class="btn-pdf">PDF</button></a>{% endif %}
{% if publi.doi %}<a href="https://doi.org/{{ publi.doi }}" target="_blank"><button class="btn-doi">DOI</button></a>{% endif %}
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
<iframe data-src="{{site.url}}{{site.baseurl}}/p/{{publi.image | remove: '.jpg'}}.txt" scrolling="yes" width="100%" height="210" frameborder="0" allowtransparency="true"></iframe>
</div></div>
{% endif %}
</li>
</ul>
</div>
{% endif %}
{% endfor %}

{% endfor %}

Download all papers in bib file <a href="{{ site.url }}{{ site.baseurl }}/p/bazilinskyy.bib">here</a>.

\* Joint first author.

<script>
(function () {
var groups = document.querySelectorAll('.filter-group');
var search = document.getElementById('pub-search');

// Abstracts are already in the page inside each entry, so searching them costs no extra
// bytes. Cache the plain text of every highlightable field once so a keystroke never has
// to walk the DOM. Each selector must wrap text only, since marking rewrites innerHTML.
var MARKABLE = '.pub-title, .pub-authors, .pub-venue, .pub-year, .pub-tag';
var entryData = new Map();
document.querySelectorAll('.publication-entry').forEach(function (entry) {
var abstractEl = entry.querySelector('.well-abstract');
entryData.set(entry, {
fields: Array.prototype.map.call(entry.querySelectorAll(MARKABLE), field),
abstract: abstractEl ? field(abstractEl) : null,
abstractLower: abstractEl ? abstractEl.textContent.toLowerCase() : ''
});
});
function field(el) { return { el: el, text: el.textContent, sig: '' }; }
function escapeRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }
function escapeHtml(s) { return s.replace(/[&<>]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]; }); }
function mark(f, terms) {
var sig = terms.join('\u0000');
if (f.sig === sig) return;              // nothing changed for this field
f.sig = sig;
if (!terms.length) { f.el.textContent = f.text; return; }
var re = new RegExp('(' + terms.map(escapeRe).join('|') + ')', 'gi');
f.el.innerHTML = escapeHtml(f.text).replace(re, '<mark>$1</mark>');
}
// each group holds a Set of active filters; empty Set = "all"
var activeFilters = Array.from(groups).map(function () { return new Set(); });
function applyFilters() {
var required = [];
activeFilters.forEach(function (set) { set.forEach(function (f) { required.push(f); }); });
var terms = (search.value || '').trim().toLowerCase().split(/\s+/).filter(Boolean);
var entries = document.querySelectorAll('.publication-entry');
var visible = 0;
entries.forEach(function (entry) {
var tags = (entry.getAttribute('data-tags') || '').split(/\s+/).filter(Boolean);
var match = required.every(function (f) { return tags.indexOf(f) !== -1; });
var data = entryData.get(entry);
var fromAbstract = false;
if (match && terms.length) {
var haystack = entry.getAttribute('data-search') || '';
// all terms must appear, so "bazilinskyy ehmi" narrows rather than widens
match = terms.every(function (t) { return haystack.indexOf(t) !== -1 || data.abstractLower.indexOf(t) !== -1; });
// a term that only hit the abstract leaves no visible reason for the row,
// so open that abstract too
fromAbstract = match && terms.some(function (t) { return haystack.indexOf(t) === -1; });
}
var hits = (match && terms.length) ? terms : [];
data.fields.forEach(function (f) { mark(f, hits); });
if (data.abstract) {
mark(data.abstract, fromAbstract ? terms : []);
data.abstract.el.parentNode.classList.toggle('search-expanded', fromAbstract);
}
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
search.addEventListener('input', applyFilters);
document.getElementById('reset-filters').addEventListener('click', function () {
search.value = '';
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

// BibTeX frames start without a src; load one the first time its panel is opened
document.addEventListener('show.bs.collapse', function (e) {
  e.target.querySelectorAll('iframe[data-src]').forEach(function (f) {
    f.src = f.getAttribute('data-src');
    f.removeAttribute('data-src');
  });
});

document.querySelectorAll('.well-bib iframe').forEach(function(iframe) {
    iframe.addEventListener('load', function() {
        try {
            var iDoc = iframe.contentDocument || iframe.contentWindow.document;
            iDoc.body.style.margin = '0';
            iDoc.body.style.padding = '0';
        } catch(e) {}
    });
});
</script>
