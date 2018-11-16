---
title: "3. Classes Quiz"
date: 2018-11-15T21:49:27-06:00
weight: 40
draft: false
#type: slide
#theme: white
description: "Quiz on basic class definition, GridWorld construction."
---

You may not use any notes or old classes to help you. You should start
with the BlueJ projects in the [`ap-cs` Github
repository](https://github.com/2018-2019-WY-AP-CS/ap-cs), whichyou can
get by copy and pasting the code or running `./one-time` and then `git
pull upstream master`.

##  ZenoAdder

The `ZenoAdder` is not in GridWorld, it is just a class. Make it 
normally, but do not try to put it in the grid. A `ZenoAdder`
begins at a given initial x-coordinate on the number line. 

* The `report()` method returns the current location.  
* The `hut()` method updates the location by adding 1/n on move number n.

```java
ZenoAdder a = new ZenoAdder(5.2);
a.hut();
a.report();  // 5.2 + 1/1 = 6.2
a.hut();
a.report();  // 6.2 + 1/2 = 6.7
a.hut();
a.hut();
a.report();  // 6.7 + 1/3 + 1/4 = 7.28333...
// 
```

The `System.out.println(value);` method will let you print your
location in a visible way.

## DashBug

The DashBug is in GridWorld.

1. The `DashBug` walks `steps` times with the ordinary Bug `act()` method,
and then walks for two steps using the `move()` method. The cycle is
repeated `cycle` times.

2. A `DashBug` made without specifying the number of steps or cycles
   should repeat 3 steps in two cycles.

When the bug is done moving it should be stationary.

The constructors should let the code below work:

```java
int steps = 4;
int cycle = 3;
Bug c = new DashBug(steps, cycle);
Bug d = new DashBug();
world.add(new Location(10,3), c);
world.add(new Location(10,4), d);
[...]
```

