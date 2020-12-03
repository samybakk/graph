def evaluate (in_ring ,out_ring ,liste1 ,liste2) :
    score = 0
    for index ,edge in enumerate(in_ring) :
        if index +2 <= len(in_ring) :
            score += liste1[int(edge -1)][int(in_ring[int(index +1) ] -1)]
    
    for index ,edge in enumerate(out_ring) :
        score += min(liste2[edge -1])
    
    return score