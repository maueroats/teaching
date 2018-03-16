---
title: "22a. Hangman Draw Handler"
date: 2018-03-16T07:58:46-05:00
weight: 994
draft: false
#type: slide
#theme: white
---

Draw the whole scene by using helper functions to draw the different
parts. At first you can just put all of the images `above` each other;
later you can change the placement so it looks the way you prefer.

1. Draw the gallows based on how many wrong answers.
2. Draw the mistaken letters.
3. Draw the word with underscores for letters that are not guessed.

This page will not include any specific advice on how to draw the word
with underscores for the letters that are not guessed. The `wipeout`
function below should provide you will all of the skills you need to
do it, though.


## Underscore Warmup I: omit

The `omit` function takes in a word and a letter and returns the same word with every occurence of the letter omitted (left out).

    omit: string(word) string(letter) -> string
    (check-expect (omit "word" "w") "ord")
    (check-expect (omit "hangman" "a") "hngmn")
    (check-expect (omit "nothing" "z") "nothing")
    
Follow the design process to write the `omit` function.

1. Simple examples that build up to a three letter word, showing how a letter can be omitted zero, one, or two times.
2. Write the function: handle the empty word 
3. Write the function: handle one letter word
4. Write the function: handler longer words

Run your checks after each step to make sure you stay on track.

## Underscore Warmup II: wipeout

The `wipeout` function takes in a word and a string of letters to
remove. Every occurence of the letters should be removed from the word.

    wipeout: string(word) string(letters) -> string
    (check-expect (wipeout "Williams" "li") "Wams")
    (check-expect (wipeout "penguin" "dinosaur") "peg")

Follow the design process and use the `omit` helper function!
