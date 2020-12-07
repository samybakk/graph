import copy as cp
from random import randint
from utils import evaluation
# verifier que le ring_cost sera une matrice symétrique aussi pour le challenge
def full_ring(ring_cost,ring_sommet, meta ,Tcoef):
    temp_ring_cost = cp.deepcopy(ring_cost)

    sol = [1]
    autre = []

    #on calcul les sommet qui sont pas dans le ring
    for i in range(len(ring_cost)):
        if i + 1 not in ring_sommet:
            autre.append(i + 1)

    #on back ce qui rentre pas dans le ring
    for elem in autre:
        for temp in range(len(temp_ring_cost[elem-1])):
            temp_ring_cost[elem-1][temp] = 1000000
        for temp in temp_ring_cost:
            temp[elem-1] = 1000000


    # on cré le ring
    for i in range(len(ring_sommet)):
        # on trouve la meilleur possibilité locale et on met a jour la solution
        h = temp_ring_cost[sol[-1]-1].index(min(temp_ring_cost[sol[-1]-1]))
        sol.append(h+1)

        # on corrige la matrice ring_coast pour empecher de cycler
        for elem in range(len(temp_ring_cost[sol[-2]-1])):
            temp_ring_cost[sol[-2]-1][elem]= 1000000
        for elem in temp_ring_cost:
            elem[sol[-2]-1] = 1000000

    best_sol = cp.deepcopy(sol)


    if meta == True :
        size_tabu = len(ring_sommet) * (Tcoef) +1
        best_cost = evaluation(best_sol, [], ring_cost, [])
        tabu = [1]
        for i in range(len(ring_sommet)**1):
            ref = randint(1, len(ring_sommet)-1)
            if ref not in tabu:
                if ref == 1:
                    temp = sol[ref]
                    sol[ref] = sol[ref+1]
                    sol[ref + 1] = temp
                    cost = evaluation(sol, [], ring_cost, [])
                    print('coucou')
                elif id == len(ring_sommet)-1:
                    temp = sol[ref]
                    sol[ref] = sol[ref - 1]
                    sol[ref - 1] = temp
                    cost = evaluation(sol, [], ring_cost, [])
                    print('coucou gf')
                else:

                    temp = sol[ref]
                    sol[ref] = sol[ref + 1]
                    sol[ref + 1] = temp
                    cost1 = evaluation(sol, [], ring_cost, [])
                    G1 = sol

                    temp = sol[ref+1]
                    sol[ref+1] = sol[ref]
                    sol[ref] = temp
                    temp = sol[ref]
                    sol[ref] = sol[ref - 1]
                    sol[ref - 1] = temp
                    cost2 = evaluation(sol, [], ring_cost, [])

                    if cost2 >= cost1:
                        cost = cost1
                        sol = G1

                    if cost1 > cost2:
                        cost = cost2

                if cost <= best_cost:
                    best_cost = cost
                    best_sol = cp.deepcopy(sol)
                if cost > best_cost:
                    tabu.append(ref)

            if len(tabu) > size_tabu:
                del tabu[1]

    return best_sol



