---
title: "15. Heatmap with Contours"
date: 2018-12-21T07:24:27-06:00
weight: 70
draft: false
#type: slide
#theme: white
description: "Color pixels based on values of a function. Put contour lines every 50 values."
---

{{% use-mathjax %}}

A contour line shows where the elevation does not change.

{{% figure src="contour-lines.gif" %}}


We are going to make a beautiful icy winter picture using that idea.

{{% figure src="astral.png" %}}


## Decide the function

The picture above is made using this function:

$$ f(x,y) = 300 \left( \sin(x) + \cos(x\cdot y /10) \right) $$

In Racket you would type the function:

    (define (f x y)
      (* 300 
         (+ (sin x)
            (cos (* x y 1/10)))))

## Computer coordinates and people coordinates

The picture above is a 600x600 computer coordinate window, with people
coordinates $-22.5 \le x \le 22.5$ and $-15 \le y \le 15$.

Create functions to change x and y computer coordinates to people
coordinates. Follow the process of making a number line, writing
check-expects, and then using a solver to get the equations.

**Note**: For this project you will only need to change computer to
people coordinates.

## Colorize the results

The function $f(x,y)$ above gives numbers from -600 to 600.

Use the ideas from the heatmap to use different colors for
different values. I made mine in three pieces:

| value | color |
|-------|-------|
| 0     | blue 175 |
| 250   | blue 250 |
| 251   | green 1, blue 250 |
| 500   | green 250, blue 250|
| 501   | red 1, blue 250 |
| 750   | red 250, blue 250 |

   
