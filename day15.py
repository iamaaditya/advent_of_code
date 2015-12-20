from itertools import product
input = open('./input_data/input15.txt').read().splitlines()

data = [map(int, ip.replace(',','').split(' ')[2::2]) for ip in input]

def solve_cookie(calorie_flag):
    maxprod = 0
    for a, b, c in product(xrange(100), xrange(100), xrange(100)):

        d = 100 - (a + b + c)
        if d < 0: continue
        
        int_list = [a,b,c,d]

        if(calorie_flag):
            total_calories = sum([ingre[-1] * amt for ingre, amt in zip(data, int_list)])
            if total_calories != 500: continue

        prod = 1
        for i in xrange(4):
            temp_sum = sum([ingre[i] * amt for ingre, amt in zip(data, int_list)])
            if temp_sum < 0:
                prod = 0
                break
            prod *= temp_sum
        
        maxprod = max(prod,maxprod)
    return maxprod

print solve_cookie(False)
print solve_cookie(True)
