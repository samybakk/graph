from full_ring import full_ring
from evaluate import evaluate
from utils import lecture
import numpy as np
import copy as cp




    
 
 
if __name__ == '__main__':
    liste1, liste2 = lecture("data1.dat")
    list_ring,list_assign = cp.deepcopy(liste1),cp.deepcopy(liste2)
    ring = full_ring(list_ring)
    print("initial ring : ",ring)
    
    
    finished = False
    for x in range (10) :
        print("epoch : ",str(x))
        ring = ring [:-1]
        
        score_list = []
        result_list = []
        
        
        
        for _ in range(99) :
    
            
            egdes_nbr = len(ring)
            in_ring = [x for x in range(1,egdes_nbr+1) if x in ring]
            out_ring = [x for x in range(1,egdes_nbr+1) if x not in ring]
            
            
            for edge in ring :
                
                if np.random.random_sample() < 0.15 :
                    if edge in in_ring :
                        in_ring.remove(edge)
                    else :
                        in_ring.append(edge)
                    
            
            in_ring = np.random.permutation(in_ring[1:])
            in_ring = np.insert(in_ring,0,1)
            in_ring = np.insert(in_ring,len(in_ring),1)
            
            
            score = evaluate(in_ring,out_ring,liste1,liste2)
            
            score_list.append(score)
            result_list.append((in_ring,out_ring))
         
        print('best child score : ',str(min(score_list)))
        best_child_index = score_list.index(min(score_list))
        ring = result_list[best_child_index][0]

