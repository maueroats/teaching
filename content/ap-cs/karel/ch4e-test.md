---
title: "4. Test"
date: 2017-11-14T08:21:12-06:00
draft: false
weight: 51
#type: slide
#theme: white
---

# Karel Chapter 4 Test

You may not use any resource materials for this test.

## Partners

New laws have been passed and now robots can get married. A robot who
wants to get married must implement the `Partner` interface. The
Partner interface consists of a `public UrRobot spouse()` method as
well as a `public void setSpouse(Partner x)` and a `public boolean
isAvailable()` method. When robots are delivered from the factory they
do not have a partner.

1. Write the `Partner` interface.

2. Create a `LBot` that implements the `Partner` interface.

## Marriage

3. The `JusticeOfThePeaceBot` can marry robots. 
The function is `public boolean marry(Partner a, Partner b)`. 
    - Write this function. 
    - If either robot is unavailable, do not marry them!
    - Return true if the partners are married, false if the marriage fails.

## Relationships

Do one of the following:

4. (Know 4.8) The `FindRelationship` strategy is: move forward one step, if there is a robot there and it is available, change to NoStrategy, otherwise continue looking.

5. (No 4.8) The `Court` strategy is created by `Strategy s = new Court(Partner x)`. The strategy checks to see if the partner is available, and if so it puts a beeper down. Write the `Court` strategy.


