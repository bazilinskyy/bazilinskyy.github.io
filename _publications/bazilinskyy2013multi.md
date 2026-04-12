---
layout: publication
sitemap: false
title: "Multi-core Insense"
authors: Bazilinskyy, P.
pdf: bazilinskyy2013multi
image: bazilinskyy2013multi.jpg
display: "Thesis for: Erasmus Mundus Double MSc in Dependable Software Systems"
year: 2013
tags: [thesis, cs]
code: https://github.com/bazilinskyy/multicore-insense-runtime
abstract: "This project set out to investigate the benefits of using private heaps for memory management and static thread placement for optimising performance and cache usage. For this study, Insense, which is a component-based programming language developed in the University of St Andrews that abstracts over complications of memory management, concurrency control and synchronisation, was used (Dearle et al. 2008). Two memory management schemes are under investigation: use of a single shared heap and use of multiple private heaps. Further, three thread placement schemes are designed and implemented: 1) even distribution among cores; 2) placing all components on a single core; 3) locating Insense components based on frequency of inter-component communication. Furthermore, several elements of this investigation are worth emphasizing. With regard to allocation and deallocation of memory taking place in component instances running on different cores, the efficiency of using a private heap for each component resulted in speedup by a factor of 16. Then, utilising private heaps reduces a number of L1 cache misses by ~30%. Distributing components over cores according to communication pattern, for the most part performed similar to allowing the OS to perform thread placement dynamically according to load balance. In cases where no exchange of data between components takes place, static placement outperformed because there is no computation which may make load balancing dynamic placement of threads under control of the OS difficult. In this case, the static placement scheme was faster than dynamic balancing by a factor of 2.4."
---
