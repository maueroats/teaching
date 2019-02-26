---
title: "14. Comparable Clock"
date: 2019-02-26T11:08:48-06:00
weight: 20
draft: false
#type: slide
#theme: white
description: "Example implementing Comparable for a clock class with hours and minutes."
---

A `Clock` class has hours and minutes, two times are compared by first
comparing the hours. If the hours are the same, then compare the minutes.
Write a complete class definition including a constructor and the
`compareTo` method. 

## Demo Test Code

```java
public void testCmp() {
    Clock a = new Clock(7,30);
    Clock b = new Clock(9,25);
    int r1 = a.compareTo(b);
    System.out.println(r1); // should be negative
    Clock c = new Clock(7,21);
    int r2 = a.compareTo(c);
    System.out.println(r2); // should be positive
}
```

## Solution

```java
public class Clock implements Comparable<Clock> {
    private int hour, min;
    public Clock(int h, int m) {
        hour = h; min = m;
    }
    public int compareTo (Clock other) {
        int answer;
        answer = this.hour - other.hour;
        if (answer != 0) return answer;
        answer = this.minute - other.minute;
        return answer;
    }
}
```
