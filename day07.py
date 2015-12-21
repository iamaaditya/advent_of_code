in_str = open('./input_data/input7.txt').read().splitlines()


def extract_ops(input):
    """ extracts the operands and operators, for binary and unary operations """
    # returns left operand, right operand (none for unary), operator and result
    # returns left operant (value), none, operator (assign), result for assignment

    input_words = input.split(' ')

    if len(input_words) == 3:
        return input_words[0], None, "assign", input_words[2]
    
    elif input_words[0] == "NOT":
        # unary operator
        return input_words[1], None, input_words[0], input_words[3]
    else:
        return input_words[0], input_words[2], input_words[1], input_words[4]

dic_wire = {}
for input in in_str:
    opL, opR, op, res = extract_ops(input)
    dic_wire[ res ] = (opL, opR, op)


def recursive_solve(wire):
    global soln_memo
    # Memoization
    if wire in soln_memo:
        return soln_memo[wire]

    if wire.isdigit(): 
        ans =  int(wire)
        soln_memo[wire] = ans
        return ans

    opL, opR, op = dic_wire[wire]

    if op == "assign":
        # base case, it is assigned numeric value
        if opL.isdigit():
            ans = int(opL)
            soln_memo[wire] = ans
            return ans
        ans = recursive_solve(opL)
        soln_memo[wire] = ans
        return ans

    elif op == "NOT":
        ans =  ~ recursive_solve(opL)
        soln_memo[wire] = ans
        return ans


    elif op == "AND":
        ans =  recursive_solve(opL) & recursive_solve(opR)
        soln_memo[wire] = ans
        return ans

    elif op == "OR":
        ans =  recursive_solve(opL) | recursive_solve(opR)
        soln_memo[wire] = ans
        return ans

    elif op == "LSHIFT":
        ans =  recursive_solve(opL) << int(opR)
        soln_memo[wire] = ans
        return ans

    elif op == "RSHIFT":
        ans =  recursive_solve(opL) >> int(opR)
        soln_memo[wire] = ans
        return ans

    else:
        print "ERROR"
        return 
# Part 1
soln_memo = {}
print recursive_solve('a') 

# Part 2
soln_memo = {}
dic_wire['b'] = ('956', None, 'assign')
print recursive_solve('a') 
