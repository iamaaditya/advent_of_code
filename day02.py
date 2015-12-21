lines = open('./input_data/input2.txt').read().splitlines()
dimensions = [map(int, l.split('x')) for l in lines]

# Part 1
total_area = 0
for a,b,c in dimensions:
    total_area += 2 * a * b + 2 * b * c + 2 * a * c + min(a*b, b*c, c*a)

print "Square feet of wrapping paper required is : ", total_area

# Part 2
total_length = 0
for a,b,c in dimensions:
    total_length += min(2 * (a + b) , 2 * (b + c), 2 * (c + a)) + a*b*c

print "Length of ribbon required is : ", total_length



