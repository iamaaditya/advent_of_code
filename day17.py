from itertools import combinations
from collections import Counter

input = open('./input_data/input17.txt').read().splitlines()
containers = map(int, input)
# containers = sorted([20, 15, 10, 5, 5])

# items = [(1,i) for i in containers]
# print items


sol_count = 0
container_counter = Counter()
for n in xrange(1, len(containers) + 1):
    for i in combinations(containers,n):
        if sum(i) == 150: 
            # sol_count +=1 
            container_counter[len(i)] += 1

print "sol_count: ", sol_count
print container_counter
         # print i


