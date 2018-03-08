---
title: "9. Exercises 1"
date: 2017-11-13T15:16:21-06:00
draft: false
#type: slide
#theme: white
weight: 91
---

* `dot-fill`: Take in a string(word) and put out a string. The output string is the same as the input string, except that it has periods added (".") to bring it to 10 characters long.

    Examples: 
```racket
(check-expect (dot-fill "abc") "abc.......")
(check-expect (dot-fill "0123456789") "0123456789")
```
    You may assume that the word has no more than ten letters.
    
* `cash`: num(dollars) num(cents) -> string(price)

    Write the price including the dollar sign.
```racket
(check-expect (cash 5 99) "$5.99")
(check-expect (cash 10 0) "$10.00")
(check-expect (cash 98 15) "$98.15")
(check-expect (cash 6 4) "$6.04")
```

