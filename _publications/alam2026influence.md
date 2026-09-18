---
layout: publication
title: "Influence of rudder action resolution on autonomous ship path following"
description: "Rudder action resolution directly influences how a deep reinforcement learning controller balances path tracking and steering demand. This study compares…"
authors: Alam, M. S., Bazilinskyy, P.
pdf: alam2026influence
image: alam2026influence.jpg
display: Submitted for publication.
# year: 
# doi: 
tags: [preprint, artificial-intelligence, robotics]
code: https://github.com/Shaadalam9/shipRL-actionresolution
# suppmat: 
abstract: "Rudder action resolution directly influences how a deep reinforcement learning controller balances path tracking and steering demand. This study compares three autonomous ship controllers: a Deep Q Network (DQN) with three discrete rudder commands, a DQN with five discrete commands, and a Proximal Policy Optimization (PPO) controller with continuous rudder control. All controllers are evaluated on the same three degree of freedom KRISO Container Ship model using common observations, reward formulation, actuator limits, and performance metrics. In calm water, DQN 3 achieves the lowest mean cross track RMSE of 1.16L, while PPO gives the lowest mean rudder demand of 0.16. Under wind and wave disturbances, PPO achieves the lowest mean RMSE of 0.73L and the lowest mean rudder demand of 0.17. In model scale experiments, PPO records the smallest tracking error at 0.79L, compared to 0.83L for DQN 3 and 0.86L for DQN 5. In a tightening spiral, DQN 3 reaches 32 of 40 waypoints, compared to 28 for PPO and 27 for DQN 5."
---
