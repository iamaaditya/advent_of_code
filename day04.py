import hashlib

def Find_lowest_integer(trailing_zeros):
    i = 0
    while True:
        i += 1
        m = hashlib.md5()
        in_str = "ckczppom" + str(i)
        m.update(in_str)
        out_str =  m.hexdigest()[:trailing_zeros]
        # print out_str
        if out_str == "0"*trailing_zeros:
            print in_str, i
            break

# Solution to part 1
Find_lowest_integer(5)

# Solution to part 2
Find_lowest_integer(6)
