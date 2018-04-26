---
title: "15. File Quiz"
date: 2018-04-26T09:30:51-05:00
weight: 30
draft: false
#type: slide
#theme: white
description: "Quiz using File, similar tasks to what we have done previously."
---

Given the name of a folder (directory), find all of the files inside
that directory that have either:

* more than 50 lines; _or_
* a number on the first line.

You may assume that the number on the first line is separated by whitespace from the 
other characters. You need only handle lines of these forms:

    211 S. Laflin St
    Room 306
    I ate 4 cookies.

There is a [zip file containing a folder of test cases](quiztry.zip) that you may use to test your code.

## Questions and Problems

* Is it required to look inside folders (directories) that you find? No.
* `NullPointerException`: Commonly caused by attempting to list the files of something that is not a directory. 
* Generic debugging advice: Add print statements so you can see what is going on!
