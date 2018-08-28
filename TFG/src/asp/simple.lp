#program types(t).
fluent(p(X,t)) :- item(X).
fluent(q(X,t)) :- item(X).
fluent(r(X,t)) :- item(X).
action(move(X,t)) :- item(X).

#program static.
item(i1;i2;i3).

#program initial.
q(i2,0). r(i3,0).

#program dynamic(t).

p(X,t+1) :- move(X,t+1), item(X), r(X,t).
q(X,t+1) :- move(X,t+1), item(X), p(X,t).
r(X,t+1) :- move(X,t+1), item(X), q(X,t).

% We cannot move more than one element
1 { move(X,t+1): item(X) } 1.

#program final(t).

p(i2,t).