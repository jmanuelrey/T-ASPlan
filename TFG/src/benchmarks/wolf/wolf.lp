#program always.
% "Types" -> it is obtained from :objects

bank(left). bank(right).
item(wolf). item(sheep). item(cabbage).

:- at(X,B1), at(Y,B1), eats(X,Y), atboat(B2), opp(B1,B2).

#program initial.
% Initial state -> it is obtained from :init

%Invariants -> this predicares wont change at all during solving.
opp(left,right). opp(right,left).
eats(wolf,sheep). eats(sheep,cabbage).

at(wolf,left). at(sheep,left). at(cabbage,left).
atboat(left).

#program dynamic.
% Fluents, action generation and inertia.

%INERTIA
eats(X,Y) :- 'eats(X,Y).
opp(X,Y) :- 'opp(X,Y).
at(X,B1) :- 'at(X,B1), not at(X,B2), opp(B1,B2).

%EFFECTS -> its is obtained from :effect
at(X,B2) :- 'at(X,B1), move(X,B1,B2), opp(B1,B2).
atboat(B2) :- 'atboat(B1), cross(B1,B2), opp(B1,B2).

%ACTIONS
0 {move(X,B1,B2): item(X), bank(B1), bank(B2)} 1.
1 {cross(B1,B2): bank(B1), bank(B2)} 1.




#program final.
% Final state -> it is obtained from :goal

goal :- at(wolf,right), at(sheep,right), at(cabbage,right), atboat(right).
:- not goal.


