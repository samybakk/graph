from flo.full_ring import full_ring
from flo.affectation import affectation
from utils import lecture, evaluation, rest
from random import randint
import copy as cp
import time
import matplotlib.pyplot as plt
start_time = time.time()

ring_cost, affectation_cost = lecture("data6.dat")

problem_size = len(ring_cost)

current_ring_solution = []
current_affectation_solution = []

best_ring_solution = []
best_affectation_solution = []

tabu_list = []

ring_sommet = []
restant = []
passed = []

star = []
print('problem_size : '+ str(problem_size))
#print(' ')


"""------------- parametre de la methode -------------"""
max_size_tabu = problem_size * ( 1/2 )




"""------------- solution initiale -------------"""

for i in range(problem_size):
    ring_sommet.append(i+1)
current_ring_solution = full_ring(ring_cost, ring_sommet, True)

"""il faut faire un delestage ici"""
objectif0 = evaluation(current_ring_solution, current_affectation_solution, ring_cost, affectation_cost)

best_ring_solution = current_ring_solution

best_affectation_solution = current_affectation_solution

nbr = 0

"""------------- algorithme -------------"""
for k in range(5000):
    #on prend un sommet random
    sommet = randint(2, problem_size)
    print(sommet)

    #on remet a zero les liste de travail
    ring_sommet = []
    restant = []


    """------------ création de la nouvelle solution -------------"""
    if sommet not in tabu_list:
        print('not tabu')
        # si le sommet est dans le ring
        if sommet in current_ring_solution:
            print('in current ring')

            # on le retire du ring
            del current_ring_solution[current_ring_solution.index(sommet)]
            #on fait le nouveau ring

            """il faut un delestage ici """

            # on affecte les sommet au meilleur endroit dispo
            """NB : on ne peut pas juste recalculer pour l affectation pour le dernier sommet car potentiellement
            d autres sommet y etaint affectés"""
            restant = rest(current_ring_solution, problem_size, restant)
            #print('restant : ' + str(restant))
            current_affectation_solution = affectation(affectation_cost, restant, current_affectation_solution)
            #print(current_affectation_solution)


        # si le sommet n'est PAS dans le ring
        elif sommet not in current_ring_solution :
            print('not in ring')
            ring_sommet = cp.deepcopy(current_ring_solution)
            ring_sommet[-1] = sommet
            current_ring_solution = full_ring(ring_cost, ring_sommet, False)
            restant = rest(current_ring_solution, problem_size, restant)
            current_affectation_solution = affectation(affectation_cost, restant, current_affectation_solution)
            #print(current_affectation_solution)

        """------------- comparaison des solutions -------------"""
        # on test la qualité de la nouvelle solution
        objectif1 = evaluation(current_ring_solution, current_affectation_solution, ring_cost, affectation_cost)

        # print ('new objectif : ' + str(objectif1))
        # si le nouvel objectif est moins bien, alors le sommet est tabu
        if objectif1 > objectif0:
            print('pas mieux')
            nbr += 1
            passed.append(sommet)
            tabu_list.append(sommet)
            current_ring_solution = cp.deepcopy(best_ring_solution)
            current_affectation_solution = cp.deepcopy(best_affectation_solution)
        # si il est meilleur il devient la nouvelle référence :
        if objectif1 <= objectif0:
            print('mieux')
            if objectif1 != objectif0:
                nbr = 0
                passed = []
            else :
                nbr += 1
                passed.append(sommet)
            best_ring_solution = current_ring_solution
            best_affectation_solution = current_affectation_solution
            objectif0 = objectif1

    else :
        print('tabu')



    #print('tabu liste : ' + str(tabu_list))
    #print('taille ring sol : ' + str(len(best_ring_solution)))
    #print('taille affect sol : ' + str(len(best_affectation_solution)))



    # on del les vieux sommet de la liste tabou
    if len(tabu_list) > max_size_tabu:
        del tabu_list[0]

    # si on a deja traité tout les sommet une fois sans amélioration :
    if len(passed) >= problem_size :
        ring_sommet = []
        for i in range(problem_size):
            ring_sommet.append(i + 1)
        current_ring_solution = full_ring(ring_cost, ring_sommet, True)



    star.append(objectif0)
    print(str(objectif0) +' '+str(nbr))
    print(' ')
    #print(best_ring_solution)
    #print(best_affectation_solution)
    #print(' ')
"""
note pour apres, voir si recalculer un full ring avec 
les sommets de chaque solution ne serait pas mieux que juste adapter le ring actuelle
"""

print("--- %s seconds ---" % (time.time() - start_time))
plt.plot(star)

plt.show()
print(problem_size)
print('best_ring : ' + str(len(best_ring_solution)))
print('best_affectation : ' + str(len(best_affectation_solution)))
print('cost : ' + str(objectif0))
print(best_ring_solution)