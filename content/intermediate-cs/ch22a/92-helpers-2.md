---
title: "22a. Recursion Practice 3"
date: 2018-03-06T20:37:55-06:00
weight: 92
draft: false
#type: slide
#theme: white
description: "Even more recursion practice."
---

Please make sure to write at least three tests for each function.

1. `is-in-word?`: string(letter) string(word) -> boolean. True if the letter is in the word, false otherwise.

        (check-expect (is-in-word? "x" "explode") true)
        (check-expect (is-in-word? "s" "juliuc caecar" false)

2. `word-shrink`: string(word) number(starting-size) -> image. Create a picture of the word in which each letter is four points smaller than the previous letter. Do not let the font size go below 5pt.

     {{% figure src="shrink-word.png" title="(shrink-word \"Perspective Drawing\" 64)" %}}
     
