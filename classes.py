import copy as cp
from random import randint, sample, random,uniform
import time

def lecture(file_name):
    ring_cost = []
    affectation_cost = []
    with open(file_name) as f:
        ligne = f.readline()
        elem = ligne.split()
        results = map(int, elem)
        results = list(map(int, results))
        nbr = results[0]
        for i in range(nbr):
            ligne = f.readline()
            elem = ligne.split()
            elem[i] = '1000000'
            results = map(int, elem)
            results = list(map(int, results))
            ring_cost.append(results)
        for i in range(nbr):
            ligne = f.readline()
            elem = ligne.split()
            # on oblige le sommet 1 a être dans le ring
            if i == 0:
                elem = ['1000000' for x in elem]

            elem[i] = '1000000'
            results = map(int, elem)
            results = list(map(int, results))
            affectation_cost.append(results)

    return ring_cost, affectation_cost

liste1, liste2 = lecture("data3.dat")

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
                if index+1 in self.in_ring:
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


def lecture(file_name):
    ring_cost = []
    affectation_cost = []
    with open(file_name) as f:
        ligne = f.readline()
        elem = ligne.split()
        results = map(int, elem)
        results = list(map(int, results))
        nbr = results[0]
        for i in range(nbr):
            ligne = f.readline()
            elem = ligne.split()
            elem[i] = '1000000'
            results = map(int, elem)
            results = list(map(int, results))
            ring_cost.append(results)
        for i in range(nbr):
            ligne = f.readline()
            elem = ligne.split()
            # on oblige le sommet 1 a être dans le ring
            if i == 0:
                elem = ['1000000' for x in elem]

            elem[i] = '1000000'
            results = map(int, elem)
            results = list(map(int, results))
            affectation_cost.append(results)

    return ring_cost, affectation_cost

def evaluation(liste_ring,liste_affectation , ring_cost, affectation_cost):
    """

    :param ring_cost : matrice de cout du ring
    :param affectation_cost: matrice de cout des affectations
    :return: COST : le coup de la solution
    """
    cost = 0

    for i in range(len(liste_ring)):
        # evite le indice out of range quand on retombe sur le 1
        if i != len(liste_ring) - 1:
            cost += ring_cost[liste_ring[i] - 1][liste_ring[i+1]-1]


    for elem in liste_affectation:
        cost += affectation_cost[elem[0]-1][elem[1]-1]

    return cost


def full_ring(ring_cost,ring_sommet, meta ,Tcoef):
    temp_ring_cost = cp.deepcopy(ring_cost)

    sol = [1]
    autre = []

    #on calcul les sommet qui sont pas dans le ring
    for i in range(len(ring_cost)):
        if i + 1 not in ring_sommet:
            autre.append(i + 1)

    #on back ce qui rentre pas dans le ring
    for elem in autre:
        for temp in range(len(temp_ring_cost[elem-1])):
            temp_ring_cost[elem-1][temp] = 1000000
        for temp in temp_ring_cost:
            temp[elem-1] = 1000000


    # on cré le ring
    for i in range(len(ring_sommet)):
        # on trouve la meilleur possibilité locale et on met a jour la solution
        h = temp_ring_cost[sol[-1]-1].index(min(temp_ring_cost[sol[-1]-1]))
        sol.append(h+1)

        # on corrige la matrice ring_coast pour empecher de cycler
        for elem in range(len(temp_ring_cost[sol[-2]-1])):
            temp_ring_cost[sol[-2]-1][elem]= 1000000
        for elem in temp_ring_cost:
            elem[sol[-2]-1] = 1000000

    best_sol = cp.deepcopy(sol)


    if meta == True :
        size_tabu = len(ring_sommet) * (Tcoef) +1
        best_cost = evaluation(best_sol, [], ring_cost, [])
        tabu = [1]
        for i in range(len(ring_sommet)**2):
            ref = randint(1, len(ring_sommet)-1)
            if ref not in tabu:
                if ref == 1:
                    temp = sol[ref]
                    sol[ref] = sol[ref+1]
                    sol[ref + 1] = temp
                    cost = evaluation(sol, [], ring_cost, [])
                    print('coucou')
                elif id == len(ring_sommet)-1:
                    temp = sol[ref]
                    sol[ref] = sol[ref - 1]
                    sol[ref - 1] = temp
                    cost = evaluation(sol, [], ring_cost, [])
                    print('coucou gf')
                else:

                    temp = sol[ref]
                    sol[ref] = sol[ref + 1]
                    sol[ref + 1] = temp
                    cost1 = evaluation(sol, [], ring_cost, [])
                    G1 = sol

                    temp = sol[ref+1]
                    sol[ref+1] = sol[ref]
                    sol[ref] = temp
                    temp = sol[ref]
                    sol[ref] = sol[ref - 1]
                    sol[ref - 1] = temp
                    cost2 = evaluation(sol, [], ring_cost, [])

                    if cost2 >= cost1:
                        cost = cost1
                        sol = G1

                    if cost1 > cost2:
                        cost = cost2

                if cost <= best_cost:
                    best_cost = cost
                    best_sol = cp.deepcopy(sol)
                if cost > best_cost:
                    tabu.append(ref)

            if len(tabu) > size_tabu:
                del tabu[1]

    return best_sol

if __name__ == '__main__':
    
    
    
    pop_size = 400
    tourn_size = int(pop_size/4)
    mut_rate = 0.1
    elit = 10

    list_ring,list_assign = cp.deepcopy(liste1),cp.deepcopy(liste2)
    ring = full_ring(list_ring,[x for x in range(1,len(liste1)+1)],meta=False, Tcoef=0.9)
    ring_stars = []
    for x in range(pop_size):
        ring_stars.append(Ring_star(cp.deepcopy(ring), []))
        
    
    Pop = Population(ring_stars)
    star = time.time()
    

    counter, min_score, gen = 0, 100000000, 1
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
    out_ring_txt = []
    for edge in best.out_ring :
        assign_list = []
        for index, assign in enumerate(liste2[edge - 1]):
            if index + 1 in best.in_ring:
                assign_list.append(assign)
            else :
                assign_list.append(10000000)
        edge_connec = assign_list.index(min(assign_list))+1
        out_ring_txt.append((edge,edge_connec))
    

    with open("Groupe9-Challenge1.txt", "w") as w:
        w.write('RING ' + str(len(best.in_ring)-1) + " \n")
        for elem in best.in_ring[:-1]:
            w.write(str(elem) + ' ')
        w.write(" \n")
        w.write("STAR \n")
        for elem in out_ring_txt:
            w.write(str(elem[0]) + " " + str(elem[1]) + " \n")
    
        w.write("COST " + str(min_score) + " \n")