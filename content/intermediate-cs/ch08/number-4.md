---
title: "Number Models 4"
date: 2017-10-31T10:15:38-05:00
draft: false
weight: 40
#type: slide
#theme: white
---

* How to show a number in an image:
    - (number->string 50) makes "50"
    - (text ...) wrapped around that makes an image

    Example: `(text (number->string 50) FONT-SIZE "purple")` produces an image with the number 50 in FONT-SIZE point purple font.

* Make a dot follow the line y=2x-30 from x=0 to x=100. Repeat over from x=0 once the dot gets to 100.

* Draw a random radius circle (10<=r<=100) on the screen. Show the radius inside the circle.
    
    Writing check-expects is key to making this work!

{{< figure src="circle-50.png" >}}
