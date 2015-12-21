
in_str_plain = open('./input_data/input8.txt').read().splitlines()
# in_str_plain = open('./input_data/small.txt').read().splitlines()

def Part1():
    sum = 0
    for i, d in enumerate(in_str_plain):
        e =  unicode(d.decode('string-escape'),errors='replace')
        sum +=  len(d) -  (len(e) - 2) # 2 is for the quotes at the start
    print sum

def Part2():
    sum = 0
    for d in in_str_plain:
        sum += 2  + d.count('"') + d.count('\\') #+ len(d) (no need to subtract, as we want the difference, and also 2 is for the quotes
    print sum

Part1()
Part2()
