from math import pow

def eloUpdate(winner, loser, k=32):
    expected_win = 1 / (1 + pow(10, (loser-winner)/400))
    new_w = winner + k * (1 - expected_win)
    new_l = loser - k * (1 - expected_win)
    return new_w, new_l