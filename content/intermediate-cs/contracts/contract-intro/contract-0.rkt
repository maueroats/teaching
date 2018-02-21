(require picturing-programs)
(require racket/contract)

; add-five: number -> number
(define (add-five n)
  (+ 5 n))

(add-five 10)

; note error does not appear here when you run
(add-five "whoops")
