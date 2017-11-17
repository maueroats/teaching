---
title: "4.* Advanced"
date: 2017-11-17T09:40:32-06:00
draft: false
weight: 50
#type: slide
#theme: white
---

## Undoing

Page 100, exercise 12 - the robot that has the undo command. I used the idea of a Decorator strategy. 

## Simultaneous Action

Chapter 8 in the text shows how to make more than one robot act at the same time.  See the [MultiThreadBot](https://github.com/2017-2018-wy-ap-cs/apcs-karel/blob/master/MultiThreadBot.java) on the class GitHub.

A brief summary is:

* `World.setupThread(robot)` prepares the robot to act in its own thread.

* `World.startThreads()` calls the `run()` method for every robot that is set up as threading using the command above.

