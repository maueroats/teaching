---
title: "Java Bloopers"
date: 2018-03-09T10:29:38-06:00
#weight: 
draft: false
#type: slide
#theme: white
---

Here are two very tricky problems that people in our class had.

## Exponentiation

What should the output of `loop(5)` be?

    public static void loop(int y)
    {
        for (int k = 0; k < (y^2); k++) {
            System.out.println(k);
        }
    }
    

Explain:

    DemoBlooper.loop(5);
    0 1 2 3 4 5 6 
    
Uh-oh:

    DemoBlooper.loop(7);
    0 1 2 3 4 
    
I'll leave it a mystery for now. If you want the compiler to give you
a hint, remove the parentheses around `y^2`.

## Conditionals

The following code is supposed to examine the neighbors of the element
row=r, col=c in the array temp. If the element is 1 but it has less
than 2 or more than 3 neighbors, it becomes 0. If the element is 0 but
has 3 neighbors, it becomes 1.

    int nextalive = countnextalive(size, r, c, temp);
    if(temp[r][c] == 1)
        if(nextalive < 2 || nextalive > 3)
            nums[r][c] = 0;
    else
        if(nextalive == 3)
            nums[r][c] = 1;

The code has a bug in it... any ideas? You'll probably need to test it
to figure out what's wrong.



