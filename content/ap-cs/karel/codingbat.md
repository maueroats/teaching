---
title: "CodingBat Interlude"
date: 2017-11-02T07:40:52-05:00
draft: false
#type: slide
#theme: white
---

* Make an account on [CodingBat.com](http://codingbat.com/java). Do not use a valuable password.

* Wednesday, November 1: 
    - Read about [logical operations in Java](http://codingbat.com/doc/java-if-boolean-logic.html). 
    - See below for a quick summary.
    - Do eight problems from [Logic-1](http://codingbat.com/java/Logic-1) or higher.

* Thursday, November 2: 
    - Read about [for and while loops](http://codingbat.com/doc/java-if-boolean-logic.html) .
    - Read about [arrays](http://codingbat.com/doc/java-array-loops.html) which provide a context for using `for`.
    - See below for a quick summary.
    - Do eight problems from [Arrays-2](http://codingbat.com/java/Array-2).


## Summary of Logical Operations

* if - else if - else
* and(`&&`), or (`||`), not (`!`)

```java
public boolean someFunction (int n)
{
  boolean answer = false;
  
  if ( n > 20 ) {
    answer = true;
  } else {
    answer = ( n < -10);
  }
  
  return answer;
}
```

## Summary of Looping

* `arrayname.length` finds the length of the array
* `arrayname[index]` gets the the value at the given index
* for (set starting value; test to continue; what to do between steps) { ... }

```java
public boolean countNines (int[] nums)
{
  int count = 0;
  for (int k = 0; k < nums.length; k++)
  {
    if (nums[k] == 9) 
    {
      count = count + 1;
    }
  }
}
```
