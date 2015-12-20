def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
def Part2():
    i = 1
    while True:
        ans = sum([f * 11 for f in factors(i) if f * 50 >= i])
        if ans >= 34000000: return i
        i += 1

def Part1():
    i = 1
    while True:
        ans = sum([f * 10 for f in factors(i)])
        if ans >= 34000000: return i

print "Part1: ", Part1()
print "Part2: ", Part2()

