---
title: "Hugo 0.27.1 / BlackFriday bug report"
draft: true
---

Code blocks are not rendered properly if they are members of the first item in a list.

This is almost certainly an upstream issue:
* `https://github.com/russross/blackfriday/issues/239`.
* `https://github.com/russross/blackfriday/issues/326`


    
## Demo of error

1. This will be wrong. Look at generated HTML.
``` haskell
      bug
```

## Demo of correct behavior

1. With one item before it in the list, everything works.

2. This will generate fine HTML.
``` haskell
      all_ok
```

## Thanks

I am not familiar with the code.




