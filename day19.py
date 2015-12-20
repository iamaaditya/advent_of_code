import re

input = open('./input_data/input19.txt').read().split('\n')

replacements = [i.split(' ')  for i in input[:-3]]
molecule = input[-2]


def Part1():
    total_sols = set()
    for r_from, _, r_to in replacements:
        for matches in re.finditer('%s'%r_from, molecule):
            pos =  matches.start()
            total_sols.add(molecule[:pos] + r_to + molecule[pos+len(r_from):]) # form the new string, by substituting, and add to set
    return len(total_sols)


def Part2():
    # arrange them in decreasing order of the replacement part (second part)
    replacements.sort(key=lambda item: len(item[2]), reverse=True)

    count = 0
    start_string = molecule
    while start_string != "e":
        for r_to, _ , r_from in replacements:
            while True:
                if start_string.find(r_from) == -1: break
                start_string = start_string.replace(r_from, r_to, 1)
                count += 1
    return count

print "Part1: ", Part1()
print "Part2: ", Part2() 
