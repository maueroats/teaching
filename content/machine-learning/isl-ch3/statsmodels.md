---
title: "Statsmodels"
date: 2018-10-26T13:15:08-05:00
weight: 40
draft: false
#type: slide
#theme: white
description: "Functions you can use in your StatsModels formulas."
---

The formulas are written in
[patsy](https://patsy.readthedocs.io/en/latest/formulas.html). When
writing your formulas, use NumPy functions whenever you can.

* `np.log`
* `np.sqrt`
* `np.power(x,2)` for the square of x. Using `x*x` does **not** work!
* `a:b` means only the cross effect `a` multiplied by `b`.
* `stuff * other` means `stuff + other + stuff:other`. 

