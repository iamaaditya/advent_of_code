from itertools import permutations
import sys

in_str = open('./input_data/input9.txt').read().splitlines()


node_list = set()
edge_dic = {}

for str in in_str:
    node_from, _, node_to, _, weight = str.split(' ')
    weight = int(weight)
    
    node_list.add(node_from)
    node_list.add(node_to)

    edge_dic[(node_from,node_to)] = weight
    edge_dic[(node_to,node_from)] = weight

def Cost_of_Hamiltonian_Path(path):
    """ for the given path, returns the cost """
    cost = 0
    for i in range(len(path)-1):
        cost += edge_dic[(path[i], path[i+1])]
    return cost

min_cost = sys.maxint
max_cost = -1*sys.maxint
for i in  permutations(node_list):
    current_cost = Cost_of_Hamiltonian_Path(i)
    min_cost = min(min_cost, current_cost)
    max_cost = max(max_cost, current_cost)

print "Min Cost : ", min_cost
print "Max Cost : ", max_cost
