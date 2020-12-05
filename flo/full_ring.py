
# verifier que le ring_cost sera une matrice symétrique aussi pour le challenge
def full_ring(temp_ring_cost):
    #temp_ring_cost = ring_cost
    sol = [1]
    for i in range(len(temp_ring_cost)):
        # on trouve la meilleur possibilité locale et on met a jour la solution
        h = temp_ring_cost[sol[-1]-1].index(min(temp_ring_cost[sol[-1]-1]))
        #print(min(ring_cost[sol[-1]-1]))
        sol.append(h+1)

        # on corrige la matrice ring_coast pour empecher de cycler
        for elem in temp_ring_cost[sol[-2]-1]:
            elem = 1000000
        for elem in temp_ring_cost:
            elem[sol[-2]-1] = 1000000
    return sol
