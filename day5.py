from itertools import groupby
import re

in_str = open('./input_data/input5.txt').read().splitlines()
# in_str = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
# in_str = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]


def Is_Nice_1(input):
    # Rule 3 (Disallowed substrings) 
    disallowed = set(['ab', 'cd', 'pq', 'xy'])
    for dis in disallowed:
        if input.find(dis) != -1:
            return False

    # Rule 1 (Vowels)
    vow_count = sum(map(input.count, list("aeiou")))
    if vow_count < 3: return False

    # Rule 2 
    repeated_letter_count = max([len(list(g)) for k, g in groupby(input)])
    if repeated_letter_count < 2: return False

    return True

         
def Part1():
    
    print len(filter(Is_Nice_1, in_str))


def Is_Nice_2(input):

    # Rule 1, two letter non-overlapping matches
    matches_1 = re.search(r'(\w\w).*\1', input)
    if matches_1 is None : return False


    # Rule 2, one letter repeats with another letter in between
    matches_2 = re.search(r'(\w)\w\1', input)
    if matches_2 is None: return False

    return True
    

def Part2():

    print len(filter(Is_Nice_2, in_str))

Part1()
Part2()

