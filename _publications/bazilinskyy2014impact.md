---
layout: publication
sitemap: false
title: "Impact of cache on data-sharing in multi-threaded programmes"
authors: Bazilinskyy, P.
pdf: bazilinskyy2014impact
image: bazilinskyy2014impact.jpg
display: "Thesis for: Erasmus Mundus Double MSc in Dependable Software Systems"
year: 2014
tags: [thesis, computer-science]
code: https://github.com/bazilinskyy/cache-mt
abstract: "This thesis answers the question whether a scheduler needs to take into account where communicating threads in multi-threaded applications are executed. The impact of cache on data-sharing in multi-threaded environments is measured. This work investigates a common base–case scenario in the telecommunication industry, where a programme has one thread that writes data and one thread that reads data. A taxonomy of inter-thread communication is defined. Furthermore, a mathematical model that describes inter-thread communication is presented. Two cycle–level experiments were designed to measure latency of CPU registers, cache and main memory. These results were utilised to quantify the model. Three application–level experiments were used to verify the model by comparing predictions of the model and data received in the real-life setting. The model broadens the applicability of experimental results, and it describes three types of communication outlined in the taxonomy. Storing communicating data across all levels of cache does have an impact on the speed of data–intense multi-threaded applications. Scheduling threads in a sender–receiver scenario to different dies in a multi-chip processor decreases speed of execution of such programmes by up to 37%. Pinning such threads to different cores in the same chip results in up to 5% decrease in speed of execution. The findings of this study show how threads need to be scheduled by a cache-aware scheduler. This project extends the author’s previous work, which investigated cache interference."
---
