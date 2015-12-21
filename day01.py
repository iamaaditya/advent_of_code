from collections import Counter


# Part 1
list_common_char =  Counter(open('./input_data/input1.txt').readline()).most_common(2)

print "Total number of steps : ",
print list_common_char[0][1] - list_common_char[1][1]
print "In the direction of :", list_common_char[0][0]


# Part 2
inputStr = open('./input_data/input1.txt').readline().rstrip()

currentFloor = 0
steps = 0
for i in inputStr:
    steps += 1
    floor_value =  1 if i == '(' else -1
    currentFloor += floor_value
    if currentFloor == -1:
        print "You reached basement in step :", steps
        break






