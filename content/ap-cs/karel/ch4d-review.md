---
title: "4.6 MurderBot"
date: 2017-11-13T09:52:14-06:00
draft: false
weight: 49
#type: slide
#theme: white
description: "Review exercises for class design."
---

## MurderBot

* A `MurderBot` is a kind of `StrategyLayer` with two additional abilities:
    - `public void stab()`: place two beepers
    - `public void flee()`: move one step

* The `KillerStrategy` is a kind of `Strategy` that makes the robot it controls `stab` the first time the strategy is invoked (via `doStrat`, which will call `doIt`). Every subsequent time the robot is told to `doStrat()`, it should `flee`.

* Make sure the same `doStrat()` call causes one stab or one flee each time.

* Test your `MurderBot` with 8 calls to `doStrat()`.

* Challenge yourself: this can be done without variables (except what is built into the StrategyLayer).

* Advanced: use the techniques the Spy in Section 4.8 to cause the
`stab` action to find another robot on the same corner as the
MurderBot and turn it off.

## ViciousMurderBot

Create a kind of MurderBot that places six beepers when it is told to stab, instead of just two. 

