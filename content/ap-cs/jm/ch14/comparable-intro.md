---
title: "14. Comparable Intro"
date: 2019-02-26T09:45:33-06:00
weight: 10
draft: false
#type: slide
#theme: white
---

A class implements the `Comparable` interface when there is a way to
decide whether one object of the class is greater than another. The
`compareTo` method is the way to find out how the two classes
compare. 

<!--more-->

The `first.compareTo(second)` method call gives a positive number when
the first object is greater than the second. Summary of meaning of results:

* positive: first is greater than second
* negative: first is less than second
* zero: first equals second

## Important Examples

A good example to remember is comparing `Integer` objects. 

     Integer a = new Integer(5);
     Integer b = new Integer(12);
     int c = a.compareTo(b); // results in 5-12 = -7

Another example is `String` objects, where strings that are later in
the alphabet are like larger numbers. In the code below, do you expect
the result to be positive, negative, or zero? Why?

     int result = "bog".compareTo("aardvark);

## Details

Technically, the Comparable interface has a class parameter `<T>`
which indicates to which type you can compare your class. This
parameter should just be the type of the class you are
writing. Examples:

      public class Student implements Comparable<Student> {
          // ...
          public int compareTo(Student other) { ... }
      }
      
      public class Time implements Comparable<Time> {
          // ...
          public int compareTo(Time other) { ... }
      }

