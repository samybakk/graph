
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
            results = map(int, elem)
            results = list(map(int, results))
            ring_cost.append(results)
        for i in range(nbr):
            ligne = f.readline()
            elem = ligne.split()
            results = map(int, elem)
            results = list(map(int, results))
            affectation_cost.append(results)

    return ring_cost, affectation_cost
