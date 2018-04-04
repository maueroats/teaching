---
title: "Q3. Classes More 1"
date: 2018-04-04T08:51:54-05:00
weight: 10
draft: false
#type: slide
#theme: white
description: "Writing classes, some review problems."
---

We have `NoisyDog` and `SportsFan` classes to practice working with
abstract classes and implementing interfaces.

## NoisyDog

Write the abstract class `Noisy` and the subclass `NoisyDog`.

        public abstract class Noisy {
            public Noisy (int n);

            // print the designated noise one time
            public abstract void noise();
            
            // print the designated noise N times
            public void makeNoise();
        }

        public class NoisyDog extends Noisy {
            // "bark" three times by default
            public NoisyDog(); 
            
            // prints the bark string 3 times
            public NoisyDog(String bark);

            // Also need to implement this
            public void noise();
        }

## SportsFan

        public interface SportsFan { 
            String cheer();
            String boo();
        }
        
1. Make a `BoorFan` class that implements the SportsFan interface. A `BoorFan` does not cheer, so just return the empty string for that method. A `BoorFan` returns `"You stink!"` when booing.

2. Make a `GetRowdy` class that cheers twice, separated by spaces, when asked to cheer. It boos three times. 

        public class GetRowdy implements SportsFan {
            public GetRowdy (SportsFan p) {
                // write this
            }
            // other methods required 
        }
        
3. A `DolphinFan` says `"flip"` to cheer and `"glub"` to boo. Make the
   `DolphinFan` class.

4. The following code has some OK parts and some errors. Which lines are errors? If a line is not an error, explain what happens when you call the `cheer()` method of that object.

        public void demo() {
            SportsFan s = new SportsFan();  // 1
            SportsFan t = new BoorFan();    // 2
            BoorFan b = new SportsFan();    // 3
            GetRowdy r = new GetRowdy();    // 4
            GetRowdy rr = new GetRowdy(t);  // 5
            GetRowdy d = 
               new GetRowdy(new DolphinFan()); // 6

            /* Call cheer() on all of them. What do they do? */ 
        }


