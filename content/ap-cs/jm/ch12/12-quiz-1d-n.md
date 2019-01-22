---
title: "12. Quiz N"
date: 2019-01-22T09:05:31-06:00
#weight: 
draft: false
#type: slide
#theme: white
---

(`similarEnds`)
An array has similar N-ends if the front and back N numbers are either
in the reversed order. 

Return the largest N value for which an array has the same N-ends. 

* N is a positive integer.
* Give -1 if the ends are not similar at all.

Examples:

1. `similarEnds([20,30,40])` => -1.
2. `similarEnds([20,30,4,5,30,20])` => 2.
1. `similarEnds([20,30,40,50,50,40,30,20])` => 8. The repeating segments overlap.
2. `similarEnds([10,20,30,20,10])` => `5`.
