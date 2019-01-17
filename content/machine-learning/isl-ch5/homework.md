---
title: "5. Homework"
date: 2019-01-11T11:24:50-06:00
weight: 20
draft: false
#type: slide
#theme: white
description: "Book homework problems." 
---

Chapter 5 homework problems, beginning on page 197 in the book (PDF page
210).

* 2019-01-10: Exercise 5
* 2019-01-11: Exercise 6

**Note**: When you compute results two different ways, you should do a
statistical test to determine whether the difference is
significant. 

## Significance Testing

Normal stats method: 

1. Standardize your results to have mean 0 and variance 1. This number
   is called the z-score. 
   
        z = (value - mean)/standard deviation

2. Find out the probability of observing a number with at least this
   absolute value - P( |num| > z ). The survivor function (sf) is
   P(num > z), so make sure z is positive and double it to account for
   the possibilty of a negative.

        p = scipy.stats.norm().sf(z) * 2

One way to generate a 95% confidence interval about a mean of `xmean`
with a standard deviation of `xstdev`: 

        scipy.stats.norm().interval(0.95, loc=xmean, scale=xstdev)

## Exercise 5

Common problems:

* StatsModels requires numerical result for predicting with a
  logistic regression.

* The LogitResult from your StatsModels logistic regression has a
  predict method which takes in data frame containing the test data.
  
* It is OK to choose your validation set by randomly selecting each row with
  a 50% probability.

* The validation set shows that the error rate is about 2.5% for 5.b.iv.

* Bootstrap gives about 2.7% with a standard error of about 0.2%.

Source for the data:

    df_raw = pd.read_csv('http://vincentarelbundock.github.io/Rdatasets/csv/ISLR/Default.csv')
    df = df_raw.drop(columns=['Unnamed: 0'])
     

## Exercise 6

The data is the same. You should read the [high-level view]({{% relref
"./notes.md" %}}) in the Notes for this chapter so that you know how the
bootstrap works.

* The book talks about `glm` but this means use the StatsModels Logit
  regression and `summary2` from the LogitResults. 
  
* You are supposed to estimate the standard errors of the logistic
  regression coefficients with the bootstrap. That means your `boot1`
  function needs to compute the coefficients of a random sample and
  return them. The coefficients are the `params` field.
  
* You have to write your own bootstrap code to repeat the random
  sampling N times (N=100 seems good). Store the data in a list and
  then make it into a data frame

* 6(d): Use a statistical test in your discussion. Specifically:
  find the likelihood that given the mean and standard deviation you
  estimate from the bootstrap, that the coefficients from the initial
  logistic regression come from the same distribution. Use the
  technique and code from the  "Significance Testing" section above.
  
  

