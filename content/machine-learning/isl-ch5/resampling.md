---
title: "5. Resampling"
date: 2019-01-09T14:02:47-06:00
weight: 10
draft: false
#type: slide
#theme: white
description: "The first lab on resampling."
---

{{% notice note %}}
The Colaboratory link is: [resampling
lab](https://colab.research.google.com/drive/1oD5DssImqK29xPXLS7eJrcJC9W1l-QWG).
{{% /notice %}}

## Notes

Many people are still using for loops and appending to create the data
from their 1000 runs of a function.

Simplify your work. 

1. Write a function `do_once(...)` that produces the value
   once. 
2. Create a list `[ do_once(...) for _ in range(1000) ]`.

