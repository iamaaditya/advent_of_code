import re
import json

input = open('./input_data/input12.txt').read()
nums_pattern = re.compile(r"[+-]?\d+(?:\.\d+)?") # generic pattern for numbers, positive, negative, decimal
numbers = re.findall(nums_pattern, input)

print "Part 1 sum : " , sum(map(int, numbers))


stack = json.load(open('./input_data/input12.txt'))
numbers = []
while stack:
    item = stack.pop()
    if type(item) == int:
        numbers.append(item)
    elif type(item) == dict:
        if "red" in item.values():
            continue
        for key in item:
            stack.append(item[key])
    elif type(item) == list: 
        for list_items in item:
            stack.append(list_items)
    else:
        continue

print "Part 2 sum without red in objects: " , sum(numbers)
