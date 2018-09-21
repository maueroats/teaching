---
title: "Ch03 Test"
date: 2018-09-21T07:28:38-05:00
weight: 50
draft: true
#type: slide
#theme: white
description: "DRAFT of test on LYaH Chapter 3."
---

{{< use-mathjax >}}

1. (`someSqrt`) Write a signature and the function.
   The `someSqrt` function that takes in a list of x values and puts out a
   list of points:
   
       * x values less than 10 are ignored (no corresponding point is
         output)
       * otherwise output a point on the graph of $y=\sqrt{x}$

2. The `whatSig` function takes in an ordered pair, a distance, and
   two strings. If the ordered pair is within the distance of (0,0),
   then the answer is the first string, otherwise the answer is the
   second string. What is an appropriate the _signature_ (only) for
   this function? 

     ```haskell
     whatSig (3,4) 10 "Close" "Far" == "Close"
     ```

3. Give an example of an ability that the  `Fractional` class
   constraint provides that is not available with an `Integral` class
   constraint. 
   
4. Give an exmaple of an ability that the `Floating` class constraint
   provides that is not available with `Fractional`.
   
5. (`midAvg`) Given a list of `Double` numbers with 3 or more
   elements, the `midAvg` function gets rid of the first and the last
   element, then finds the average of the remaining list. Write the
   complete function, including signature.
   
   
