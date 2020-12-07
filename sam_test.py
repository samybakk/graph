from flo.full_ring import full_ring
from evaluate import evaluate
from utils import lecture
import numpy as np
import copy as cp

 
if __name__ == '__main__':
    liste1, liste2 = lecture("data1.dat")
    list_ring,list_assign = cp.deepcopy(liste1), cp.deepcopy(liste2)
    ring = full_ring(list_ring)
    print("initial ring : ", ring)
    
    
    egdes_nbr = len(ring)
    history = [ring]
    for x in range (10) : #while counter < n_generation
        print("epoch : ",str(x))
        
        
        score_list = []
        result_list = []
        
        
        
        for _ in range(99) :
            
            ring = ring[1:-1]
            
            in_ring =  list(ring)
            out_ring = [x for x in range(2,egdes_nbr) if x not in ring]

            #in_ring = in_ring[1:]
            for edge in range(2,egdes_nbr) :
                
                if np.random.random_sample() < 0.05 :
                    if edge in in_ring :
                        in_ring.remove(edge)
                        out_ring.append(edge)
                    else :
                        in_ring.append(edge)
                        out_ring.remove(edge)
            
            
            #in_ring = np.random.permutation(in_ring)
            
            in_ring = np.insert(in_ring,0,1)
            in_ring = np.insert(in_ring,len(in_ring),1)

            #print(in_ring, out_ring)
            score = evaluate(in_ring,out_ring,liste1,liste2)
            
            score_list.append(score)
            result_list.append((in_ring,out_ring))
         
        print('best child score : ',str(min(score_list)))
        best_child_index = score_list.index(min(score_list))
        ring = result_list[best_child_index][0]
        

    print('final ring : ', ring)