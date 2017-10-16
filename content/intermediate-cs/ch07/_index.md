---
title: "7. Numbers"
date: 2017-10-16T14:54:40-05:00
weight: 70
draft: false
---

We learn to do math with numbers. 
<!--more-->

## Essential summary

* Basic arithmetic
```racket
(+ 5 3)
(/ 13 7) ; thirteen divided by seven
(* 11 2)
(- 9 1) ; nine minus one
(- 8)
(quotient 21912 7)
(remainder 21912 7)
```

* Exponents, square root, squaring:
```racket
(expt 1.01 95) ; 1.01 to the 95 power is about 2.57
(sqrt 9) ; square root of 9 is three
(sqr 1241) ; when you square 1241 you get 1540081
```

* Inexact answers, checking with tolerance
```racket
> (sqrt 5) ; about 2.236
#2.23606797749979
```
The `#i` at the start of `#i2.236...` means that the number is an "inexact" decimal. 
You should never use check-expect with inexact numbers, because the inexact results can be different on different computers! Instead, use `check-within`.

```racket
(check-within (sqrt 5) 2.236 0.001)
```

* Special numbers: both pi is built in. Your tests should still pass if you use either the buit in value of `pi` or `3.1415`.

```racket
> pi
#i3.141592653589793
```

## Further Information

{{% children description="true" %}}

