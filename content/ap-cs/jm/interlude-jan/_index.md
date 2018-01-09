---
title: "Interlude"
date: 2018-01-09T14:59:06-06:00
draft: false
weight: 109
#type: slide
#theme: white
---

* CodingBat String-2: did 16 the week before Winter Break.

## Review 1

## Review 2

1. Change "snow" to "ice", but only when it appears between "December"
and "February".  To simplify, you may assume that both December and
February appear in the string, and December comes before February.

     ```java
System.out.println(winter("snow December snow ice snow February snow"));
==> "snow December ice ice ice February snow"
```
2. Create a ASCII tree. Given: 
    - height of whole tree (height >= 6)
    - width of crown at the top (width odd)
    - trunk is always 4 lines tall and 3 characters wide
    - width of crown increases by two "*" each line between bottom and top of crown (then decreasing halfway in between)
    
     Example:
    ```text
tree(10,5)
==>
        *****
       *******
      *********
      *********
       *******
        *****
         ***
         ***
         ***
         ***
```

