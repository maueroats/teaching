---
title: "3. Writing Basic Classes 1"
date: 2018-11-07T09:42:05-06:00
weight: 10
draft: false
type: slide
theme: white
description: "Practice writing straightforward classes: instance variables, constructor, getter, setter methods."
---

# Rectangle

* Class header
* Instance variables
* Constructor
* Accessor: getWidth
* Method: area

---

# Square

* Class header
* Constructor
* etc.

---

# AddConstant

* Constructor, `addTo`, `setConstant`
* Knows constant to add

```java
{
  AddConstant a = new AddConstant(5);
  int x;
  x = a.addTo(7); // gives x=12
  x = a.addTo(80); // gives x=85
  a.setConstant(3); // now does +3 
  x = a.addTo(7); // gives x=10
}
```

---

# RainbowBug

* Straight 5 steps
* Change color: red -> green -> blue 
* Repeat color changes forever

## Instance variables?
