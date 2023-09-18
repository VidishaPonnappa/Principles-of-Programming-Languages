# This is the SEND + MORE = MONEY problem solved in python using a brute force methodology.
from itertools import permutations

def manual_solve():
    for perm in permutations(range(10), 8):
        S, E, N, D, M, O, R, Y = perm
        if S != 0 and M != 0:  # Ensure leading zeros are not allowed
            send = S * 1000 + E * 100 + N * 10 + D
            more = M * 1000 + O * 100 + R * 10 + E
            money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y
            if send + more == money:
                return {'S': S, 'E': E, 'N': N, 'D': D, 'M': M, 'O': O, 'R': R, 'Y': Y}

print(manual_solve())
