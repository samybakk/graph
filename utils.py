
def lecture(file_name):
    liste1= []
    liste2= []
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
            liste1.append(results)
        for i in range(nbr):
            ligne = f.readline()
            elem = ligne.split()
            results = map(int, elem)
            results = list(map(int, results))
            liste2.append(results)

    return liste1, liste2,