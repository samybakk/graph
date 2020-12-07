from flo.full_ring import full_ring
from utils import lecture
import copy as cp
from random import randint, sample, random
import time

liste1, liste2 = lecture("data1.dat")
class Ring_star:

    def __init__(self, in_ring, out_ring):
        self.in_ring = in_ring
        self.out_ring = out_ring
        self.score = self.cost(liste1,liste2)

    def cost(self, ring_cost, assign_cost): #Ne pas oublier de rajouter le 1 à la fin
        self.score = 0
        for index, edge in enumerate(self.in_ring):
            if index + 2 <= len(self.in_ring):

                self.score += ring_cost[int(edge - 1)][int(self.in_ring[int(index + 1)] - 1)]

        for edge in self.out_ring:
            assign_list = []
            for index, assign in enumerate(assign_cost[edge-1]):
                if index in self.in_ring:
                    assign_list.append(assign)
            self.score += min(assign_list)
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
            if edge not in self.out_ring:
                print(self.in_ring,'\n',self.out_ring)
                print(edge)
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
        best = self.ring_stars[0]
        best_score = best.cost(liste1,liste2)
        for ring_star in self.ring_stars:
            if ring_star.cost(liste1, liste2) < best_score:
                best = ring_star
                best_score = ring_star.cost(liste1, liste2)
    
        return best

def mutate(ring, rate):
    for i in range(len(ring.in_ring)):
        if random() < rate:
            if random() < 0.5:
                selected = sample(ring.in_ring[1:-1], 1)
                ring.swap(ring.in_ring[i], selected[0])
            else:
                selected = ring.in_ring[i]
                ring.switch(selected)
    for i in range(len(ring.out_ring)):
        if random() < rate:
            selected = ring.out_ring[i]
            ring.switch(selected)
def select(population, nbr):
    return Population(sample(population.ring_stars, nbr)).get_best()

def evolve(old_gen, rate, tourn_nbr, elit):
    new_gen = Population([])
    old_pop = len(old_gen.ring_stars)
    old_elit = old_pop // elit

    for i in range(old_elit):
        best = old_gen.get_best()
        new_gen.add(best)
        old_gen.remove_ring(best)

    #for _ in range(old_elit, old_pop):
        #parent_1 = select(old_gen, tourn_nbr)
        #parent_2 = select(old_gen, tourn_nbr)
        #child = crossover(parent_1, parent_2)
        #new_gen.add(child)
    
    for i in range(old_pop//2, old_pop):
        
        mutate(new_gen.ring_stars[i], rate)

    return new_gen

def crossover(ring_star1,ring_star2):
    nbr_edges = int(0.5*(len(ring_star1.in_ring)+len(ring_star2.in_ring)))
    new_ring_star = Ring_star([None for _ in range(nbr_edges)],[])
    cut_pos = randint(0,min(len(ring_star1.in_ring),len(ring_star2.in_ring)))
    for i in range(cut_pos) :
        new_ring_star.in_ring[i] = ring_star1.in_ring[i]
    
    for i in range(cut_pos,nbr_edges-1) :
        for j in ring_star2.in_ring :
            if j not in new_ring_star.in_ring :
                new_ring_star.in_ring[i] = ring_star2.in_ring[j]
        
    new_ring_star.in_ring = [i for i in new_ring_star.in_ring if i]
    
    new_ring_star.out_ring = [i for i in range(2,len(ring_star1.in_ring)+len(ring_star1.out_ring)) if i not in new_ring_star.in_ring]

    print(new_ring_star.in_ring)
    print(ring_star1)
    print(ring_star2)
    
    return new_ring_star

if __name__ == '__main__':
    pop_size = 100
    tourn_size = int(pop_size/4)
    mut_rate = 0.15
    elit = 1
    
    liste1, liste2 = lecture("data1.dat")
    list_ring,list_assign = cp.deepcopy(liste1),cp.deepcopy(liste2)
    ring = full_ring(list_ring,[x for x in range(1,len(liste1))],meta=False)
    ring_stars = []
    for x in range(pop_size):
        ring_stars.append(Ring_star(ring, []))
    
    Pop = Population(ring_stars)
    star = time.time()
    counter,min_score,gen = 0,1_000_000,0
    
    while counter < 10 :
        
        Pop = evolve(Pop, mut_rate, tourn_size, elit)
        score = Pop.get_best().score
    
        if score < min_score:
            counter, min_score = 0, score
        else:
            counter += 1
    
        gen += 1
     
     
    duree = round(time.time()-star,4)
    print('temps écoulé : ',duree,'\nbest sol : ',Pop.get_best().score,Pop.get_best().in_ring,Pop.get_best().out_ring)