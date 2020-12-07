from flo.full_ring import full_ring
from utils import lecture
import copy as cp
from random import randint, sample, random,uniform
import time

liste1, liste2 = lecture("data2.dat")
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
        else:
            self.in_ring.insert(randint(1, len(self.in_ring)-1), edge)
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
        best.cost(liste1,liste2)
        for ring_star in self.ring_stars:
            if ring_star.cost(liste1, liste2) < best.score:
                best = ring_star
                best.score = ring_star.cost(liste1, liste2)
    
        return best

def mutate(ring, rate):
    for element in ring.in_ring[1:-1]:
        if len(ring.in_ring) > 2:
            if random() < rate:
                if random() < 0.5:
                        selected = sample(ring.in_ring[1:-1], 1)
                        ring.swap(element, selected[0])
                else:
                    ring.switch(element)
    for element in ring.out_ring:
        if random() < rate:
            ring.switch(element)

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

    for _ in range(old_elit, old_pop):
        parent_1 = select(old_gen, tourn_nbr)
        parent_2 = select(old_gen, tourn_nbr)
        child = crossover(parent_1, parent_2)
        new_gen.add(child)
    
    for i in range(1, len(new_gen.ring_stars)):
        mutate(new_gen.ring_stars[i],uniform(rate/10,rate))

    return new_gen

def crossover(ring_star1,ring_star2):
    cut_pos1 = randint(1, len(ring_star1.in_ring)-1)
    cut_pos2 = randint(1, len(ring_star2.in_ring)-1)
    new_ring_star = Ring_star([],[])
    new_ring_star.in_ring.append(1)
    for i in range(1, cut_pos1):
        new_ring_star.in_ring.append(ring_star1.in_ring[i])

    for i in range(cut_pos2,len(ring_star2.in_ring)-1):
        if ring_star2.in_ring[i] not in new_ring_star.in_ring:
            new_ring_star.in_ring.append(ring_star2.in_ring[i])

    new_ring_star.in_ring.append(1)

    new_ring_star.out_ring = [i for i in range(2,len(ring_star1.in_ring)+len(ring_star1.out_ring)) if i not in new_ring_star.in_ring]
    
    return new_ring_star

if __name__ == '__main__':
    pop_size = 500
    tourn_size = int(pop_size/4)
    mut_rate = 0.25
    elit = 4

    list_ring,list_assign = cp.deepcopy(liste1),cp.deepcopy(liste2)
    ring = full_ring(list_ring,[x for x in range(1,len(liste1)+1)],meta=False, Tcoef=0.9)
    ring_stars = []
    for x in range(pop_size):
        ring_stars.append(Ring_star(cp.deepcopy(ring), []))

    Pop = Population(ring_stars)
    star = time.time()
    

    counter, min_score, gen = 0, 100000000, 0
    while counter < 10 :
        
        Pop = evolve(Pop, mut_rate, tourn_size, elit)

        best_pop = Pop.get_best()
        score_pop = Pop.get_best().cost(liste1, liste2)
    
        if score_pop < min_score:
            best = best_pop
            counter, min_score = 0, score_pop

        else:
            counter += 1


        print("gen : ",gen,'\nbest : ',best.in_ring,best.out_ring,'\ncost : ',min_score)
        gen += 1
     
     
    duree = round(time.time()-star,4)
    print('temps écoulé : ',duree,'\nbest sol : ',min_score,best.in_ring,best.out_ring)