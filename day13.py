from itertools import permutations
import sys

input = open('./input_data/input13.txt').read().splitlines()

cross_happiness_dict = {}
names = set()
for ii in input:
    i = ii.replace('.', '')
    l = i.split(' ')
    names.add(l[0])
    value = int(l[3])
    value = value if l[2] == 'gain' else -1 * value
    # print l[0], l[-1], l[2], l[3]
    cross_happiness_dict[( l[0], l[-1])] = value


def Happiness_of_Current_Arrangment(path):
    """ for the given path, returns the happiness """
    happiness = 0
    for i in range(len(path)-1):
        happiness += cross_happiness_dict[(path[i], path[i+1])]
    happiness += cross_happiness_dict[(path[0], path[-1])]
    return happiness

def Calculate_Maximum_Happiness():
    max_happiness = -1*sys.maxint
    for i in  permutations(names):
        current_happiness = Happiness_of_Current_Arrangment(i) + Happiness_of_Current_Arrangment(i[::-1])
        max_happiness = max(max_happiness, current_happiness)
    return max_happiness

# Part A
print "Maximum happiness of all arrangment : ", Calculate_Maximum_Happiness()

for name in names:
    cross_happiness_dict[('me',name)] = 0
    cross_happiness_dict[(name, 'me')] = 0

names.add('me')

# Part B
print "Maximum happiness of all arrangment (incl me): ", Calculate_Maximum_Happiness()
