---
title: "14 .Comparable Bug"
date: 2019-02-26T11:21:34-06:00
weight: 30
draft: false
#type: slide
#theme: white
---

A `Bug` can go one of four directions: "North", "South", "East", and
"West". A bug also has a speed, which is a non-negative integer.

Bugs are going to be ordered using both their direction and speed. The
"primary" method of ordering bugs will be their direction. We will
consider their speed only if their directions are the same.

* Direction: West < South < East < North
* Speed: small number < big number

You are going to write the code, including a constructor `Bug (String
direction, int speed)`. 

```java
{
    Bug a = new Bug("North", 5);
    Bug b = new Bug("South", 8);
    Bug c = new Bug("South", 7);
    
    System.out.println(b.compareTo(a));
    System.out.println(b.compareTo(c));
}
```

