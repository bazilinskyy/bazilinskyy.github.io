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

#### Crowdsourced Human Factors experiments
  
During my PhD on Human Factors, I was astonished to realise that the majority of research features features a sample of <i>"10 white male highly educated students from Europe with an average age of 21.5 years"</i>. I thought that it was not a right way to design and develop systems, which primary function is to save lives and be used by the public (especially in developing countries, which are impacted the most by unsafe traffic). I launched my first [study](/publications/bazilinskyy2015auditory.pdf) using a novel method of crowdsourcing already in the 2nd month of my PhD project. 1,205 respondents from 91 countries expressed their opinions about current and hypothetical auditory interfaces. In another [study](/publications/bazilinskyy2017analyzing.pdf), I implemented synthesised speech in a crowdsourcing survey—an innovative approach, as most researchers in the domain focus on non-speech feedback. I developed a new framework to reliably present stimuli to participants online and replicated several well-established studies but with a much larger sample size of 2669 participants from 95 countries. Then, I developed a JavaScript framework based on the [jsPsych project](https://www.jspsych.org/7.0/) for accurate online measurements of reaction times and asked 20000 participants to react to 176 trials featuring [auditory, visual, and multimodal stimuli](/publications/bazilinskyy2018crowdsourced.pdf). Then, I adapted the [TurkEyes](https://turkeyes.mit.edu) library to receive accurate measurement of eye gazes from a browser without any eye trackers (see video on the left for a demonstration of animated heatmaps of 2000 pedestrians looking at 107 traffic scenes with different exposure times in a recent [study](/publications/bazilinskyy2021visual.pdf)). I also published the [source code with an extendable framework](https://github.com/bazilinskyy/gazes-crowdsourced) for crowdsourced recording of eye gazes. Such code can be used in combination with [accurate measurement of keypresses](https://github.com/bazilinskyy/crossing-crowdsourcing). Being able to conduct crowdsourced research proved to be especially useful during the pandemic.

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
