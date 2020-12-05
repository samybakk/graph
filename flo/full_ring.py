import copy as cp
from utils import rest
# verifier que le ring_cost sera une matrice symétrique aussi pour le challenge
def full_ring(ring_cost,ring_sommet):
    temp_ring_cost = cp.deepcopy(ring_cost)

    sol = [1]
    autre = []

    #on calcul les sommet qui sont pas dans le ring
    for i in range(len(ring_cost)):
        if i + 1 not in ring_sommet:
            autre.append(i + 1)

    #on back ce qui rentre pas dans le ring
    for elem in autre:
        for temp in temp_ring_cost[elem-1]:
            temp = 1000000
        for temp in temp_ring_cost:
            temp[elem-1] = 1000000


    # on cré le ring
    for i in range(len(ring_sommet)):
        # on trouve la meilleur possibilité locale et on met a jour la solution
        h = temp_ring_cost[sol[-1]-1].index(min(temp_ring_cost[sol[-1]-1]))
        sol.append(h+1)

        # on corrige la matrice ring_coast pour empecher de cycler
        for elem in temp_ring_cost[sol[-2]-1]:
            elem = 1000000
        for elem in temp_ring_cost:
            elem[sol[-2]-1] = 1000000


    return sol



