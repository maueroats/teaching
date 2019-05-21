---
title: "Potentiometer"
date: 2019-05-20T17:19:41-05:00
weight: 30
draft: false
#type: slide
#theme: white
description: "Turn a dial or pinch a rectangle to send a value to the computer."
---

## Basic circuit layout

Connect the two outside pins to power (5V, +) and ground (GND, -). It
does not matter which. The middle pin connects to one of the "analong
inputs" A0 through A5. Memorize this setup.

{{% figure src="potentiometer-only_bb.png" %}}


## Basic coding

The 
<scratch class="inline">analog reading () :: #468cfc reporter</scratch>
block gets a number from 0 to 1023 for your program, based on the
voltage of the input you select.

I will use <scratch class="inline">the value :: variables reporter</scratch> for the variable that holds the reading from
the potentiometer. You should name the variable whatever makes sense
for you. Sometimes "brightness" is a good name.

{{< scratch >}}
when green flag clicked
forever
  set [the value v] to (analog reading (2) :: #468cfc) 
  say (the value) for (0.5) seconds
  set pin (9 v) to value (the value) :: #468cfc
{{< /scratch >}}

