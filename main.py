from utils import lecture
import numpy as np
from geneticalgorithm import geneticalgorithm as ga

liste1, liste2 = lecture("data1.dat")
connec = [-1 for x in liste1[0]]
def f(X,liste1=liste1,liste2=liste2):
    somme =0
    
    for pos,x in enumerate(X) :
        if x ==1.0 :
            for y in range(pos,len(X)):
                pos_next = 0
                if y ==1.0 :
                    pos_next = y
                    
            connec[pos] = pos_next
            somme += liste1[pos][pos_next]
            
        else :
            pos_next = min(liste2[pos])
            connec[pos] = pos_next
            somme += liste2[pos][pos_next]
        
    
    
   
    return somme

if __name__ == '__main__':
 

    restants = [x for x in range(1,len(liste1))]

    algorithm_param = {'max_num_iteration': 10000, \
                       'population_size': 100, \
                       'mutation_probability': 0.1, \
                       'elit_ratio': 0.01, \
                       'crossover_probability': 0.5, \
                       'parents_portion': 0.3, \
                       'crossover_type': 'uniform', \
                       'max_iteration_without_improv': 50}

    model = ga(function=f, dimension=len(restants),algorithm_parameters=algorithm_param, variable_type='bool')

    model.run()
    
    print(connec)