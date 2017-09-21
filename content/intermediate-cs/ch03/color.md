---
title: "Color Commands"
date: 2017-09-21T13:31:31-05:00
draft: false
---

* `name->color` changes a string name to a color, like this:
```
	> (name->color "lavender") 
	(make-color 230 230 250)
```

   If you give it a color already, the computer complains:
```
	> (name->color (make-color 230 230 250))
    name->color: Expected a string or symbol, but received (make-color 230 230 250 255) 
```

* `colorize` changes a name to a color, but does not complain if it gets something that is already a color. That makes it better than `name->color`.
```
	> (colorize "lavender") 
	(make-color 230 230 250)
```

   If you give it a color already, the computer complains:
```
	> (colorize (make-color 230 230 250))
	(make-color 230 230 250))
```

