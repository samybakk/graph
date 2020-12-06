
import copy as cp
def affectation(affectation_cost, restant):
    current_affectation_solution = []
    temp_affectation_cost = cp.deepcopy(affectation_cost)

    # on empêche d affectr a un sommet pas dans le ring
    for elem in temp_affectation_cost:
        for i in range(len(elem)):
            if i+1 in restant:
                elem[i] = 1000000

    # on affecte
    for elem in restant:
        current_affectation_solution.append([elem, 1 + temp_affectation_cost[elem - 1].index(min(temp_affectation_cost[elem - 1]))])
    return current_affectation_solution
