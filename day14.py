import re
from itertools import repeat

input = open('./input_data/input14.txt').read().splitlines()

regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
data = [(name, int(speed),int(fly),int(sleep)) for ip in input for name,speed,fly,sleep in re.findall(regex, ip)]


distance = list(repeat(0, len(data)))
points = list(repeat(0, len(data)))
deer_fly = [ik[2] for ik in data]
deer_sleep  = [ik[3] for ik in data]

time_ = 2503 

for t in xrange(1,time_+1):
    for index, r in enumerate(data):

        if deer_fly[index] : 
            distance[index] += r[1]
            deer_fly[index] -= 1

        elif deer_sleep[index] :
            deer_sleep[index] -= 1

        else:
            deer_fly[index] = r[2] -1
            deer_sleep[index] = r[3]
            distance[index] += r[1]
    
    md = max(distance)
    for i,d in enumerate(distance):
        if d == max(distance):
            points[i] += 1

print max(distance)
print max( points )



