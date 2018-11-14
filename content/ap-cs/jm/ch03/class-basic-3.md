---
title: "3. Writing Basic Classes 3"
date: 2018-11-14T08:46:30-06:00
weight: 30
draft: false
#type: slide
#theme: white
description: "The last sequence of practice classes."
---

You can look up the methods available in the GridWorld classes. There
is a 
[directory of all
methods](http://horstmann.com/gridworld/javadoc/). The most useful
ones are Actor, Bug, and Flower.


1. `CreepingCharlie`: A subclass of flower that has the normal
   behavior of a flower, except every third time it is asked to
   `act()`, it changes its direction by 45 degrees. (See documentation
   for Actor.)
   
         Flower c = new CreepingCharlie();
         
2. `NStep`: Add a method named `go()` to your `NStep` bug.
   Telling the bug `go()` activates it. After it is
   activated, it moves N times (one every time it acts) and then stops. 
   Set N in the constructor.
   
        Bug s = new NStep(3);
        s = new Location(1,5);
        world.add(where, s); 
        s.step(); // then moves 3 times forward
