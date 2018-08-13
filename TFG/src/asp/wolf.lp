#program base(t).

bank(left;right). opp(left, right).
eats(wolf,sheep). eats(sheep,cabbage).

% Inertia
at(X,B1,t+1) :- at(X,B2,t), move(X,t), opp(B1,B2).
at(X,B1,t+1) :- at(X,B1,t), not move(X,t).

% Boat is always moving
boat(B1,t+1) :- boat(B2,t), opp(B1,B2).

% We cannot move more than one element
0 {move(X,t)} 1.

% We cannot move an element if the boat is at the other bank
:- move(X,t), at(X,B1,t), boat(B2,t), opp(B1,B2).

% We cannot leave X and Y alone if X eats Y
:- at(X,B1,t), at(Y,B1,t), eats(X,Y), boat(B2,t), opp(B1,B2).

#program config.

action(move,1).

fluent(at,2). fluent(boat,1).

#program init.

at(wolf,left,0). at(sheep,left,0). at(cabbage,left,0).

boat(left,0). 

#program goal.

goal(0) :- at(wolf,right,0), at(sheep,right,0), at(cabbage,right,0), boat(right,0).