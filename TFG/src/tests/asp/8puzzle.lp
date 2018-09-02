#program types(t).

action(move(X,t)) :- dir(X).
fluent(pos(X,Y,Z,t)) :- tile(X), row(Y), col(Z).
fluent(goal(t)).


#program static.

row(1..3).
col(1..3).
tile(0..8).
cell(X,Y) :- row(X), col(Y).

dir(up;down;right;left).

adj(X,Y,up,   X-1,Y) :- row(X),row(X-1),col(Y).
adj(X,Y,down, X+1,Y) :- row(X),row(X+1),col(Y).
adj(X,Y,left, X,Y-1) :- row(X),col(Y-1),col(Y).
adj(X,Y,right,X,Y+1) :- row(X),col(Y+1),col(Y).

#program initial.

pos(1,1,1,0). pos(8,1,2,0). pos(2,1,3,0).
pos(0,2,1,0). pos(4,2,2,0). pos(3,2,3,0).
pos(7,3,1,0). pos(6,3,2,0). pos(5,3,3,0).


#program dynamic(t).

1 {move(D,t) : dir(D)} 1.

pos(0,Z,T,t) :- move(D,t), pos(0,X,Y,t-1), adj(X,Y,D,Z,T).
pos(P,X,Y,t) :- move(D,t), pos(0,X,Y,t-1), adj(X,Y,D,Z,T), pos(P,Z,T,t-1).

% Inertia
pos(P,Z,T,t) :- pos(P,Z,T,t-1), not -pos(P,Z,T,t).
-pos(P,Z,T,t) :- pos(P,X,Y,t), (X,Y)!=(Z,T), row(Z), col(T).


#program final(t).

goal(t) :- pos(1,1,1,t), pos(2,1,2,t), pos(3,1,3,t),
		   pos(4,2,1,t), pos(5,2,2,t), pos(6,2,3,t),
           pos(7,3,1,t), pos(8,3,2,t), pos(0,3,3,t).