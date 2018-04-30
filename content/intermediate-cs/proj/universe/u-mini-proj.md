---
title: "Universe Mini Projects"
date: 2018-04-30T09:28:07-05:00
weight: 20
draft: false
#type: slide
#theme: white
description: "Short projects to get used to the Universe code."
---

These short projects (1-2 days) will help you get used to writing
code using the Universe.

1. [Color]({{% relref "u-color" %}}): set everyone's color to yours.
2. Count: add your own number to the total, display your number in a small box and the total big on the screen.

    {{% figure src="count-drawn.png" %}}

3. Color Strip. Modify the color program from above so that the model is a list of colors and hitting a key adds your color to the start of the list. Draw either the whole list of colors or the first 10.

    {{% figure src="color-list-drawn.png" %}}
    
    
4. [Spinning]({{% relref "u-spin" %}}). Each world has a separate image. Only one image spins at a time. When you hit a key in a window, that world's image starts spinning and the other window(s) stop.

5. Chase. Each world has one image that it controls with the mouse. Hitting a key makes the mouse inactive for about one second. (Use a tick handler to reactivate.) I used a colored bar to indicate whether the window is active or not.

    {{% figure src="chase-drawn-frozen.png"  %}}
    {{% figure src="chase-drawn-running.png"  %}}
