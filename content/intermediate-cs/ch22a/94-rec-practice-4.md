---
title: "22a. Recursion Practice 4"
date: 2018-03-12T08:18:47-05:00
#weight: 
draft: false
#type: slide
#theme: white
---

1. `zoo-1`: string -> string. Change every occurrence of "penguin" to "penguins" and change every occurrence of "mouse" to "mice. Leave everything else alone.

         (check-expect (zoo-1 "mouse") "mice")
         (check-expect (zoo-1 "xmouse") "xmice")
         (check-expect (zoo-1 "mousex") "micex")
         (check-expect (zoo-1 "mouse mouse") "mice mice")
         (check-expect (zoo-1 "mouse moose") "mice moose")
         (check-expect (zoo-1 "penguin penguins") "penguins penguinss")


