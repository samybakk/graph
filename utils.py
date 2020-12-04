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
        if i != len(liste_ring) - 1: # evite le indice out of range quand on retombe sur le 1
            cost += int(ring_cost[liste_ring[i] - 1][liste_ring[i+1]]-1)


    for elem in liste_affectation:
        cost += int(affectation_cost[elem[0]-1][elem[1]-1])

    return cost
