---
title: "Karel 4.5-4.6"
date: 2017-10-30T09:52:53-05:00
draft: false
weight: 41
description: "Great chapter: Strategy, Spy, Observer. Design patterns in Java."
---

## NeighborTalker

Read Section 4.5.

* What is the purpose of the `private BeeperPutter neighbor` field of a `NeighborTalker`?
* Could the `neighbor` field be `null` when you run the `distributeBeepers()` method?
* Draw a box and arrow diagram showing the different robots that `aRobot` points to as the main method on the top of page 82 runs.
* How could you modify the `distributeBeepers()` method so that the last robot in the line puts their beeper down and moves before the second to last robot in line, etc., so the first robot in line is the last one to put their beeper down and move.

## Robot Horde Project

Make a "Robot Horde" where each robot sends a `swarm()` message to the 0, 1, or 2 robots that it controls. 

{{< figure src="small-horde.jpg" >}}

## StrategyLayer (4.6)

(Two days.)

* Does the `StrategyLayer` robot implement the `Strategy` interface? Explain in what way your answer is logical.

* Casts
     - Clark Kent / Superman analogy
     - Can a cast change an UrRobot into a HarvesterBot?
     - Is a cast useful to change a HarversterBot into an UrRobot?
     - What happens when you cast an UrRobot into something that it is not?

* How can you use "advanced" robot methods in a Strategy?

* Misc: The three-hands method of exchanging two items.

