from itertools import groupby

def look_and_say(input):
    """ for the given number, return it's look and say decoded number """
    new_string = []
    for k,g in groupby(input):
        # print k,g
        # print list(g)
        gl = list(g)
        new_string.append(str(len(gl)))
        new_string.append(gl[0])
    return new_string

# look_and_say(list('1211133444444'))
# print look_and_say(look_and_say(list('1211')))
input = list('1113222113')
for i in range(50):
    input = look_and_say(input)
    if i == 39: 
        print "After 40 iterations : " , len(input)

print "After 50 iterations : " , len(input)
