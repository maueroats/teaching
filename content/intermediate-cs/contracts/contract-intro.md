---
title: "Contract Intro"
date: 2018-02-21T09:43:52-06:00
weight: 10
draft: false
#type: slide
#theme: white
description: "An introduction to using contracts."
---

Contracts are the signatures of functions that we have been using. The
vocabulary word changes to make it sound more legal. Contracts are
actually enforced by Racket.

## Defining a contract

If you want to make sure a function takes in a number and puts out a
number, you can include a contract when you define it. Here is a
simple complete example of a function to add five to a number.

    (require picturing-programs)
    (require racket/contract)

    ; add-five: number -> number
    (define/contract (add-five n)
      (-> number? number?)
      (+ 5 n))
    (add-five "whoops")

Demo files: [no contract](contract-0.rkt), [simple contract](contract-1.rkt).

## Types in a contract

You can use any of the familiar type-testing functions that end in a
question mark. Here is an incomplete list:

* `number?`
* `string?`
* `image?`
* `any/c`: The `/c` stands for `contract`.  Why [any by itself is not correct](https://docs.racket-lang.org/guide/contract-func.html?q=any%2Fc#%28part._any_and_any_c%29) is beyond what we will study.
