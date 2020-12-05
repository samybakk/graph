def re_size_tabu (tabu_liste,max_size_tabu):
    while len(tabu_liste) > max_size_tabu :
        del tabu_liste[0]