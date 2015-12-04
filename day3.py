from collections import defaultdict

data = open('./input_data/input3.txt').readline().rstrip()
# data = "^v^v^v^v^v"

def move(x,y, step):
        if step == '^':
            x += 1
        elif step == 'v':
            x -= 1
        elif step == '>':
            y += 1
        elif step == '<':
            y -= 1
        else:
            print "Unrecognized value as step !! Error !!!"
        return x,y

def part1():
    """ Only Santa """
    visited = defaultdict(lambda: 0)
    # let the starting value is 0,0, which is visited by definition
    x,y = 0,0
    visited[(x,y)] += 1

    for step in data:
        x,y = move(x,y,step)
        visited[(x,y)] += 1

    print "Total number of houses visited is : ", len(visited)

def part2():
    """ Santa (_s) and Robo Santa (_r) """

    visited = defaultdict(lambda: 0)
    x_s, y_s = 0,0
    x_r, y_r = 0,0

    visited[(x_s,y_s)] += 2 # initial visit is same and they get two present

    for i in xrange(0, len(data)-1, 2):
        step_s = data[i]
        step_r = data[i+1]
        x_s, y_s = move(x_s, y_s, step_s)
        x_r, y_r = move(x_r, y_r, step_r)
        visited[(x_s, y_s)] += 1
        visited[(x_r, y_r)] += 1

    # if the data is odd length
    if len(data) % 2:
        step_s = data[-1]
        x_s, y_s = move(x_s, y_s, step_s)
        visited[(x_s, y_s)] += 1

    print "Total number of houses visited is : ", len(visited)


part1()
part2()
