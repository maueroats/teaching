---
title: "Classes Review"
date: 2019-01-25T14:30:51-06:00
#weight: 
draft: false
#type: slide
#theme: white
---

## Gnome

A Gnome has a double precision height in meters and an integer weight
in kilograms. When you make a new Gnome, if you do not specify the
weight it is assumed to be 10kg.

	    Gnome a = new Gnome(0.37, 4); // 0.37m, 4kg
		Gnome b = new Gnome(0.61); // 0.61m, 10kg
		
The Gnome class should have the following methods:

1. `public void grow()`: Increase the height by 0.1m.
2. `public void eat()`: A Gnome gains 1kg every 3 times it eats.
3. `public String see()`: Returns a string showing height and
      weight: "ht: 0.37m, wt: 4kg" for the Gnome `a` above.

* Write the complete `Gnome` class. 
* Demonstrate its use by making a 12kg, 80cm tall gnome, having it
  grow and then eat 5 times. Print out what you `see()`: it should be
  0.9m and 13kg.
  
## ShootingStar

[This class had problems, was unclear and the details of tick() are not
important now.]

The universe schedules shooting stars to appear at a certain time. A
shooting star has an `appearTime` (double) and a `brightness` (int),
both of which are set in the constructor.

The current time in "ticks" when a shooting star is constructed is
always 0. A shooting star will keep track of time on its own (when
`tick()` is called, time passes).

The constructor you must support is:

	 // a star that appears at time 3.7 with brightness 8
     ShootingStar c = new ShootingStar(3.7, 8); 

The methods you need are:

1. `public void tick()`: Called by the universe to increase the
   current time by one. Do not call this in your code.
3. `public void explode()`: Makes brightness = 1000 for the next 6
   ticks, then brightness becomes 0.
4. `public int getBrightness()`: Return the brightness for the current
   time (as the shooting star knows). The reported brightness is zero
   before the star appears.

How should it work? 

     ShootingStar c = new ShootingStar(3.7, 8);
     for(int t=0; t<12; t++) {
	     System.out.println(t+" shows "+c.getBrightness());
		 c.tick();
		 if (t==4) c.explode();
	 }

Code above gives the output:

     0 shows 0
	 1 shows 0
     2 shows 0
	 3 shows 0
	 4 shows 8
	 5 shows 1000
	 6 shows 1000
	 7 shows 1000
	 8 shows 1000
	 9 shows 1000
	10 shows 1000
	11 shows 0
	12 shows 0
	
