---
title: "13. ArrayList Quiz"
date: 2018-02-13T08:20:28-06:00
#weight: 
draft: false
#type: slide
#theme: white
---

1. Change the sequence "I" "run" "fast" to "You" "and" "I" "run" "fast"
   every place that the former occurs.
   
        public static void runfast(ArrayList<String> data)


2. **No mice**. Remove every "mouse" (or "mice") in the input.

        public static void noMouse(ArrayList<String> school)


## Advanced

Read Wolfram's numbering scheme for 
[one dimensional cellular automata](https://en.wikipedia.org/wiki/Elementary_cellular_automaton). Write a function that creates a new ArrayList according to a given rule number.

    public static ArrayList<Boolean> evolve (int rule, ArrayList<Boolean> data)

