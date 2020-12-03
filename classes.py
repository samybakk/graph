from full_ring import full_ring
from utils import lecture
import copy as cp
import random

class ring_star:

    def __init__(self, in_ring, out_ring):
        self.in_ring = in_ring
        self.out_ring = out_ring
        self.score = 0

    def cost(self, ring_cost, assign_cost):
        self.score = 0
        for index, edge in enumerate(self.in_ring):
            if index + 2 <= len(self.in_ring):

                self.score += ring_cost[int(edge - 1)][int(self.in_ring[int(index + 1)] - 1)]

        for index, edge in enumerate(self.out_ring):
            self.score += min(assign_cost[edge - 1])
        return self.score

    def swap(self, edge1, edge2):
        index1 = self.in_ring.index(edge1)
        index2 = self.in_ring.index(edge2)
        tmp = self.in_ring[index1]
        self.in_ring[index1] = self.in_ring[index2]
        self.in_ring[index2] = tmp
    
class population :
    def __init__(self,ring_stars):
        self.ring_stars = ring_stars
        
    def add(self,ring_star):
        self.ring_stars.append(ring_star)
    
    def remove_ring(self,ring_star):
        self.ring_stars.remove(ring_star)

    def get_best(self):
        best = self.individuals[0]
        for ring_star in self.individuals:
            if ring_star.score > best.score:
                best = ring_star
    
        return best
    
    
    
    
def crossover(ring_star1,ring_star2):
    nbr_edges = int(0.5*(len(ring_star1.in_ring)+len(ring_star2.in_ring)))
    new_ring_star = ring_star([None for _ in range(nbr_edges)],[])
    cut_pos = random.randint(0,min(len(ring_star1.in_ring)+len(ring_star2.in_ring)))
    for i in range(cut_pos) :
        new_ring_star.in_ring[i] = ring_star1[i]
    
    for i in range(cut_pos,nbr_edges-1) :
        for j in ring_star2.in_ring :
            if j not in new_ring_star.in_ring :
                new_ring_star.in_ring[i] = ring_star2[j]
        
    new_ring_star.in_ring = [i for i in new_ring_star if i]
    
    new_ring_star.out_ring = [i for i in range(2,len(ring_star1.in_ring)+len(ring_star1.out_ring)) if i not in new_ring_star.in_ring]
    
    
    return new_ring_star
        
if __name__ == '__main__':
    liste1, liste2 = lecture("data1.dat")
    list_ring,list_assign = cp.deepcopy(liste1),cp.deepcopy(liste2)
    ring = full_ring(list_ring)
    test = ring_star(ring,[])
    print(test.cost(liste1, liste2))