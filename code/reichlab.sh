#!/bin/bash

endDate='2022-05-14'
valEndDate='2022-05-21'
predDate='2022-05-22'
firstSat='2022-05-28'

python validation.py --END_DATE $endDate --VAL_END_DATE $valEndDate --dataset JHU --level state
python validation.py --END_DATE $endDate --VAL_END_DATE $valEndDate --dataset JHU --level nation --nation US
python reichlab_csv.py --END_DATE $endDate --VAL_END_DATE $valEndDate --PRED_DATE $predDate --FIRST_SAT $firstSat
python remove_loc_name.py -f $predDate-UCLA-SuEIR_state.csv 