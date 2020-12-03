
# verifier que le ring_cost sera une matrice symétrique aussi pour le challenge
def full_ring(ring_cost):
    sol = [1]
    for i in range(len(ring_cost)):
        # on trouve la meilleur possibilité locale et on met a jour la solution
        h = ring_cost[sol[-1]-1].index(min(ring_cost[sol[-1]-1]))
        #print(min(ring_cost[sol[-1]-1]))
        sol.append(h+1)

        # on corrige la matrice ring_coast pour empecher de cycler
        for elem in ring_cost[sol[-2]-1]:
            elem = 1000000
        for elem in ring_cost:
            elem[sol[-2]-1] = 1000000
    return sol
