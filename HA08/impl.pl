:- bat_ok.
:- ign_ok.
:- freg_ok.
:- start_ok.
:- tank_ok.
:- pump_ok.
:- filt_ok.
:- eng_ok.

ign_ok :- starter_ok.
bat_ok :- ign_ok.
start_ok :- eng_ok.
filter_ok :- eng_ok.
pump_ok :- filt_ok.
tank_ok :- pump_ok.
freg_ok :- pump_ok.
ign_ok :- freg_ok.
bat_ok :- freg_ok.
