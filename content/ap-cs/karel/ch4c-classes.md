---
title: "4.6 More Classes"
date: 2017-11-09T11:35:15-06:00
draft: false
weight: 48
#type: slide
#theme: white
description: "Three exercises to improve your understanding of classes and interfaces."
---

## Go South

Write a `GoFarStrat` which makes a `BirdBot` fly three times.

We are not going to write a `BirdBot` class, but assume it is already written:
```java
public class BirdBot extends StrategyLayer { 
  ...
  public void fly() { ... }
}
```

The following code should work:
```java
public static void main (String[] args) {
  GoFarStrat flyFar = new GoFarStrat();
  BirdBot robin = new BirdBot(4,1,East,20, flyFar);
  flyFar.doIt(robin); // could be robin.doStrat()
}
```

## AndThenStrat

The `AndThenStrat` is a Strategy that combines two strategies by doing one and then the other. See lines 5-6 in the code sample below for its construction and use.

The following sample code should cause the robot to step and then turn. The `MoveOneStrat` is supposed to make the robot move one step. The `TurnOneStrat` is supposed to mkae the robot turn to the left. You do not need to write either of those strategies; they are just here to illustrate how the `AndThenStrat` works.
{{< highlight java "linenos=inline,hl_lines=5-6" >}}
public static void demoAndThen() {
  UrRobot r = new UrRobot(4,1,East,20);
  Strategy step = new MoveOneStrat();
  Strategy turn = new TurnOneStrat();
  AndThenStrat combine = new AndThenStrat(step, turn);
  combine.doIt( r );
}
{{< /highlight >}}


## ZigStrat

We are going to make a strategy that is called `ZigStrat`. This strategy layers on top of another strategy that we are given and does three things:

* turnLeft()
* (the behavior from the given strategy)
* turnRight()

The following sample code should cause the robot to turn left, move three, and turn right:
```java
public static void main (String[] args) {
  Strategy th = new MoveThreeStrat());
  ZigStrat z = new ZigStrat(th);
  BetterBot bb = new BetterBot(4,1,East,20);
  z.doIt(bb);
}
```


### Background and Additional Information
The [MoveThreeStrat](MoveThreeStrat.java) extends the basic `Strategy` interface from the book:
```java
public interface Strategy { 
   public void doIt(UrRobot r);
}
```

We will use a robot called [BetterBot](BetterBot.java) that has a `turnRight()` method. Do not write your own `turnRight`.

### Extensions

Check to make sure your solution is still good when you add a `public void skip()` method to BetterBot that causes it to move two spaces forward. Make `ZigStrat` turn left, skip, do the other work, turn right, and skip again.

