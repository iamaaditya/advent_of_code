from itertools import product

input = open('./input_data/input18.txt').read().splitlines()


def run_state(current_state):
    list_positions_flip = []
    for i,j in product(xrange(gridSize), xrange(gridSize)):

        count_of_on_nei = 0
        for m,n in product(xrange(-1,2), xrange(-1,2)):
            if m==0 and n == 0: continue # because 0,0 is not neighbour but itself
            if i+m<0 or j+n < 0: # because in python negative indexes do not throw error, but traverse list in reverse order
                continue
            try:
                if current_state[i+m][j+n] == '#': count_of_on_nei += 1
            except:
                pass
        if current_state[i][j] == '#':
            if count_of_on_nei not in [2,3]: list_positions_flip.append((i,j))
        else:
            if count_of_on_nei == 3: list_positions_flip.append((i,j))

    return list_positions_flip

def flip_switches(current_state, list_positions_flip, Part1):

    for i,j in list_positions_flip:
        if not Part1:
            if (i,j) in [(0,0), (0,gridSize-1), (gridSize-1,0), (gridSize-1, gridSize-1)]: continue
        if current_state[i][j] == '#': current_state[i][j] = '.'
        else: current_state[i][j] = '#'

    return current_state


def run_X_steps(input, X, Part1=True):
    current_state = []
    for item in input:
        current_state.append(list(item))

    if not Part1:
        # make all the four corners on
        for i,j in four_corners:
            current_state[i][j] = '#'

    for i in xrange(X):
        current_state = flip_switches(current_state, run_state(current_state), Part1)

    return current_state


gridSize = 100
number_of_steps = 100
four_corners = [(0,0), (0,gridSize-1), (gridSize-1,0), (gridSize-1, gridSize-1)]
# count number of lights on
print "Part1 : " , sum([i.count('#') for i in run_X_steps(input, number_of_steps)])
print "Part2 : " , sum([i.count('#') for i in run_X_steps(input, number_of_steps, False)])



