---
title: "Home"
layout: homelay
sitemap: false
permalink: /
---

<style>
code {padding: 6px 8px; font-size: 90%;}
</style>

Welcome to my personal homepage! I am currently working as an assistant professor in the [Future Everyday](https://www.tue.nl/en/research/research-groups/future-everyday) group of the department of [Industrial Design](https://www.tue.nl/en/our-university/departments/industrial-design/) of [TU Eindhoven](https://www.tue.nl). My focus is on AI-driven interaction between automated vehicles, people inside of automated vehicles and other road users.

During 2018-2022 I was postdoctoral researcher in the [Human-Robot Interaction](https://www.tudelft.nl/3me/over/afdelingen/cognitive-robotics-cor/research) group at the department of [Cognitive Robotics](https://www.tudelft.nl/3me/over/afdelingen/cognitive-robotics-cor) of [TU Delft](https://www.tudelft.nl). My focus was on Human Factors of communication between automated vehicles and vulnerable road users (pedestrians, cyclists). I am a big advocate of open science (hence this website hosted on GitHub) and I volunteered as a [data champion](https://openworking.wordpress.com/2019/08/19/switch-gear-drive-the-uptake-of-open-science-within-your-research-team) of the 3mE faculty of TU Delft. I joined TU Delft in August 2014 to work within the [HFAuto](http://hf-auto.eu) project as a Marie Curie Fellow. During my PhD, my aim was to develop a human-machine interface for highly automated driving, focusing on the auditory modality. I defended [my PhD](/_publications/bazilinskyy2018auditoryinterface.pdf) in December 2018.

Before starting my PhD on human factors, I was doing something completely different. I concluded Erasmus Mundus Double MSc in Dependable Software Systems with double distinction at the [University of St Andrews](https://www.st-andrews.ac.uk) (Scotland) and [Maynooth University](https://www.maynoothuniversity.ie) (Ireland) in 2014. I wrote two dissertations within this degree where I evaluated the [implications of porting a strongly-encapsulated programming language Insense to multi-core systems](/_publications/bazilinskyy2013multi.pdf) and the [impact of the cache on multi-threaded data-sharing applications](/_publications/bazilinskyy2014impact.pdf). I enrolled in the BSc course in Computer Science at the [National University of "Kyiv-Mohyla Academy"](https://www.ukma.edu.ua/eng/) (Ukraine). After the 1st year of the course, I decided to experience international mobility and transferred to a BEng programme in Information Technology at [Mikkeli University of Technology](https://www.xamk.fi) (Finland). I concluded the degree in 2012, specialising in Software Engineering. In my thesis, I focused on the development of [a customisable multitenant web form for the bioenergy sector](/_publications/bazilinskyy2012customisable.pdf). After my MSc, I decided to switch my research focus and enrolled in the PhD project on automated driving, as I was looking for a more hands-on area that has a direct impact on our world and great potential to save millions of people.

I like to be active and engage in interesting projects. During 2018–2021, I was a director of data science research at [SD-Insights](https://sd-insights.eu). I was a chair (2017–2021) and a vice-chair (2021–2022) of the [Bridging Science and Business (BSB) working group](https://www.mariecuriealumni.eu/groups/bridging-science-and-business) of [Marie Curie Alumni Association (MCAA)](https://www.mariecuriealumni.eu). I was also a chair (2015–2017) and a vice-chair (2017–2019) of the [BeNeLux chapter](https://www.mariecuriealumni.eu/groups/benelux-chapter) of MCAA. I am currently a member of the board with a position of the treasurer of the association (since 2022). I was a member of the Capacity building task-force of [(ESAA)](https://www.esaa-eu.org) (2018–2019), a board member of the Eurasian chapter (2017–2019), a member of the Communications and Course Quality Advisory Board (2017–2018) teams, and a director of [Research and Innovation (R&I) unit](https://www.em-a.eu/unit-riu) (2019–2021) of [Erasmus Mundus Association (EMA)](https://www.em-a.eu).

### Multi-user communication in traffic
I am currently engaged in research on communication between multiple automated vehicles and multiple vulnerable road users. Most of experiments in current research features 1, maybe 2, human participants. But, think about driving around a town in real life. Traffic situations are very complicated. And being able to perform experiments with 3, 4, ..., 16 participants is essential for understanding the mechanics of communication of situation awareness/collaborative decision making/collaboration in both modern and future traffic. To enable such research, I present [an open-source simulator](https://github.com/bazilinskyy/coupled-sim). It supports a virtually unlimited number of human participants and fine-tunes for high precision data logging. It is aimed for, but not limited to, academic research.

<div class="row" style="text-align:center">
  <iframe style="display:inline-block; border-radius: 5px; border:0px solid #FFF; width: 95%; height: 246px" src="https://www.youtube.com/embed/W2VWLYnTYrM?playlist=W2VWLYnTYrM&loop=1&autoplay=1&mute=1" frameborder="0" allowfullscreen></iframe>

  Demo of [coupled simulator](https://github.com/bazilinskyy/coupled-sim) with 3 agents in the same traffic scene.
</div>

### Free time
* 🏃‍♂🚴‍♂️🏊‍♂️ Running, [cycling](https://www.wielervrienden.nl/profiel/pavlo-7126007), swimming, cross-country skiing, hiking. Like, [a lot of it](https://www.strava.com/athletes/bazilinskyy).
* 🗺️ Travelling (especially through [couchsurfing](https://www.couchsurfing.com/people/pavlo.bazilinskyy)/[bewelcome](https://www.bewelcome.org/members/bazilinskyy)/[trustroots](https://www.trustroots.org/profile/bazilinskyy), [travel map](https://beeneverywhere.net/user/bazilinskyy)).
* 💻 Coding ([github](https://github.com/bazilinskyy)).
* 📖 Reading ([goodreads](https://www.goodreads.com/user/show/5571310-pavlo-bazilinskyy)).
* ♟️ Chess ([chess.com](https://www.chess.com/member/bazilinskyy)).
* 🎸 Music ([last.fm](https://www.last.fm/user/Hollgam)). I also play sax alto and guitar.
* 📺 Films and tv series ([imdb](https://www.imdb.com/user/ur16534776), [trakt](https://trakt.tv/users/bazilinskyy)). Somebody likes tv, surprise! 😬

<br/>

<div class="well-md">
  <h3>Funding</h3>
  <div style='display:block; text-align:center; margin-left:auto; margin-right:auto;'>
   {% for funder in site.data.funders %}{% if funder.url %}<a href="{{funder.url}}" target="_blank"><img src='/images/logos/{{ funder.image }}' style='max-height: 70px; max-width: 170px;'/></a>{% else %}<img src='/images/logos/{{ funder.image }}' class='mycenter' style='max-height: 70px; max-width: 170px;'/>{% endif %}   {% endfor %}
  </div>
</div>
