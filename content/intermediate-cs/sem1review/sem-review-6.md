---
title: "I.6 Semester I Review 6"
date: 2018-01-26T07:56:22-06:00
weight: 60
draft: false
#type: slide
#theme: white
---

## What does it do? 

Write check-expects.

1. The `double-circle-img` function (abbeviate `dci`):

        (define (double-circle-image img)
          (image-width 
            (beside (circle 40 "solid" "blue)
                    img
                    (circle 40 "solid" "blue))))


2. Write and test a function `r2d` that returns a random two digit
   number. There is a 40% chance of the number beginning with a 2 and
   a 60% chance of it beginning with a 1. The ones digit should be
   random.

3. **Gas gauge**. You are making a _text_ based gas gauge function. 

        gas-gauge: number -> string

    * The readout result will be 16 X's when the tank is full, and then should O's 
    for the part that is empty. For example, half full is `"XXXXXXXXOOOOOOOO"`.
    
    * The gas tank can hold a maximum of 12 gallons. 
    
    * When the tank is over half full, round the result, so 96% reads full.
      
    * When the tank is less than half full, always round down to avoid
      suddenly running out of gas. (So 6% reads empty.)

4. **Graphing**. You are making an animation where a red circle
   follows the people-coordinate graph of the function
   
        y = 1/600 * (x-200) * (x+200)
        
    * Graphing window is 500x300.
    * Both x and y axes are visible.
    * People-coordinate origin is (250,150) in computer coordinates.
    * Positive y-axis for the graph is up.
    * As you move the mouse, the red point shows on the graph is
      directly above/below your mouse.

