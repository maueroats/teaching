---
title: "4. Syntax in Functions"
date: 2017-09-18T13:22:05-05:00
tags: 
 - haskell
weight: 4
draft: false
---
Patterns, guards, where, let, and case.
<!--more-->

* patterns

```haskell
    f [] = 0
    f (x:xs) = x + f xs
```

* guards 

```haskell
    numword x 
    | x < 0     = "Negative"
    | x == 0    = "Zero"
    | otherwise = "Positive"
```

* where

```haskell
    h x = constant * x
       where constant = 100
```

* let

```haskell
    yis65 x = let (parabola = 10 * x * x + 25) in parabola == 65
```

* case

```haskell
    numit value = case (value) of 
        5 -> "Five"
        4 -> "Four"
        _ -> "Something else"
```
