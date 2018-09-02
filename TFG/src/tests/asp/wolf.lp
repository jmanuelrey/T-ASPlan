#program types(t).

action(move(X,t)) :- item(X).
fluent(at(X,Y,t)) :- item(X), bank(Y).
fluent(boat(Y,t)) :- bank(Y).
fluent(goal(t)).

#program initial.

at(wolf,right,0). at(sheep,left,0). at(cabbage,left,0). 
boat(right,0). 

#program static.

bank(left;right). opp(left, right).    opp(right, left). 
eats(wolf,sheep). eats(sheep,cabbage). item(wolf; sheep; cabbage).

#program dynamic(t).

% Inertia
at(X,B1,t) :- at(X,B2,t-1), move(X,t), opp(B1,B2), item(X), bank(B1), bank(B2).
at(X,B1,t) :- at(X,B1,t-1), not move(X,t), opp(B1,B2), item(X), bank(B1), bank(B2).

% Boat is always moving
boat(B1,t) :- boat(B2,t-1), opp(B1,B2), bank(B1), bank(B2).

% We cannot move more than one element
0 { move(X,t): item(X) } 1.

% We cannot move an element if the boat is at the other bank
:- move(X,t), at(X,B1,t-1), boat(B2,t-1), opp(B1,B2), item(X), bank(B1), bank(B2).

% We cannot leave X and Y alone if X eats Y
:- at(X,B1,t-1), at(Y,B1,t-1), eats(X,Y), boat(B2,t-1), opp(B1,B2), item(X), item(Y), bank(B1), bank(B2).

#program final(t).

goal(t) :- at(wolf,right,t), at(sheep,right,t), at(cabbage,right,t), boat(right,t). 