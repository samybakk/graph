

def affectation(affectation_cost, restant, current_affectation_solution):
    current_affectation_solution = []
    for elem in restant:
        current_affectation_solution.append([elem, 1 + affectation_cost[elem - 1].index(min(affectation_cost[elem - 1]))])
    return current_affectation_solution
