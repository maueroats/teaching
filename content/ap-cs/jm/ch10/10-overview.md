---
title: "10. Overview"
date: 2017-12-14T22:19:19-06:00
draft: false
#type: slide
#theme: white
weight: 10
---

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

