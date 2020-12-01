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


def evaluation(file_solution_name, ring_cost, affectation_cost):
    """

    :param file_solution_name: la liste des sommet du ring dans l'ordre SANS LE 1 A LA FIN !!!!!
    :param ring_cost : matrice de cout du ring
    :param affectation_cost: matrice de cout des affectations
    :return: COST : le coup de la solution
    """
    cost = 0
    with open(file_solution_name) as f:
        h = f.readline().split()  # on s en balek de la premiere ligne
        h = f.readline().split()  # on recupere la liste de sommet qui est dans le ring
        h.append('1')
        ring_size = len(h)
        for i in range(len(h)):
            if i == len(h) - 1:
                cost += int(ring_cost[int(h[i]) - 1][int(h[0])])
            else:
                cost += int(ring_cost[int(h[i]) - 1][int(h[i + 1]) - 1])

        h = f.readline().split()  # on s'en balek de la troisième ligne
        for i in range(len(ring_cost) - ring_size):
            h = f.readline().split()
            cost += int(affectation_cost[int(h[0]) - 1][int(h[1]) - 1])
    return cost
