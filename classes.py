from full_ring import full_ring
from utils import lecture
import copy as cp
from random import randint, sample, random

class Ring_star:

    def __init__(self, in_ring, out_ring):
        self.in_ring = in_ring
        self.out_ring = out_ring
        self.score = 0

    def cost(self, ring_cost, assign_cost): #Ne pas oublier de rajouter le 1 à la fin
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

    def switch(self, edge):
        if edge in self.in_ring:
            self.in_ring.remove(edge)
            self.out_ring.append(edge)
        if edge not in self.in_ring:
            self.in_ring.insert(randint(0, len(self.in_ring)), edge)
            self.out_ring.remove(edge)
    
class Population :
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

def mutate(ring, rate):
    for _ in range(len(ring.in_ring)):
        if random() < rate:
            if random() < 0.5:
                selected = sample(ring.in_ring, 2)
                ring.swap(selected[0], selected[1])
            else:
                selected = sample(ring.in_ring, 1)
                ring.switch(selected)

def select(population, nbr):
    return Population(sample(population, nbr).get_best())

def evolve(old_gen, rate, tourn_nbr, elit):
    new_gen = Population([])
    old_pop = len(old_gen.ring_stars)
    old_elit = old_pop // elit

    for i in range(old_elit):
        best = old_gen.get_best()
        new_gen.add(best)
        old_gen.remove_ring(best)

    for _ in range(old_elit, old_pop):
        parent_1 = select(new_gen, tourn_nbr)
        parent_2 = select(new_gen, tourn_nbr)
        child = crossover(parent_1, parent_2)
        new_gen.add(child)

    for i in range(old_elit, old_pop):
        mutate(new_gen.individuals[i], rate)

    return new_gen

if __name__ == '__main__':
    liste1, liste2 = lecture("data1.dat")
    list_ring,list_assign = cp.deepcopy(liste1),cp.deepcopy(liste2)
    ring = full_ring(list_ring)
    test = Ring_star(ring,[])
    print(test.cost(liste1, liste2))