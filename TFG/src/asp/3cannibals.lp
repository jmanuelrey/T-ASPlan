#program types(t).

action(move(X,Y,t))  :- numpair(X,Y).
fluent(moved(G,N,t)) :- group(G), number(N).
fluent(num(G,B,N,t)) :- group(G), bank(B), number(N).
fluent(boat(B,t))    :- bank(B).
fluent(goal(t)).



#program static.

group(mis;can).  bank(left;right). 
opp(left,right). opp(right,left).
number(0..3).
numpair(X,Y) :- number(X), number(Y).



#program initial.

num(mis,left,3,0). num(can,left,3,0).
boat(left,0).
num(mis,right,0,0). num(can,right,0,0).


#program dynamic(t).

% Auxiliary (action attributes).
moved(mis,M,t) :- move(M,C,t).
moved(can,C,t) :- move(M,C,t).

% No more than 2 persons in the boat.
:- move(M,C,t), M+C > 2.

% The boat cannot be moved by itself.
:- move(M,C,t), M=0, C=0.

% We cannot move more persons than their number in that bank.
:- moved(G,N,t), boat(B,t-1), num(G,B,M,t-1), N > M.

num(G,B,M+N,t) :- num(G,B,M,t-1), boat(B,t), moved(G,N,t).

num(G,B,M-N,t) :- num(G,B,M,t-1), boat(B,t-1), moved(G,N,t).

% Boat is always moving.
boat(B1,t) :- boat(B2,t-1), opp(B2,B1).

% The number of cannibals cannot surpass the number of misionaries in a bank.
:- num(mis,B1,M,t), num(can,B2,C,t), C>M, M>0, B1==B2.

% Inertia rules.
num(G,B,N,t) :- num(G,B,N,t-1), moved(G,0,t).

:- num(G,B,N,t), num(G,B,M,t), M!=N.
:- boat(left,t), boat(right,t).

1 {move(X,Y,t) : numpair(X,Y) } 1.

#program final(t).

goal(t) :- num(mis,right,3,t), num(can,right,3,t).