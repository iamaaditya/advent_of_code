from itertools import product
from sys import maxint


def Cost_Calculator(d, part1, weapon, ring):

    augumented_items = weapon.copy()

    for k_ring in ring:
        for k_weapon in weapon:
            new_total = k_ring + k_weapon
            new_cost  = ring[k_ring] + weapon[k_weapon]
            # if that value already exists, update only if cheaper
            if new_total in weapon:
                if part1:
                    if weapon[new_total] < new_cost:
                        continue
                else:
                    if weapon[new_total] > new_cost:
                        continue

            augumented_items[new_total] = new_cost



    if d in augumented_items: return augumented_items[d]
    
    return maxint




def solve(part1):
    min_cost = maxint
    max_cost = -1 * maxint 

    weapon = {4:8, 5:10, 6:25, 7:40, 8:74}
    ring_weapon = {1:25, 2:50, 3:100}
    armor = {0:0, 1:13, 2:31, 3:53, 4:75, 5:102}
    ring_armor = {1: 20, 2:40, 3:60}
    
    # let the game begin
    for pd,pa in product(xrange(4,15), xrange(0,12)):
        current_cost = Cost_Calculator(pd, part1, weapon, ring_weapon) + Cost_Calculator(pa, part1, armor, ring_armor)

        bhp, bd, ba = 104, 8, 1

        php = 100

        while True:
            # player attacks
            bhp -= max(pd - ba, 1)
            if bhp <= 0: 
                min_cost = min(min_cost, current_cost)
                break 
            # boss attacks
            php -= max(bd - pa, 1)
            if php <= 0:
                max_cost = max(max_cost, current_cost)
                break

    if part1 : return min_cost
    
    return max_cost


print "Part1: " , solve(True)
print "Part2: " , solve(False)
