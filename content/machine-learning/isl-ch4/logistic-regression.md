---
title: "4. Logistic Regression"
date: 2018-12-12T21:04:59-06:00
weight: 42
draft: false
#type: slide
#theme: white
description: "The details of Logistic Regression in StatsModels."
---

All of this information is taken from Section 4.6.2 Logistic
Regression in the [Chapter 4 Lab
walkthrough](https://colab.research.google.com/drive/1M1fukzCHH5AkiKg6UFudn82ad_MAFQeD). You
should consult that for details.

{{% notice warning %}}
For StatsModels, the output variable must be a number. Change strings like "Larger" and
"Smaller" to the numbers 0 and 1.
{{% /notice %}}

```
import statsmodels.api as sm
result = sm.Logit.from_formula("output~p1+p2",
           data=DataFrame).fit()
```

The resulting `result` variable is of type
[LogitResults](http://www.statsmodels.org/dev/generated/statsmodels.discrete.discrete_model.LogitResults.html),
so check the documentation for all available information. Some
important fields of `LogitResults`: 

* `summary()`
* `summary2()`: We found this was needed on old installations.
* `params`: Coefficients.
* `pvalues`

Less important, still common to use:

* `tvalues()`
* `fittedvalues`
* `bse`: Coefficient standard errors.
* `aic`: A measure of model fit.
