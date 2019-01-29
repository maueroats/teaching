---
title: "12. Quiz P"
date: 2019-01-29T06:32:10-06:00
#weight: 
draft: true
#type: slide
#theme: white
description: "CodingBat-like Array-2 question: thumbs2019"
---

(`thumb2019`)
We say a value in an array of ints is a "thumb" value if
it has a value to the left and right, and it is more than 7 away from
both of those values. Replace all of the "thumb" values with the average of its neighbors to the left and right. When the average is not an int, round it.
An exception to this rule is that if either of the neighbor values is 2019, then the number is not considered a "thumb" value.

In addition to replacing the values, also return the changed array.

Examples:

5. `thumb2019([5,15,31])` => `[5,18,31]`
6. `thumb2019([5,15,2019])` => `[5,15,2019]`
7. `thumb2019([51,15,5])` => `[51,28,5]`
8. `thumb2019([50,15,5])` => `[50,28,5]`
1. `thumb2019([10,30,70,100])` => `[10,40,65,100]`
2. `thumb2019([40,47,54,61])` => `[40,47,54,61]`
3. `thumb2019([40,47,55,2019,65])` => `[40,47,55,60,65]`
4. `thumb2019([1,1,3,4,2019,5,2019])` => `[1,1,3,4,5,5,2019]`
5. `thumb2019([36,47,55,2019,65]`) => `[36,46,55,60,65]`

[Starter code](12-quiz-p.java) with tests included.

