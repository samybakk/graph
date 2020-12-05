def lecture(file_name):
    ring_cost = []
    affectation_cost = []
    with open(file_name) as f:
        ligne = f.readline()
        elem = ligne.split()
        results = map(int, elem)
        results = list(map(int, results))
        nbr = results[0]
        for i in range(nbr):
            ligne = f.readline()
            elem = ligne.split()
            elem[i] = '1000000'
            results = map(int, elem)
            results = list(map(int, results))
            ring_cost.append(results)
        for i in range(nbr):
            ligne = f.readline()
            elem = ligne.split()
            # on oblige le sommet 1 a être dans le ring
            if i == 0:
                elem = ['1000000' for x in elem]

            elem[i] = '1000000'
            results = map(int, elem)
            results = list(map(int, results))
            affectation_cost.append(results)

    return ring_cost, affectation_cost

def evaluation(liste_ring,liste_affectation , ring_cost, affectation_cost):
    """

    :param ring_cost : matrice de cout du ring
    :param affectation_cost: matrice de cout des affectations
    :return: COST : le coup de la solution
    """
    cost = 0

    for i in range(len(liste_ring)):
        # evite le indice out of range quand on retombe sur le 1
        if i != len(liste_ring) - 1:
            cost += ring_cost[liste_ring[i] - 1][liste_ring[i+1]-1]


    for elem in liste_affectation:
        cost += int(affectation_cost[elem[0]-1][elem[1]-1])

    return cost

def rest(ring_solution,problem_size,restant):
    for i in range(problem_size):
        if i+1 not in ring_solution:
            restant.append(i+1)

    return restant

def delestage (ring_solution, affectation_solution , ring_cost, affectation_cost):
    temp = []
    #pour chaque sommet de du ring sauf le premier et le dernier(depot)
    for j in range(1, len(ring_solution) - 1):
        t = True

        for i in range(1, len(ring_solution)-1):
            if t == True :
                # si rejoindre le sommet avant et celui apres coute moins chers
                if ring_cost[ring_solution[i]-1][ring_solution[i-1]-1] + ring_cost[ring_solution[i]-1][ring_solution[i+1]-1]< ring_cost[ring_solution[i-1]-1][ring_solution[i+1]-1] + min(affectation_cost[ring_solution[i]-1]):
                    t = False
                    affectation_solution.append([ring_solution[i], min(affectation_cost[ring_solution[i]-1])])
                    del ring_solution[i]
            else :
                break



    return ring_solution, affectation_solution

