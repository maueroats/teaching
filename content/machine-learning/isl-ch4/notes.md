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
* Sensitivity: fraction of "true" correctly identified (correctly
  predicted positives / all predicted positives)
* Recall: sensitivity
* Specificity: fraction of "false" correctly identified (true
  negatives / predicted negatives )
* Precision: correctly predicted positive / all predicted positive.
* Type I Error: false positive
* Type II Error: false negative
* ROC curve: graph of true positive rate vs false positive rate (as
  some parameter like "threshold" is varied)

## LDA vs QDA

Both methods assume classes are normally distributed.

* LDA. Same variance means optimal class boundary is linear.
* QDA. Different variances cause the optimal class boundary to be
  quadratic.
  
## SciKit-Learn vs StatsModels

Some estimators like logistic regression are available in both
StatsModels and scikit-learn. 

Scikit-learn offers a uniform interface.

StatsModels offers statistical analysis of the results, including a
convenient summary method. (Although the name of the summary method
may change names for different modeling methods...)

Scikit-learn does not offer statistical analysis tools like p-values
for coefficients, and even getting the coefficients themselves is
not "official" from the API.

Estimators like KNN, LDA, and QDA are only available from
scikit-learn. 

{{% notice tip %}}
Use StatsModels when you want access to statistical information about
the underlying model, like p-values for coefficients. 

Use scikit-learn
for the benefit of a consistent interface across different models, or
do not care about low-level details from the model - for
example when bootstrapping or doing cross validation.
{{% /notice %}}

