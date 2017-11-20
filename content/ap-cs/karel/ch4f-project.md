---
title: "4. Robot Drama"
date: 2017-11-17T09:40:50-06:00
draft: false
weight: 55
#type: slide
#theme: white
description: "A skit involving robots making decisions."
---

You are going to make a play in which robots interact.

Documentation:

* [Karel the Robot (all)](http://csis.pace.edu/~bergin/KarelJava2ed/KJRdocs/index.html)
* [Robot](http://csis.pace.edu/~bergin/KarelJava2ed/KJRdocs/kareltherobot/Robot.html)
* [UrRobot](http://csis.pace.edu/~bergin/KarelJava2ed/KJRdocs/kareltherobot/UrRobot.html)

## Assignment in Brief

### Assignment Elements

* One robot interacts with another robot.
* You create a new interface or abstract class for use.
* Robots interact in a non-formulaic way.
* Interesting plot line (please!). It's supposed to be fun.

### Assignment Timeline

* Friday: Outline of the action which will happen. (Check in.)
* Tuesday: You should have at least 3 classes/interfaces written. (Check in.)
* Tuesday after Thanksgiving: project due.



## SchoolBot abstract class

We decided that every robot in school will have four basic functions. 

```java
boolean isStudent();
boolean isTeacher();
boolean isHelpful();
Strategy getHelp();
```
Robots can be students or teachers. If a robot is helpful, then you can
get a Strategy from it. (The idea is that the Strategy will get you help when you "doIt".) 


## StudentBot looks for TeacherBot

To interact with other robots, I suggest using:

* the enhanced `Robot` class
* the `neighbors()` function

### Robot vs UrRobot

Use the `Robot` class instead of `UrRobot`. This lets your robot detect some things in its environment. For example, `nextToARobot()` returns true if there is at least one other robot with the same coordinates. Links to the [Robot](http://csis.pace.edu/~bergin/KarelJava2ed/KJRdocs/kareltherobot/Robot.html) documentation are at the top of this page.

### neighbors

The `myRobot.neighbors()` function returns an `Enumeration`. An Enumeration is an object that is basically a list of items. There is a `nextElement()` function which gives you the next item in the list. (You start before the first item.) There is a `hasMoreElements()` which returns true if there is another element you can get.

{{% notice note %}}
In order to use Enumeration you must include `import java.util.*` at the start of your document.
{{% /notice %}}

Note: Karel the Robot is an old program and [Enumeration](https://docs.oracle.com/javase/7/docs/api/java/util/Enumeration.html) is an old interface. New programs use an [Iterator](https://docs.oracle.com/javase/7/docs/api/java/util/Iterator.html) instead.

