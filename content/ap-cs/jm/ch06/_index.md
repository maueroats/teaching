---
title: "6. Data Types"
date: 2017-12-13T09:59:49-06:00
draft: false
weight: 60
#type: slide
#theme: white
---

We did a whirlwind tour of Chapter 5 and 6

## Chapter 5

Read Section 5.3 - reserved words. Look at Figure 5-1 on page 111 and do not use those words as variable names in your program. Especially `try`!

Interested in mastering all of Java? Look up the unusual keywords: 

* [native](https://stackoverflow.com/questions/6101311/what-is-the-native-keyword-in-java-for)
* [transient](https://stackoverflow.com/questions/910374/why-does-java-have-transient-fields)
* [synchroniszed](https://stackoverflow.com/questions/1085709/what-does-synchronized-mean)
* [assert](https://stackoverflow.com/questions/2758224/what-does-the-java-assert-keyword-do-and-when-should-it-be-used)
* [strictfp](https://en.wikipedia.org/wiki/Strictfp)

## Chapter 6

Skim Chapter 6:

* 6.3: Declaring fields, including the use of `final` for constant instance variables. Constants are conventionally written in `UPPERCASE`.
* 6.4: The Table 6-1 on page 133 shows the size in bytes of each of the built-in types, as well as their range. 
* 6.5: How do you get `"` inside a string? How about `\`?
* 6.6: The section on scope is too brief, but the PowerPoint has good examples.

Read the code below and decide how `new Demo(8)` will print out?
```java
public class Demo {
   private int num = 1;
   public Demo(int n) {
      int  num = n;
   }
   public String toString { return "Demo: "+num; }
}
```

## Chapter 6 exercises

* Exercises: 3, 4, 6, 9, 11. 
* Programming: 13.

