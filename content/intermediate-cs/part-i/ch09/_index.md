---
title: "9. Strings"
date: 2017-11-08T15:07:52-06:00
draft: false
weight: 90
#type: slide
#theme: white
---

This chapter takes one day to do. Read pages 149-150 in the book. 

## Homework

Page 151 (PDF page 162), exercises 9.2.2 through 9.2.7.

Challenge: 10.2.6.

## Key Functions

* `string-append`
* `string-length`
* `number->string`
* `substring`: string number(start) number(end) -> string. 

   If you omit the end number, the result you get starts at the "start" position and goes until the end of the original string.
   
   Illustration of positions in the string "Cattle":

```text
      C a t t l e
     0 1 2 3 4 5 6 
```
   So `(substring "Cattle" 1 3)` produces `"at"`. 
   
   
The function `string->number` is sometimes useful but not nearly as important. 
Usually it is misused.
