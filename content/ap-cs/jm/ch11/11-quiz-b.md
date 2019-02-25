---
title: "11 Quiz B"
date: 2019-02-25T08:50:40-06:00
#weight: 
draft: false
#type: slide
#theme: white
---

* `Clothes` interface has `int fashion()` and `int warmth()`.

* `HeadCovering` implements the `Clothes` interface. Its constructor
  sets fashion and warmth.

* `WoolClothes` takes in a `Clothes` class in its constructor. It adds 5 to
  the warmth provided by the Clothes when they are made of wool.

* `Person` is an abstract class with a `String name` field and a
  `String getName()` function, as well as abstract methods `int
  getWarmth()` and `int getFashion()`. Constructor sets the name.
  
* `PlainPerson` is a subclass of `Person` with a warmth of 90 and a
  fashion of 50, always.
  
* `BigFashionPerson` is a subclass of `Person` that has an
  `ArrayList<Clothes>`. 
  
      * Constructor takes in a name and an arraylist of clothes.
      * Their warmth is the sum of the warmth of their clothes. 
      * Their fashion is the *minimum* of the fashion of their clothes. 

