;; REY ESCOBAR, JUAN MANUEL
;; Wolf, Sheep and Cabbage.


(define (domain wolf)
  (:requirements :adl)
  (:predicates
   (bank ?b)
   (ownership ?x) (eats ?x ?y)
   (at ?x ?y) (at-boat ?x))

  (:action transport
    :parameters (?x ?b1 ?b2)
    :precondition (and
      (bank ?b1) (bank ?b2)
      (ownership ?x) (at ?x ?b1)
      (at-boat ?b1) (not(= ?b1 ?b2)))
    :effect (and
      (at ?x ?b2) (not(at ?x ?b1))
      (at-boat ?b2) (not(at-boat ?b1))
      (forall (?y ?z) (and (ownership ?y) (ownership ?z) (when(and(eats ?z ?y) 
                                          (not(= ?x ?y)) (not(= ?x ?z))
                                          (at ?y ?b1) (at ?z ?b1)) 
                                          (and (not(at ?y ?b2)) (not(at ?y ?b1))))))))

  (:action cross
      :parameters (?b1 ?b2)
      :precondition (and
        (bank ?b1) (bank ?b2)
        (at-boat ?b1) (not(= ?b1 ?b2)))
      :effect (and
        (at-boat ?b2) (not(at-boat ?b1))
        (forall (?y ?z) (and (ownership ?y) (ownership ?z) (when(and(eats ?z ?y) 
                                          (at ?y ?b1) (at ?z ?b1)) 
                                          (and (not(at ?y ?b2)) (not(at ?y ?b1))))))))

  )
