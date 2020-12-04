from full_ring import full_ring
from utils import lecture, delestage, evaluation

ring_cost, affectation_cost = lecture("data1.dat")
problem_size = len(ring_cost)
ring_solution = []
affectation_solution = []

print(ring_cost)
ring_solution = full_ring(ring_cost)
print(ring_cost)

#ring_solution, affectation_solution = delestage(ring_solution, affectation_solution , ring_cost, affectation_cost)
objectif = evaluation (ring_solution, affectation_solution  , ring_cost, affectation_cost)
print(ring_solution)
print(affectation_solution)
print('objectif = ' + str(objectif))
print(ring_cost)

