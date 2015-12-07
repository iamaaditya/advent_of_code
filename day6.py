from collections import defaultdict

input_str = open('./input_data/input6.txt').read().splitlines()
# input_str = ['turn on 0,0 through 999,999', 'toggle 0,0 through 999,0', 'turn off 499,499 through 500,500']


def read_line(input):
    input_split = input.split(' ')
    if input_split[0] == 'toggle':
        return input_split[0], map(int, input_split[1].split(',')), map(int, input_split[3].split(','))
    return input_split[1], map(int, input_split[2].split(',')), map(int, input_split[4].split(','))

def Part1():

    visited = defaultdict(lambda: False)

    for in_data in input_str:
        operation, start, end =  read_line(in_data)
        for x in xrange(start[0], end[0]+1):
            for y in xrange(start[1], end[1]+1):
                if operation == "toggle":
                    visited[(x,y)] = not visited[(x,y)]
                elif operation == "on":
                    visited[(x,y)] = True
                else:
                    visited[(x,y)] = False

    print "Total number of ON lights are : ", sum([1 for k in visited if visited[k]])


def Part2():

    visited = defaultdict(lambda: 0)

    for in_data in input_str:
        operation, start, end = read_line(in_data)
        for x in xrange(start[0], end[0]+1):
            for y in xrange(start[1], end[1]+1):
                if operation == "toggle":
                    visited[(x,y)] += 2
                elif operation == "on":
                    visited[(x,y)] += 1
                else:
                    visited[(x,y)] = max(0, visited[(x,y)]-1)
    
    print "Total brightness of lights is : ", sum([visited[k] for k in visited])

Part1()
Part2()
