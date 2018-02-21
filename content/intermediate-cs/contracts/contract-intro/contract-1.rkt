(require picturing-programs)
(require racket/contract)

; add-five: number -> number
(define/contract (add-five n)
  (-> number? number?)
  (+ 5 n))

(add-five 10)

; note error appears here when you win
(add-five "whoops")
