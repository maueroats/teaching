---
title: "2. Finite Dimensional Vector Spaces"
date: 2019-05-16T10:14:50-05:00
weight: 20
draft: false
#type: slide
#theme: white
---

{{% use-ml %}}

Notation from book:

* $F$ means $\mathbb{R}$ or $\mathbb{C}$. You should think it means
  the real numbers when you read it. I will write all of these notes
  using $F=\mathbb{R}$, but you could use $\mathbb{C}$ just the same.
  
* $V$ is always a vector space over $F$.

* Linear combination of $m$ vectors $v_1, \ldots, v_m$ is a vector of
  the form 
  
  $$ a_1 v_1 + \cdots + a_m v_m, $$
  where all of the $a_i$ are real numbers.
  
* **Span**. The set of all linear combinations of a list of vectors is
  called their span. 
      The span of the empty set is defined to be $\{0\}$. In notation,

      $$ \Span(v_1,\ldots,v_m) = \left\lbrace a_1 v_1 + \cdots + a_m v_m
\right\rbrace , $$

      where the $a_i$ are real numbers.

* A set of vectors "spans" a vector space if their span is the 
  whole vector space.

* All lists of vectors in this book are finite length.

* A _finite dimensional_ vector space is spanned by a (finite) list of
  vectors.
  
* A vector space is "infinite dimensional" if it is not finite
  dimensional. 

* Polynomials of degree at most m are denoted $\mathcal{P}_m$. 

* polynomials of any degree is $\mathcal{P}$.

* **Linear independence**. A list of vectors $v_1, \ldots, v_m$ is linearly independent
  if the only choice of $a_1, \ldots, a_m$ that makes 
  $$ a_1 v_1 + \cdots + a_m v_m = 0$$
  is $a_1=\cdots=a_m = 0$.

* **Linearly dependent**. You can find some $(a_1,\ldots,a_m)$ not all
  zero that makes the "linear dependence equation" be true:
  $$ a_1 v_1 + \cdots + a_m v_m = 0$$

## Facts / Lemmas

* The span of a list of vectors in $V$ is the smallest subspace of $V$
  containing all of the vectors.
  
* Linear dependence lemma (to prove).  
  
* Length of lienarly independent list <= length of spanning list.

## Quick Exercises

1. Is $(17,-4,2)$ a linear combination of $(2,1,-3)$ and $(1,-2,4)$?
2. Is $(17,-4,5)$ a linear combination of $(2,1,-3)$ and $(1,-2,4)$?
