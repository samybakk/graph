
def lecture (file_name) :
    liste = []
    with open(file_name) as f:
        ligne = f.readline()
        elem = ligne.split()
        results = map(int, elem)
        results = list(map(int, results))
        nbr = results[0]
        for i in range (nbr) :
            ligne = f.readline()
            elem = ligne.split()
            results = map(int, elem)
            results = list(map(int, results))
            liste.append(liste)

    return liste