---
layout: publication
title: "Living mobility datasets from public video: A continuously running pipeline for crashes, near-collisions and pedestrian environments"
description: "Automated vehicles need data on crashes and on where people walk, but research driving datasets contain few crashes and come from few cities. Dashcam and…"
authors: Alam, M. S., Hoggenmueller, M., Bazilinskyy, P.
pdf: alam2026automated
image: alam2026automated.jpg
display: Submitted for publication.
year: 2026
# doi:
tags: [preprint, artificial-intelligence, computer-vision, dashcam, pedestrian, dataset]
code: https://github.com/crowd-dataset/car-crash-yt
suppmat: https://github.com/crowd-dataset/walking-yt
abstract: "Automated vehicles need data on crashes and on where people walk, but research driving datasets contain few crashes and come from few cities. Dashcam and walking videos on YouTube show both, but they must be screened, cut into segments and labelled before use. We present a pipeline that does this without manual work and keeps running, so the datasets grow as new videos are uploaded. A language model screens each video’s title and description, a video vision-language model (VLM) checks the cuts and labels each segment, and a location is recorded only when the video states it. Every decision is stored with its evidence, so each segment is traceable to its source video. We apply the pipeline to road traffic crashes and to walking. The snapshot of 9 November 2026 holds 74,315 crash and near-collision segments (295.9 h) from 2,848 videos in 177 countries, and 63,993 walking segments (3,088.9 h) from 3,496 videos in 103 countries. In a validation by two independent reviewers, the model’s camera view, time of day and weather agreed with them in 94–97% of crash clips, its walking decisions in all walking clips, and the recorded locality matched the footage in 82 of 87 clips."
---
