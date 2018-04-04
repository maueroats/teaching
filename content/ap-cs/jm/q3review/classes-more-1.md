---
title: "Q3. Classes More 1"
date: 2018-04-04T08:51:54-05:00
weight: 10
draft: false
#type: slide
#theme: white
description: "Writing classes, some review problems."
---

1. Write the abstract class `Noisy` and the subclass `NoisyDog`.

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
            public void makeNoise();
        }

## SportsFan

        public interface SportsFan { 
            String cheer();
            String boo();
        }
        
1. Make a `BoorFan` class that implements the SportsFan interface. A `BoorFan` does not cheer, so just return the empty string for that method. A `BoorFan` returns `"You stink!"` when booing.

2. Make a `GetRowdy` class that cheers twice, separated by spaces, and boos three times. 

        public class GetRowdy implements SportsFan {
            public GetRowdy (SportsFan p) {
                // write this
            }
            // other methods required to implement interface
        }
        
