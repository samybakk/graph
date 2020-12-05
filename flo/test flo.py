from flo.full_ring import full_ring
from utils import lecture, evaluation
from random import randint

ring_cost, affectation_cost = lecture("../data1.dat")

problem_size = len(ring_cost)

current_ring_solution = []
current_affectation_solution = []

best_ring_solution = []
best_affectation_solution = []

tabu_list = []

"""paramtre de la methode """
max_size_tabu = problem_size / 4

"""solution initiale"""
temp_ring_cost = ring_cost
# print(ring_cost)
current_ring_solution = full_ring(temp_ring_cost)
# print(ring_cost)
"""il faut faire un delestage ici"""
objectif0 = evaluation(current_ring_solution, current_affectation_solution, ring_cost, affectation_cost)
best_ring_solution = current_ring_solution
best_affectation_solution = current_affectation_solution

sommet = randint(2, problem_size)

if sommet not in tabu_list:
    if sommet in current_ring_solution:

        # on le retire du ring
        del current_ring_solution[current_ring_solution.index(sommet)]

        # on l'affecte au meilleur endroit dispo
        current_affectation_solution.append(min(affectation_cost[sommet - 1]))
        """il faut un delestage ici """
        objectif1 = evaluation(current_ring_solution, current_affectation_solution, ring_cost, affectation_cost)

        # si le nouvel objectif est moins bien, alors le sommet est tabu
        if objectif1 > objectif0:
            tabu_list.append(sommet)

        #si il est meilleur il devient la nouvelle référence :
        if objectif1 < objectif0:
            best_ring_solution = current_ring_solution
            best_affectation_solution = current_affectation_solution
            objectif0 = objectif1



# on del les vieux sommet de la liste tabou
if len(tabu_list) > max_size_tabu:
    del tabu_list[0]

"""
note pour apres, voir si recalculer un full ring avec 
les sommets de chaque solution ne serait pas mieux que juste adapter le ring actuelle
"""
