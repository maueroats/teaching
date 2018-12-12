---
title: "4. Notes"
date: 2018-12-12T11:36:44-06:00
weight: 40
draft: false
#type: slide
#theme: white
description: "Takeaways from Chapter 4."
---

## Vocabulary and abbreviations

* LDA = Linear Discriminant Analysis (same covariance for each class)
* QDA = Quadratic Discriminant Analysis (different covariance for each class)
* KNN = k-Nearest Neighbors
* [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix):
  a table of predicted vs true counts or probabilities
* Sensitivity: fraction of "true" correctly identified (true positives)
* Specificity: fraction of "false" correctly identified (true negatives)
* Type I Error: false positive
* Type II Error: false negative
* ROC curve: graph of true positive rate vs false positive rate (as
  some parameter like "threshold" is varied)

## LDA vs QDA

Both methods assume classes are normally distributed.

* LDA. Same variance means optimal class boundary is linear.
* QDA. Different variances cause the optimal class boundary to be
  quadratic.
  
