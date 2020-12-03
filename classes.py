from full_ring import full_ring
from utils import lecture
import copy as cp

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

if __name__ == '__main__':
    liste1, liste2 = lecture("data1.dat")
    list_ring,list_assign = cp.deepcopy(liste1),cp.deepcopy(liste2)
    ring = full_ring(list_ring)
    test = ring_star(ring,[])
    print(test.cost(liste1, liste2))