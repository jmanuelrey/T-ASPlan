;; REY ESCOBAR, JUAN MANUEL
;; Wolf, Sheep and Cabbage.



(define (problem wolf-problem)
  (:domain wolf)
  (:objects left right 
            wolf sheep cabbage)
  (:init
   (bank left) (bank right) 
   (ownership wolf) (ownership sheep) (ownership cabbage) 
   (eats wolf sheep) (eats sheep cabbage) 
   (at wolf left) (at sheep left) (at cabbage left)
   (at-boat left)) 
  (:goal
   (and (at wolf right) (at sheep right) (at cabbage right)
        (at-boat right)))
  )
