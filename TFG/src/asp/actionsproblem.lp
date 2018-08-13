#program config.

action(load, 0).     action(shoot, 0).

fluent(loaded, 0).   fluent(unloaded, 0).   

fluent(alive, 0).    fluent(dead, 0).



#program base(t).

loaded(t) :- load(t), unloaded(t-1).

:- load(t), loaded(t-1).

unloaded(t) :- shoot(t), loaded(t-1).

dead(t) :- shoot(t), loaded(t-1).

% Intertia

dead(t) :- dead(t-1).

alive(t) :- alive(t-1), not dead(t).

loaded(t) :- loaded(t-1), not unloaded(t).

unloaded(t) :- unloaded(t-1), not loaded(t).

% Actions

0 {load(t); shoot(t)} 1.



% Init

alive(0).
unloaded(0).
