---
title: "4.6 FishBot"
date: 2017-11-08T13:13:15-06:00
draft: false
weight: 47
#type: slide
#theme: white
description: "A fish robot that alternates between two strategies so it is harder for predators to predict its motion."
---

## Purpose

The purpose of this assignment is to motivate the use of Strategies instead of "hard-coding" individual behavior into an object.

## Introduction

A fish that is startled moves to get away from a predator. If a fish
always does the same behavior to escape, it is easy for a predator to
predict what will happen and the fish will get eaten. In order to
avoid getting eaten, a fish alternates between darting forward and darting to the left. 

* `DartForward`: a `Strategy` of moving forward three times
* `DartLeft` :a `Strategy` of turning left and moving forward once

* `FishBot` is a kind of (our) `StrategyLayer` that remembers two
  different strategies and alternates betweewn them.
    + `public void startle()` activates the startle reflex, running the current strategy for escape
    + `public void swapStrategy()` switches between the two strategies that the fish knows
    
    
## Difficulties

* Confusion between `StrategyLayer` and `Strategy`. 
    - How are they actually related?
    - Can both be created? (`new Strategy()` vs `new StrategyLayer(...)`)
* What is the relationship between `FishBot` and `StrategyLayer`?
* Too-specific names for things: 
    - `iFishBotStrategy` for the interface
    - variables of type `DartStrategy` and `DodgeLeftStrategy` instead of just `Strategy`

Some of these difficulties should have come up with the [ArmyCaricature]({{% relref "ap-cs/karel/ch4a.md" %}}), so we need to revisit that!

