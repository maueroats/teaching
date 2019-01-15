---
title: "5. Notes"
date: 2019-01-15T12:18:20-06:00
#weight: 
draft: false
#type: slide
#theme: white
description: "Information about resampling and common problems."
---

{{% use-mathjax %}}

There are a number of common confusion to address.

## Vocabulary

I have been unclear about the difference between standard deviation
and standard error. The correct term when working with actual data
is sample standard deviation. The confusing part of the vocabulary is
the use of standard error of a statistic vs standard deviation of the
distribution. Use the term standard error when talking about the
theoretical variance of a function computed from randomly sampled
data. (Clarifications welcome.)

* Standard deviation of a distribution: a parameter or trait of the
  distribution that indicates the spread of the results around the
  mean. $\sigma$

* Standard error of a statistic: "standard deviation of its sampling
  distribution" (in the sense above). This is an exact theoretical
  quantity. ($\text{SE}$) You can only compute an estimate of it from data. ($\widehat{\text{SE}}$)
  
* Standard deviation of data: "a synonym for sample standard
  deviation". This is written $\hat{\sigma}$.





## High-level view

The bootstrap process:

1. produce a single estimate of a statistic from a given subset of the data
2. repeat the estimation process 1000 times
3. the mean of your estimates is your estimate for the statistic
4. the standard error of your estimates is the standard error for the statistic
