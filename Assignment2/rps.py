def points(combo: str) -> int:
    points_dict = {"RP": -1,"RR": 0, "RS": 1, "SS": 0, "SP": 1, "SR": -1,"PR": 1,"PP": 0, "PS": -1}
    return points_dict[combo]

def comboList(combos: str) -> [str]:
    return [combos.split(",")]

import sys
no_of_losses = 0
no_of_wins = 0
no_of_draws = 0
for combo in comboList(sys.argv[1]):
    if points(combo) == 1:
        no_of_wins += 1
    elif points(combo) == -1:
        no_of_wins += -1
    else:
        no_of_draws += 1
print("+" + str(no_of_wins) + "," + "no_of_losses" + "," + str(0) * str( no_of_draws))


