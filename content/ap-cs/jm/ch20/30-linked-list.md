---
title: "20. Linked Lists"
date: 2018-05-22T20:04:44-05:00
weight: 30
draft: false
#type: slide
#theme: white
description: "LinkedList is a List that has the ability to add items quickly on the front or back."
---

The [linked list](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html) is like our familiar `ArrayList`, except that one can quickly add items anywhere in the list. 

Summary: insertion at the first or last index is a constant time O(1)
operation. Getting the first or last item from a list is also fast
O(1). Getting items from the middle is a slower O(n) operation.


| operation \ location |  first       |  middle     |  last      |
|----------------------|--------------|-------------|------------|
| add                  | addFirst(e)  | add(idx, e) | addLast(e) |
| get                  | getFirst()   | get(idx)    | getLast()  |
| poll (get and remove)| pollFirst()  | _none_      | pollLast() | 


These are the fundamentals. There are many more convenience operations; read the [linked list](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html) documentation to learn them.

## Examples

* [LinkedListDemo](LinkedListDemo.java)
