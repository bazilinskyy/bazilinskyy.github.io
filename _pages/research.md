---
title: "Research"
layout: gridlay
sitemap: false
permalink: /research/
---

# Research

<div class="rowl1">
  <img src="{{ site.url }}{{ site.baseurl }}/images/research/multi_user_communication.jpg" class="img-responsive" style="float: left; border-radius: 5px; width: 280px; height: 158px" />

#### Multi-user communication in traffic
  
I am currently engaged in research on communication between multiple automated vehicles and multiple vulnerable road users. Most of the experiments in current research feature 1, maybe 2, human participants. But, think about driving around a town in real life. Traffic situations are very complicated. Being able to perform experiments with 3, 4, ..., 16 participants is essential for understanding the mechanics of communication of situation awareness/collaborative decision making/collaboration in both modern and future traffic. To enable such research, I present [an open-source simulator](https://github.com/bazilinskyy/coupled-sim) supporting a virtually unlimited number of human participants and fine-tuned for high precision data logging. It is aimed at, but not limited to, academic research.

  <div class="row" style="text-align:center; margin-bottom: 0px;">
  <iframe style="display:inline-block; border-radius: 5px; border:0px solid #FFF; width: 97%; height: 358px" src="https://www.youtube.com/embed/W2VWLYnTYrM?playlist=W2VWLYnTYrM&loop=1&autoplay=1&mute=1" frameborder="0" allowfullscreen></iframe>
  
Demo of [coupled simulator](https://github.com/bazilinskyy/coupled-sim) with 3 agents in the same traffic scene. One agent is wearing a motion suit and one has a head-mounted display.
  </div>
  <ul style="overflow: hidden">
  </ul>
</div>

<div class="rowl1">
  <div class="img-responsive" style="margin-top: 15px; margin-right: 19px; float: left"><iframe src="https://www.youtube.com/embed/ZroKe9dKQvs?playlist=ZroKe9dKQvs&loop=1&autoplay=1&mute=1" style="width: 280px; height: 158px; border-radius: 5px" frameborder="0" allowfullscreen></iframe></div>

#### Crowdsourced human factors experiments
  
During my PhD on human factors, I was astonished to realise that the majority of research features features a sample of <i>"10 white male highly educated students from Europe with an average age of 21.5 years"</i>. I thought that it was not a right way to design and develop systems, which primary function is to save lives and be used by the public (especially in developing countries, which are impacted the most by unsafe traffic). I launched my first [study](/publications/bazilinskyy2015auditory.pdf) using a novel method of crowdsourcing already in the 2nd month of my PhD project. 1,205 respondents from 91 countries expressed their opinions about current and hypothetical auditory interfaces. In another [study](/publications/bazilinskyy2017analyzing.pdf), I implemented synthesised speech in a crowdsourcing survey—an innovative approach, as most researchers in the domain focus on non-speech feedback. I developed a new framework to reliably present stimuli to participants online and replicated several well-established studies but with a much larger sample size of 2669 participants from 95 countries. Then, I developed a JavaScript framework based on the [jsPsych project](https://www.jspsych.org/7.0/) for accurate online measurements of reaction times and asked 20000 participants to react to 176 trials featuring [auditory, visual, and multimodal stimuli](/publications/bazilinskyy2018crowdsourced.pdf). Then, I adapted the [TurkEyes](https://turkeyes.mit.edu) library to receive accurate measurement of eye gazes from a browser without any eye trackers (see video on the left for a demonstration of animated heatmaps of 2000 pedestrians looking at 107 traffic scenes with different exposure times in a recent [study](/publications/bazilinskyy2021visual.pdf)). I also published the [source code with an extendable framework](https://github.com/bazilinskyy/gazes-crowdsourced) for crowdsourced recording of eye gazes. Such code can be used in combination with [accurate measurement of keypresses](https://github.com/bazilinskyy/crossing-crowdsourcing). Being able to conduct crowdsourced research proved to be especially useful during the pandemic.

<ul style="overflow: hidden">
  </ul>
</div>

<div class="rowl1">
  <div class="img-responsive" style="margin-top: 15px; margin-right: 19px; float: left"><iframe src="https://www.youtube.com/embed/NipvoDg0Nyk?playlist=NipvoDg0Nyk&loop=1&autoplay=1&mute=1" style="width: 280px; height: 158px; border-radius: 5px" frameborder="0" allowfullscreen></iframe></div>

#### YouTube as the data source for research on global traffic behaviour

The interactions between future cars and pedestrians should be designed to be understandable and safe worldwide. Crowdsourcing helps to go beyond WEIRD (Western, educated, industrialised, rich, developed) studies. But we can go beyond that and cover the whole world to have a true understanding of how people behave around the globe and get a better grasp of how future cars and transportation infrastructure should be designed. We live in the 21st century, where the internet has become ubiquitous and universally adopted. Accessibility to technology created a phenomenon of ASMR driving videos. I established work on the population of the “City Road Observations With Dashcams” (CROWD) [dataset](https://github.com/Shaadalam9/pedestrians-in-youtube), which includes 7932 hand-picked hours of day and night urban dashcam footage from 3926 towns and cities in 235 sovereign states and dependent territories, collected from 16153 videos. Using YOLO, we analysed aggregated pedestrian behaviour both on the [city](/publications/alam2025crossing.pdf) and [country](/publications/alam2025pedestrian.pdf) levels. And we are investing in going beyond YOLO to have a more precise and complete understanding of what exactly happens on the streets of cities on all continents.

<ul style="overflow: hidden">
  </ul>
</div>

<div class="rowl1">
  <img src="{{ site.url }}{{ site.baseurl }}/publications/alam2025cross.jpg" class="img-responsive" style="float: left; border-radius: 5px; width: 280px; height: 158px" />

#### Do we need human participants for human factors research?

The logical next step is to question whether we even need human participants to conduct (basic) human factors research. Of course, some hypothesis must be tested in a very controlled environment with expensive eye trackers. But, some research questions can maybe be answered through the "wisdom of humanity up until a certain point in time", which arguably what AI (LLM) is. In this [study](/publications/driessen2024putting.pdf), we used the GPT-4V vision-language models to compare LLM-based assessment of risk with findings from a [crowdsourced study](/publications/dewinter2023predicting.pdf) with 1378 participants. The conclusion was that the population-level human risk can be predicted using AI with a high degree of accuracy. We also [explored](/publications/alam2025cross.pdf) the use of 11 LLMs to evaluate external human-machine interfaces (eHMIs) in automated vehicles.

  <ul style="overflow: hidden">
  </ul>
</div>

<div class="rowl1">
  <div class="img-responsive" style="margin-top: 15px; margin-right: 19px; float: left"><iframe src="https://www.youtube.com/embed/isjbqXs2g7k?playlist=isjbqXs2g7k&loop=1&autoplay=1&mute=1" style="width: 280px; height: 158px; border-radius: 5px" frameborder="0" allowfullscreen></iframe></div>

#### Portable sensor to collect information on the state of the traffic environment

During my work at SD-Insights, I developed a portable sensor to collect information on the state of the environment called NEXTeye. It is based on [Mapbox Vision SDK](https://www.mapbox.com/vision) and [NVIDIA Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano-developer-kit). The sensor is plug-n-play, retrieves vehicle dynamics data, and performs real-time scene segmentation and object detection. The portability of NEXTeye allows its use not only inside of a car but also as a wearable by vulnerable road users. Multiple such sensors can be connected and synchronised.

  <ul style="overflow: hidden">
  </ul>
</div>

<div class="rowl1">
  <img src="{{ site.url }}{{ site.baseurl }}/images/research/auditory_feedback_ad.jpg" class="img-responsive" style="float: left; border-radius: 5px; width: 280px; height: 158px" />

#### Auditory feedback for automated driving
  
My intrinsic motivation to do a PhD stemmed from the fact that automated vehicles have the potential to prevent virtually all road fatalities. To achieve that, automated vehicles must collaborate with humans inside and outside the vehicle. During [my PhD](/publications/bazilinskyy2018auditoryinterface.pdf) I focused on auditory feedback for automated driving. With on-road and driving simulator studies, I showed that multimodal feedback that takes the urgency of the traffic situation into account could support AV-driver collaboration effectively.

  <ul style="overflow: hidden">
  </ul>
</div>
