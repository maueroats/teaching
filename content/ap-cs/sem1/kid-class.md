---
title: "Kid Class"
date: 2019-01-29T07:27:15-06:00
#weight: 
draft: true
#type: slide
#theme: white
---

A `Kid` has a `String` name, an `int` age, and a `String` interests.

To write:

* Constructor: includes all of information above.
* Constructor: you are allowed to omit the interests, in which case teenagers (ages 13-19) have an interest of "listening to music" and everyone else has an interest of "having fun".
* `public String introduce()`
* `public void growUp()`: Increases age by three.


Example usage:

         Kid alice = new Kid("Alice", 13, "skating");
         String s = alice.introduce();
         System.out.println(s);
         // "I'm Alice. I am 13 years old and like skating."
         alice.growUp(); // now 16

         Kid ken = new Kid("Ken", 16);
         String ss = ken.introduce();
         System.out.println(ss);
         // "I'm Ken. I am 16 years old and like listening to music."
    
