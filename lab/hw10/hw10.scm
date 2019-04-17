(define (accumulate combiner start n term)
	(cond 
	((= n 0) start) 
	(else (combiner (accumulate combiner start (- n 1) term) (term n)))
	)
)

(define (accumulate-tail combiner start n term)
	(cond 
	((= n 0) start)
	(else (accumulate-tail combiner (combiner start (term n)) (- n 1) term))
	)
)

(define (partial-sums stream)
  
  (define (stream-add s1 s2)
    (if (null? s1)
        s1
        (if (null? s2)
            s2
            (cons-stream (+ (car s1) (car s2))
                         (stream-add (cdr-stream s1)
                                     (cdr-stream s2))))))
    (cons-stream 
	    (car stream)
	    (stream-add (cdr-stream stream) (partial-sums stream))
    )
)
		   
		
		   


(define (rle s)  
	(define (goUntilNext curElement s len)    
		(cond 
			((null? s) (cons-stream (list curElement len) nil))          
			((= curElement (car s)) (goUntilNext curElement (cdr-stream s) (+ len 1)))          
			(else (cons-stream (list curElement len) (rle s)))
		)  
	)  
			
	(if (null? s) '() (goUntilNext (car s) (cdr-stream s) 1))
)