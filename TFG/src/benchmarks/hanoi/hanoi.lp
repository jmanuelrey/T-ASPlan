#program always.

#const n = 8.
disk(1..n).
peg(a;b;c).

#program initial.

init_on(1..n,a).
on(D,P) :- init_on(D,P).
goal_on(1..n,c).


#program dynamic.

% Move a disk to some peg
1 {move(D,P) : _disk(D), _peg(P)} 1.
move(D) :- move(D,P).

% Effects of moves
on(D,P) :- move(D,P).
on(D,P) :- 'on(D,P), not move(D).

% Check moves
blocked(D-1,P) :- 'on(D,P).
blocked(D-1,P) :- blocked(D,P), _disk(D).
:- move(D,P), blocked(D-1,P).
:- move(D), 'on(D,P), blocked(D,P).
:- _disk(D), not 1 {on(D,P)} 1.

#program final.


:- _goal_on(D,P), not on(D,P), not _testing.

#show move/2.
