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
Partner interface consists of a `public Partner getSpouse()` method as
well as a `public void setSpouse(Partner x)` and a `public boolean
isAvailable()` method. When robots are delivered from the factory they
do not have a partner.

1. Write the `Partner` interface.

    - getSpouse: return the current spouse
    - setSpouse: make the current spouse be the given robot
    - isAvailable: false if the Partner has a spouse

2. Create a `LBot` that implements the `Partner` interface. Example test code:

```java
public static void main (String[] args) {
   LBot sally = new LBot(4,2,East,10);
   LBot harry = new LBot(5,2,East,4);
   sally.setSpouse(harry);
   if (sally.getSpouse() != harry) {
       System.err.println("Sally just married Harry. What's going on?");
   }
   if (sally.isAvailable()) {
       System.err.println("Sally should not still be available!");
   }
}
```

## Marriage

3. The `JusticeOfThePeaceBot` can marry robots. 
The function is `public boolean marry(Partner a, Partner b)`. 
    - Write this function. 
    - Only marry if both robots are available.
    - If either robot is unavailable, do not marry them!
    - Return true if the partners get married, false if the marriage fails.

```java
public static void testMarry() 
{
   LBot sally = new LBot(4,2,East,10);
   LBot harry = new LBot(5,2,East,4);
   JusticeOfThePeaceBot judge = new JusticeOfThePeaceBot(1,1,East,0);
   
   boolean gotMarried = judge.marry(sally,harry);
   
   if ( ! gotMarried 
       || sally.getSpouse() != harry 
       || harry.getSpouse() != sally ) 
   {
       System.err.println("they did not get married!?");
   }
   
}
```

## Relationships

Do one of the following:

4. (Know 4.8) The `FindRelationship` strategy is: move forward one step, if there is a robot there and it is available, change to NoStrategy, otherwise continue looking.

5. (No 4.8) The `Courting` strategy is created by `Strategy s = new Courting(Partner x)`. The strategy checks to see if the partner is available, and if so it puts a beeper down. Write the `Courting` strategy.

```java
public static void testCourt()
{
   LBot sally = new LBot(4,2,East,10);
   LBot harry = new LBot(5,2,East,4);
   
   Courting c = new Courting(sally);
   c.doIt(harry); // harry should place a beeper
   sally.setSpouse(sally); // married herself to make harry go away
   c.doIt(harry); // harry should do nothing
}
```
