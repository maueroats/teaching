---
title: "All Commands"
date: 2019-05-20T22:08:41-05:00
weight: 800
draft: false
#type: slide
#theme: white
description: "Brief summary of all Arduino commands."
---

* A *digital pin* output can be set to true or false. (Use the operators
<scratch class="inline">true :: operators boolean</scratch>
or
<scratch class="inline">false :: operators boolean</scratch>.)
* A *PWM pin* output can be set to any value 0 through 255.
* A *digital reading* input is either true or false.
* An *analog reading* input is a number from 0 to 1023.
* Divide analog reading inputs by 4 to use the in PWM pin
  outputs. Using a larger number will work, but the actual effect
  wraps around to zero every multiple of 256.


## Snap4Arduino Blocks

{{< scratch >}}
set digital pin ( v) to <> :: #468cfc

analog reading ( v) :: #468cfc reporter

set pin ( v) to value (128) :: #468cfc

digital reading ( v) :: #468cfc boolean

arduino connected? :: #468cfc boolean

connect arduino at [] :: #468cfc

disconnect arduino :: #468cfc

set servo ( v) to [clockwise v] :: #468cfc
{{< /scratch >}}

## Interesting Facts

* Analog means continuously adjustable. Analog devices you know:
bicycle brakes, dimmer switches on (old incandescent) lights, knobs on
stove to adjust gas temperature. 

* The Arduino can use Pulse Width Modulation vary the brightness of LEDs. 
  Pulse Width refers to the fraction of the time that the electricity
  is on. Modulation means changing. Translation: the Arduino controls
  brightness by changing the fraction of time the electricity is actually
  delivered to the light.   [Read more about pulse width
  modulation](https://learn.sparkfun.com/tutorials/pulse-width-modulation/all).


* PWM output is sometimes called "fake analog". The computer pretends
  to have a light on 50% brightness by turning it on full blast for
  50% of the time and off for the other 50% of the time (switching back
  and forth very fast so the human eye cannot see the transition).

