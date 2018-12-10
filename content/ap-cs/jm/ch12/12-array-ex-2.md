---
title: "12. Array Exercises 2"
date: 2018-12-10T09:40:46-06:00
weight: 30
draft: false
type: slide
theme: white
description: "More exercises to teach you arrays and loops."
---

# countFill

* input: `int[] nums`
* input: `int s`

Fill the given array with ints counting down from `s`.

```java
int []a = new int[6];
countFill(a, 80); // {80,79,78,77,76,75}
System.out.println(Arrays.toString(a)); 
```

---

# noSevens

`int noSevens(int[] nums)`

* Count how many sevens are in the array.
* Set all of them to zero.
* Return the number of sevens you find.

```
int[] ns = { 10,7,20,7,30,7,7,40};
int a = noSevens(ns);
String ans = Arrays.toString(ns);
System.out.println(a)
System.out.println(ans)
```

---

# countBetween23

`int countBetween23 (int[] nums)`

* Count how many numbers between a 2 and 3.
* Only one 2, one three.
* 2 appears before 3

```
int [] ns = {1,2,5,6,7,13,3,8}
System.out.println(countBetween(ns)); // 4
```
