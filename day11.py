from itertools import groupby

def contains_3_incr_letter(input):
    for i in range(len(input)-2):
        # print input[i], input[i+1], input[i+2]
        if ord(input[i]) + 1 == ord(input[i+1]) and ord(input[i+1]) + 1 == ord(input[i+2]): return True
    return False

def contains_no_iol(input):
    for x in ['i','o','l']:
        if x in input: return False
    return True

def contains_two_pairs(input):
    list_len_groups = [len(list(g)) for _,g in groupby(input)]
    if max(list_len_groups) >= 4: return True # this is in the case of aaaa

    if [l > 1 for l in list_len_groups].count(True) > 1: return True
    # return .count(True) > 1
    return False

def Is_password_valid(input):

    # Check condition one
    # change this into map and all
    if contains_3_incr_letter(input) and contains_two_pairs(input) and contains_no_iol(input):
        return True
    return False


def generate_new_valid_password(input):

    while True:
        l = list(input)
        for i, _ in reversed(list(enumerate(l))):
            if l[i] != 'z':
                l[i] = chr(ord(l[i])+1)
                break
            else:
                l[i] = 'a'
        input = l[::] # remember, else it is just a reference !!!
        if Is_password_valid(input): return ''.join(input)

next_password =  generate_new_valid_password('hxbxwxba')
print "Next Password for Santa shoudl be :" , next_password
print "Next Next Password for Santa should be : " , generate_new_valid_password(next_password)



