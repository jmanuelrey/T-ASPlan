#program types(t).
action(move(D,P,t)) :- disk(D), peg(P).
fluent(moved(D,t)) :- disk(D).
fluent(on(D,P,t)) :- disk(D), peg(P).
fluent(blocked(D,P,t)) :- disk(D), peg(P).
fluent(goal(t)).

#program static.

disk(1..8).
peg(a;b;c).

#program initial.

on(1,a,0). on(2,a,0). on(3,a,0). on(4,a,0). on(5,a,0). on(6,a,0). on(7,a,0). on(8,a,0).

#program dynamic(t).

% Move a disk to some peg
1 {move(D,P,t) : disk(D), peg(P)} 1.

moved(D,t) :- move(D,P,t).

% Effects of moves
on(D,P,t) :- move(D,P,t).
on(D,P,t) :- on(D,P,t-1), not moved(D,t).

% Check moves
blocked(D-1,P,t) :- on(D,P,t-1).
blocked(D-1,P,t) :- blocked(D,P,t), disk(D).

% Constraints
:- move(D,P,t), blocked(D-1,P,t).
:- moved(D,t), on(D,P,t-1), blocked(D,P,t).
% Every single disk must be on a peg.
:- disk(D), not 1 {on(D,P,t)} 1.

#program final(t).


goal(t) :- on(1,c,t), on(2,c,t), on(3,c,t), on(4,c,t), on(5,c,t), on(6,c,t), on(7,c,t),on(8,c,t).
