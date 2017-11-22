---
title: "Karel Hacked"
date: 2017-11-22T14:48:29-06:00
draft: false
#type: slide
#theme: white
---

On GitHub, I have placed a [KarelHRobot.jar](https://github.com/2017-2018-wy-ap-cs/apcs-karel/blob/master/lib/KarelHRobot.jar) that has a hacked `UrRobot` that has the following capabilities:

* `street()`: The current street the robot is on (row = y)
* `avenue()`: The current avenue the robot is on (column = x)
* `direction()`: The direction the robot is facing.
* `beepers()`: The number of beepers the robot has in its beeper bag.

I know some people have already enhanced `UrRobot` with similar capabilities. 
These hacks are to let the rest of you finish your project without learning every
trick of Karel programming.

{{% notice note %}}
There is a sample project `karelPlayProject.drjava` that includes the hacked library. 
It also contains a demo `HackBot.java` that shows some of the functions in action. 
Update to get the most recent code from GitHub.
{{% /notice %}}
