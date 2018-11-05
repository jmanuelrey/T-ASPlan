#program types(t).

action(move(X,t)) :- dir(X).
fluent(pos(X,Y,Z,t)) :- tile(X), row(Y), col(Z).
fluent(goal(t)).

#program static.

row(1..3).
col(1..3).
tile(0..8).
cell(X,Y) :- row(X), col(Y).

% goal state
% 1 2 3
% 4 5 6
% 7 8 0
goalpos(1,1,1). goalpos(2,1,2). goalpos(3,1,3).
goalpos(4,2,1). goalpos(5,2,2). goalpos(6,2,3).
goalpos(7,3,1). goalpos(8,3,2). goalpos(0,3,3).

dir(up;down;right;left).

adj(X,Y,up,   X-1,Y) :- row(X),row(X-1),col(Y).
adj(X,Y,down, X+1,Y) :- row(X),row(X+1),col(Y).
adj(X,Y,left, X,Y-1) :- row(X),col(Y-1),col(Y).
adj(X,Y,right,X,Y+1) :- row(X),col(Y+1),col(Y).

#program initial.

% initial state
% 8 6 7
% 2 5 4
% 3 0 1
pos(8,1,1,0). pos(6,1,2,0). pos(7,1,3,0).
pos(2,2,1,0). pos(5,2,2,0). pos(4,2,3,0).
pos(3,3,1,0). pos(0,3,2,0). pos(1,3,3,0).

#program dynamic(t).

% Manhattan heuristic
heuristics(N,t) :- N = #sum{ M,F : tile(F), F!=0, pos(F,X,Y,t), goalpos(F,X2,Y2), M=|X-X2|+|Y-Y2|}.



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
