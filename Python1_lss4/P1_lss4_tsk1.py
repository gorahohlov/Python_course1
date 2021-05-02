# 1.-----------------------------------

from sys import argv
scrpt_nm, vyrobotka, stavka, premia = argv
z = float(vyrobotka) * float(stavka) + float(premia)
print('Расчёт заработной платы составил: ', round(z, 2))
