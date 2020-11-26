from full_ring import full_ring
from utils import lecture

ring_cost, affectation_cost = lecture("data1.dat")
solution = []

solution = full_ring(ring_cost)
print(len(solution))
print(len(ring_cost))
print(solution)
print(ring_cost)