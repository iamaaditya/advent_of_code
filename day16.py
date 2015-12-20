import re
input = open('./input_data/input16.txt').read()

sue_list = []
pattern = r'Sue (\d)+: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
for il in re.findall(pattern, input):
    dic_data = {}
    dic_data[il[1]] = int( il[2] )
    dic_data[il[3]] = int( il[4] )
    dic_data[il[5]] = int( il[6] )
    sue_list.append(dic_data)

m = {}
m['children'] = 3
m['cats'] = 7
m['samoyeds'] = 2
m['pomeranians'] = 3
m['akitas'] = 0
m['vizslas'] = 0
m['goldfish'] = 5
m['trees'] = 3
m['cars'] = 2
m['perfumes'] = 1

def find_aunt_sue(Part1):
    for index, sue in enumerate(sue_list):

        if Part1:
            found = ([sue[k] == m[k] for k in sue])

        else:
            found = []
            for k in sue:
                if k in ['cats', 'trees']:
                    found.append( sue[k] > m[k] )
                elif k in ['pomeranians', 'goldfish']:
                    found.append( sue[k] < m[k] )
                else:
                    found.append( sue[k] == m[k] )

        # if found the Aunt !
        if all(found): return index + 1

print "Part 1  ", find_aunt_sue(True)
print "Part 2  ", find_aunt_sue(False)
