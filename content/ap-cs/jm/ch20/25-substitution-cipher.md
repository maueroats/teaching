---
title: "20. Substitution Cipher"
date: 2018-05-24T11:23:56-05:00
weight: 25
draft: false
#type: slide
#theme: white
description: "How to break a substitution cipher."
---

You have to know the basic definition of a [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher). You permute the meaning of letters, so for examples "H" will mean "E", then "T" will mean "H", and "E" will mean "T". Every encrypted letter stands for exactly one plaintext letter, and no encrypted letter stands for more than one plaintext letter.

1. Find the frequency of each individual letter in a large file. This gives you an estimate of how often each letter occurs.
2. Find the frequency of each letter in the encrypted text (see below).
3. Match the frequencies and try to decrypt the text.


## Sample texts

* [Easy encrypted text](encrypted-caesar.txt) - just shifted by a constant amount.
* [Harder encrypted text](encrypted-subst.txt)

