---
title: "12. Arrays Exercises 4"
date: 2019-01-08T09:13:20-06:00
weight: 55
draft: false
#type: slide
#theme: white
description: "1D arrays"
---

## lockers

`public static int[] lockers(int n)`

Flip means change 0 to 1 and 1 to 0.

* Start with an integer array of n lockers, all closed (0).
* In step 1, flip every locker's state, beginning at locker 1.
* In step 2, flip every second locker's state, beginning at locker 2.
* In step 3, flip every third locker's state, beginning at locker 3.
* Etc.

Return the resulting integer array.


Examples when n=10:

* Step 1: `{0,1,1,1,1,1,1,1,1,1}`
* Step 2: `{0,1,0,1,0,1,0,1,0,1}`
* Step 3: `{0,1,0,0,1,1,1,1,0,0}`
* Step 4: `{0,1,0,0,0,1,1,1,1,0}`
* [...]
* Step 9: `{0,1,0,0,1,0,0,0,0,1}`
