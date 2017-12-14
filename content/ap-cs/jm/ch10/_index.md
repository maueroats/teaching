---
title: "10. Strings"
date: 2017-12-13T10:10:58-06:00
draft: false
weight: 100
#type: slide
#theme: white
---

There are a lot of tricky issues related to strings. Read [the powerpoint](http://www.skylit.com/javamethods2/ppt/Ch10.ppt) carefully!

* Strings are immutable. "Changing" functions like `s.toUpperCase()` actually return a copy; they do not affect the original.

* Understand the box and arrow diagrams on page 269.

* String methods (summarized on page 271, Figure 10-3):

    - `s.length()`
    - `s.charAt(idx)`: but note the answer is a `char` not a `String`.
    - `s.substring(start)`
    - `s.substring(start,end)`
    - `s.equals(otherString)`
    - `s.compareTo()`
    - `s.indexOf("wanted")` 

* Useful in real life: `trim`, `replace`, `toLowerCase`.

### 10.5: Formatting

Lots of detail on how to get a number to appear exactly the way you want it. Read if you are advanced. 

[Tutorial on printf](https://docs.oracle.com/javase/tutorial/essential/io/formatting.html), [Tutorial on formatting numbers](https://docs.oracle.com/javase/tutorial/java/data/numberformat.html).

### 10.6: Numbers to Strings

This section includes basic parsing as well as how to handle "exceptions" that may occur.

* `double x = Double.parseDouble("3.14159")`
* `int a = Integer.parseInt("121")`

## Exercises

1. Using the code below, compute:

    1. `v == w`
    2. `v.equals(w)`
    3. `v.compareTo(w)`

```java
{
   String s = "cow";
   String v = s;
   String w = new String(s);
}
```
