---
title: "Chapter 4 Discussion"
date: 2017-09-20T09:59:51-05:00
type: slide
draft: true
theme: white
---

# Chapter 4 Discussion


---

## Absence Interpretation

| Periods Absent | Probability of all day absence |
|:--------------:|:------------------------------:|
|      a >= 6    |       1.0                      |
|      a >= 3    |       0.5                      |
|      a <  3    |       0.0                      |

---

## Speaker

| Input | Pattern output |
|:-----:|----------------|
|   1   |  "welcome"     |
|   2   |  "students"    |
|   3   | "_students_ welcome welcome _students_" |
|   4   | "_students_ welcome welcome _students_ students students _students_ welcome welcome _students_" |
|   n   | (previous output) (output before that) (output before that) (previous output) |

---

## Trimult

Given a list of numbers, produce a list of all products of three terms in a row.

* `trimult [10,20,50] = [10000]`
* `trimult [1,2,3,4,5,6] = [6,24,60,120]`

---

## Second and third

|Input|Output|
|-----|------|
| [1,5,10] | "The second and third items of [1,5,10] add to be 15" |
| [3,40,60,99] | "The second and third items of [3,40,60,99] add to be 100" |

 Try two different ways!

---

## Eighty-first

Find the eighty-first item in a list.

|Input|Output|
|-----|------|
| [0,2..200] | 162 |
|[110,120..]| 920 |

---


