

def affectation(affectation_cost, sommet, affectation_solution):
    affectation_solution.append(min(affectation_cost[sommet-1]))
    return affectation_solution
