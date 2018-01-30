---
title: "Final - CodingBat"
date: 2018-01-30T08:33:07-06:00
weight: 20
draft: true
#type: slide
#theme: white
description: "Period 2 final programming question."
---

**sticksOut**. A word in an array "sticks out" if there are two words
before it and one word after it, and it is alphabetically after the
word that comes after it or it is at least two letters shorter than
the word before it. Return a version of the given array in which every
word that "sticks out" is replaced by the last half of the word after
it.

* Use case-insensitive comparison.
* If the "halves" of a word must be uneven, make the _first_ "half" larger.

```
sticksOut(["alfa","bravo","zulu","charlie"]) 
==> ["alfa","bravo","lie","charlie"]
sticksOut(["walnut","pie","quince"])
==> ["walnut", "nce", "quince"]
sticksOut(["DELTA","eragon","FOXTROT","FOXTRO"])
==> ["DELTA","eragon","FOXTROT","FOXTRO"]
```

Note: The notation [...] denotes an array, although this is not
syntactically correct Java. Use the correct syntax in your program and
tests.

* Write the function `sticksOut`.
* Write at least three additional tests.
* Use the [Starter code](SticksOut.java) and automated testing.

