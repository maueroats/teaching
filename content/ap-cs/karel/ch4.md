---
title: "Karel 4"
date: 2017-10-23T10:17:59-05:00
draft: false
weight: 40
description: "Very important chapter: Choreographer, Contractor, Strategy, Spy, Observer. Design patterns in Java."
---

* Monday, October 23, 2017: Read Section 4.1-4.3 and do Exercise 3.5 (DiamondBot) with a Choreographer robot. 

* Tuesday October 24, 2017: Section 4.2 review (abstract class, override methods).
    - Class: make a robot (team) to create [my figure 4.2b ending](4-2b-Abstract-II-End.png) from the [old blog](https://wy-ap-cs.blogspot.com/2014/09/chapter-4.html). Then make a robot (team) to pick up [my figure 4.2b start](4-2b-Abstract-II-Start.png).
    - Homework: Read Section 4.4. 
        - What is the function of an interface? 
        - What does delegation mean in cs?

* Wednesday, October 25, 2017: Section 4.4 (interfaces)
    - Class: review box on page 76 (purpose of interface, no methods in an interface)
    - Class: review box on page 79 (references can point anywhere)
    - Class: "[delegation](https://en.wikipedia.org/wiki/Delegation_(object-oriented_programming))".
    - Assignment: `Forester`. The Forester plants trees and bushes. In the robot world, you see a top view of the forest - tall plants are represented by lots of beepers, short plants are represented by few beepers in a pile. Oak trees are tall (7 beepers in a location). Maple trees are medium height (3 beepers), and bushes are only 1 beeper tall but they take up four locations instead of one. 
          1. Make a Forester interface that has the `doPlanting()` method.
          2. Implement the Forester interface in `OakPlanter`, `MaplePlanter` and `BushPlanter`. 
          3. Demonstrate with a short program that plants two oak trees 5 squares apart, and a maple next to a bush.

* Thursday, October 26, 2017

    - Create two robot classes: `SpeedyMover` and `DropMover`. 
        + SpeedyMover moves two steps when told to move one.
        + DropMover drops a beeper and moves when told to move.
    - Create an interface `ArmyCaricature` that defines the `march()` and `crawl()` methods.
    - Create a `DrillSargent` class that bosses two `ArmyCaricature` robots. The drill sargent should have a `bootCamp(ArmyCaricature a, ArmyCaricature b)` method that tells `a` to do three marches and `b` to do three crawls. 

## Quiz 4.1-4.4 on Friday

You should be able to demonstrate the following skills from Sections 4.1-4.4.

* Create a new class (including constructor from memory).
* Instance variables to remember helper robots.
* Abstract class, then concrete implementation to fill in missing parts.
* Interface: create and implement.
* Comparison of abstract class and interface.
    
## Additional Notes

* Read: [old notes, still good](https://wy-ap-cs.blogspot.com/2014/09/chapter-4.html).

* Android programming has an [AbstractCursor](http://grepcode.com/file/repository.grepcode.com/java/ext/com.google.android/android/5.1.1_r1/android/database/AbstractCursor.java#AbstractCursor) class that handles many commom behaviors. Notice that some of the methods are not there, like:
```java
     abstract public String[] getColumnNames();
```
