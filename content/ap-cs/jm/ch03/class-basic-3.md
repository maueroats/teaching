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
         
2. `PayMeBug`: Write a class called `PayMeBug` that is a kind of `Bug`. Its
constructor should take in a number of steps (N) the bug will go when paid.
Write a method named `pay()` to your `PayMeBug`.
After it is paid, the next N times its act method is called (maybe by
hitting the "Step" button), it moves forward like an ordinary
bug. Then it stops and waits to be paid again.

        Bug s = new NStep(3);
        Location where = new Location(1,5);
        world.add(where, s); 
        s.pay(); // now moves

3. `IRBug`. Write a class `IRBug` for "isosceles right triangle
   bug". The constructor should take in the number of steps on one leg
   of the triangle. When the bug's `act()` method is called, it uses
   the Bug's `move()` method to move along each side and uses the
   appropriate number of `turn()` calls to turn at each corner. It can
   repeat the triangle forever.

        Bug t = new IRBug(4);
        Location where = new Location(2,7)
        world.add(where, t);
        [...]
        
   It is fine if the `IRBug` crushes flowers and rocks instead of turning.
