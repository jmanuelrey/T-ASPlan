#program always.

row(1..3).
col(1..3).
cell(X,Y) :- row(X), col(Y).

adj(X,Y,up,   X-1,Y) :- row(X),row(X-1),col(Y).
adj(X,Y,down, X+1,Y) :- row(X),row(X+1),col(Y).
adj(X,Y,left, X,Y-1) :- row(X),col(Y-1),col(Y).
adj(X,Y,right,X,Y+1) :- row(X),col(Y+1),col(Y).

dir(up;down;right;left).

#program initial.

% pos(Tile,X,Y)

pos(8,1,1). pos(6,1,2). pos(7,1,3).
pos(2,2,1). pos(5,2,2). pos(4,2,3).
pos(3,3,1). pos(0,3,2). pos(1,3,3).

#program dynamic.

1 {move(D) : dir(D)} 1.

pos(0,Z,T) :- move(D), 'pos(0,X,Y), adj(X,Y,D,Z,T).
pos(P,X,Y) :- move(D), 'pos(0,X,Y), adj(X,Y,D,Z,T), 'pos(P,Z,T).

% Inertia
pos(P,Z,T) :- 'pos(P,Z,T), not -pos(P,Z,T).
-pos(P,Z,T) :- pos(P,X,Y), (X,Y)!=(Z,T), row(Z), col(T).

#program final.

goal :- pos(1,1,1), pos(2,1,2), pos(3,1,3),
        pos(4,2,1), pos(5,2,2), pos(6,2,3),
        pos(7,3,1), pos(8,3,2), pos(0,3,3).

:- not goal.

#show move/1.


