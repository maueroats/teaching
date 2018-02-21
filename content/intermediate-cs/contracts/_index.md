---
title: "Contracts"
date: 2018-02-21T09:32:37-06:00
weight: 225
draft: false
#type: slide
#theme: white
description: "Racket can enforce signatures (contracts). Learn how."
---

We have been writing signatures for functions by using comments.

     ; double-it: number -> number
     
This works fine for organizing your thoughts, but it would be nice if
Racket could actually stop you from doing something different from
what you said you would do. 

{{% notice note %}}
Intermediate student mode is required to use contracts. 
`(require racket/contract)`
{{% /notice %}}

{{% children description="true" %}}

