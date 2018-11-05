---
title: "Chapter 3 Exercise Hints"
date: 2018-11-05T11:57:16-06:00
#weight: 
draft: false
#type: slide
#theme: white
description: "Python commands useful in each exercise."
---

## 8. Auto, simple regression

8.a. `smf.ols` is how to do a regression

8.a.i relationship means the coefficient

8.a.iv this would be `get_prediction` and its `summary_frame`

8b. `sns.lmplot` is the way to get the points and a regression line

8c. Diagnostic plots means the `plot_lm_summary` function that i
wrote. Follow the instructions on
[`wy-cs.site`]({{% relref "." %}}).

## 9. Auto, multivariate regression

* Scatterplot matrix is `sns.pairplot`
* Pandas has a `corr()` function that works on data frames
* Again, this is `smf.ols` … you specify all of the variables you want to consider by listing them in the formula "x1+x2+stuff". Statistically significant response means looking at `results.pvalues`.
* `plot_lm_summary` again. The "*" creates a new variable by
multiplying. The ":" also includes the individual terms
automatically. You can include "log(x1)" in your formula. You may need
to do `np.power(horsepower,2)` if you want to consider what happens
when a single predictor is squared. See the [StatsModels formula
page]({{% relref "statsmodels" %}}) for more information.

## 10. Carseats, categorical variables

10f. Comparing fit with different models could be done with the material from page 79ff. 

10g. Outliers and high leverage points are visible on the summary plots.

## 11. t-statistic

Opening paragraph: 

* In order to set a random seed, you use
[`numpy.random.seed(N)`](https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do#21494630).
* The normal distribution is `scipy.stats.random.norm()`.
* Sampling 50 values from any distribution is `whatever.rvs(size=50)`

11a. To perform a regression without an intercept, use the formula the
text suggests: "y ~ x + 0". You can get $t$-values and $p$-values from
the instance variables `tvalues` and `pvalues` if you want to see them
individually.

## 13. Simulated data

See number 11 for the functions needed.

* 13d. Skip the legend if it does not appear automatically.

## 14. Collinearity with simulated data

See question 11 for a primer on simulated data.

14g. To add the bad data based on the original dataframe `df`:

    badData = pd.DataFrame({'x1': 0.1, 'x2': 0.8, 'y': 6}, index=[len(df)])
    df2 = df.append(badData)

This question needs to be unpacked. Use the `plot_lm_summary` function
that was provided in class to analyze leverage.
