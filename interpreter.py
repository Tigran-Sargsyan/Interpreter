import sys

file_name = sys.argv[1]

with open(file_name) as mp:
    program = mp.readlines()

commands = ["varbl", "write", "if", "end", "calc", "check", "\n"]
stack = {}          # For holding simple variables
signs = ["+", "-", "*", "/", "**"]  # For arithmetic operations
cmp_signs = [">", "<", "=", "!=", "&", "|", "!"]  # For comparisons
reserved = ["write", "calc", "varbl", "TRUE", "FALSE", "begin cond", "end cond", "begin loop", "end loop"]
# Reserved words that cannot be used as a variable name

"""A Function to make simple arithmetic operations"""
def calc(*args):
    op1 = args[0]
    op2 = args[2]
    sign = args[1]
    if sign == "+":
        print(op1 + op2)
        return op1 + op2
    elif sign == "-":
        print(op1 - op2)
        return op1 - op2
    elif sign == "*":
        print(op1 * op2)
        return op1 * op2
    elif sign == "/":
        print(op1 / op2)
        return op1 / op2
    elif sign == "**":
        print(op1 ** op2)
        return op1 ** op2

"""A function for declaring variables and storing them in the stack"""
def var_declaring(lst):
    name = lst[1]
#    print(name)
    assert not name[0].isnumeric()   # A variable cannot start with a number
    assert name not in reserved
    assert lst[2] == "->"
    value = lst[3]
#    print(value)
    try:
        float(value)
    except:
        if len(lst) > 4:
            if lst[-1] == ' "':
                lst[-2] += lst[-1]

            else:
                if lst[3][0] == '"':
                    for i in range(4, len(lst)):
                        if "{" in lst[i] and "}" in lst[i]:
                            var = lst[i].strip()[1:-1]
                            if var in stack:
                                lst[i] = stack[var]
#                                print(lst)
                                value += ' ' + lst[i]
                        else:
                            value += ' ' + lst[i]
                            # print(value)
                    stack[name] = value[1:-1]
                else:
                    if lst[3] in stack.keys() and lst[5] in stack.keys():
                        res = calc(float(stack[lst[3]]), lst[4], float(stack[lst[5]]))
                        stack[name] = res
                    elif lst[3] in stack.keys() and lst[5] not in stack.keys():
                        res = calc(float(stack[lst[3]]), lst[4], float(lst[5]))
                        stack[name] = res
                    elif lst[3] not in stack.keys() and lst[5] in stack.keys():
                        res = calc(float(lst[3]), lst[4], float(stack[lst[5]]))
                        stack[name] = res

        else:
            if value == "TRUE" or value == "FALSE":
                stack[name] = value
            elif value in stack.keys():
                stack[name] = stack[value]
            else:
                stack[name] = value[1:-1]
    else:
        if len(lst) == 4:
            stack[name] = float(value)
        else:
            if lst[4] in signs:
                try:
                    float(lst[3]) and float(lst[5]) and lst[4] in signs
                except:
                    if lst[5] in stack.keys():
                        res = calc(float(lst[3]), lst[4], float(stack[lst[5]]))
                        stack[name] = res
                    else:
                        print("Error!")
                else:
                    res = calc(float(lst[3]), lst[4], float(lst[5]))
                    stack[name] = res

"""A Function for comparisons"""
def check(condition):
    cmp_lst = condition.split()
#    print(cmp_lst)
    assert cmp_lst[1] in cmp_signs
    if cmp_lst[0] not in stack.keys() and cmp_lst[2] not in stack.keys():
        try:
            float(cmp_lst[0]) and float(cmp_lst[2])
        except:
            if cmp_lst[0][0] == '"' and cmp_lst[0][-1] == '"' and cmp_lst[2][0] == '"' and cmp_lst[2][-1] == '"':
                if cmp_lst[1] == ">":
                    if cmp_lst[0] > cmp_lst[2]:
                        return True
                    else:
                        return False
                elif cmp_lst[1] == "<":
                    if cmp_lst[0] < cmp_lst[2]:
                        return True
                    else:
                        return False
                elif cmp_lst[1] == "==":
                    if cmp_lst[0] == cmp_lst[2]:
                        return True
                    else:
                        return False
                elif cmp_lst[1] == "!=":
                    if cmp_lst[0] != cmp_lst[2]:
                        return True
                    else:
                        return False
            else:
                print("Error,can't compare the values")
        else:
            if(cmp_lst[1]) == ">":
                if float(cmp_lst[0]) > float(cmp_lst[2]):
                    return True
                else:
                    return False
            elif(cmp_lst[1]) == "<":
                if float(cmp_lst[0]) < float(cmp_lst[2]):
                    return True
                else:
                    return False
            elif(cmp_lst[1]) == "==":
                if float(cmp_lst[0]) == float(cmp_lst[2]):
                    return True
                else:
                    return False
            elif cmp_lst[1] == "!=":
                if float(cmp_lst[0]) != float(cmp_lst[2]):
                    return True
                else:
                    return False

    elif cmp_lst[0] in stack.keys():
        if cmp_lst[2] in stack.keys():
            if cmp_lst[1] == ">":
                if stack[cmp_lst[0]] > stack[cmp_lst[2]]:
                    return True
                else:
                    return False
            elif cmp_lst[1] == "<":
                if stack[cmp_lst[0]] < stack[cmp_lst[2]]:
                    return True
                else:
                    return False
            elif cmp_lst[1] == "==":
                if stack[cmp_lst[0]] == stack[cmp_lst[2]]:
                    return True
                else:
                    return False
            elif cmp_lst[1] == "!=":
                if stack[cmp_lst[0]] != stack[cmp_lst[2]]:
                    return True
                else:
                    return False

        else:
            try:
                float(cmp_lst[2])
            except:
                if cmp_lst[1] == ">":
                    if stack[cmp_lst[0]] > cmp_lst[2]:
                        return True
                    else:
                        return False
                elif cmp_lst[1] == "<":
                    if stack[cmp_lst[0]] < cmp_lst[2]:
                        return True
                    else:
                        return False
                elif cmp_lst[1] == "==":
                    if stack[cmp_lst[0]] == cmp_lst[2]:
                        return True
                    else:
                        return False
                elif cmp_lst[1] == "!=":
                    if stack[cmp_lst[0]] != cmp_lst[2]:
                        return True
                    else:
                        return False
            else:
                if cmp_lst[1] == ">":
                    if stack[cmp_lst[0]] > float(cmp_lst[2]):
                        return True
                    else:
                        return False
                elif cmp_lst[1] == "<":
                    if stack[cmp_lst[0]] < float(cmp_lst[2]):
                        return True
                    else:
                        return False
                elif cmp_lst[1] == "==":
                    if stack[cmp_lst[0]] == float(cmp_lst[2]):
                        return True
                    else:
                        return False
                elif cmp_lst[1] == "!=":
                    if stack[cmp_lst[0]] != float(cmp_lst[2]):
                        return True
                    else:
                        return False
    else:
        try:
            float(cmp_lst[0])
        except:
            if cmp_lst[1] == ">":
                if cmp_lst[0] > stack[cmp_lst[2]]:
                    return True
                else:
                    return False
            elif cmp_lst[1] == "<":
                if cmp_lst[0] < stack[cmp_lst[2]]:
                    return True
                else:
                    return False
            elif cmp_lst[1] == "==":
                if cmp_lst[0] == stack[cmp_lst[2]]:
                    return True
                else:
                    return False
            elif cmp_lst[1] == "!=":
                if cmp_lst[0] != stack[cmp_lst[2]]:
                    return True
                else:
                    return False

        else:
            if cmp_lst[1] == ">":
                if float(cmp_lst[0]) > stack[cmp_lst[2]]:
                    return True
                else:
                    return False
            elif cmp_lst[1] == "<":
                if float(cmp_lst[0]) < stack[cmp_lst[2]]:
                    return True
                else:
                    return False
            elif cmp_lst[1] == "==":
                if float(cmp_lst[0]) == stack[cmp_lst[2]]:
                    return True
                else:
                    return False
            elif cmp_lst[1] == "!=":
                if float(cmp_lst[0]) != stack[cmp_lst[2]]:
                    return True
                else:
                    return False

"""A Function for conditionals"""
def conditional(start, end):
    cond_block = program[start:end]
#   print(cond_block)
    cond_block[0] = cond_block[0].strip()
#   print(cond_block[0])
    if cond_block[0][0:2] == "if" and cond_block[0][3] == "(" and cond_block[0][-3] == ")" and cond_block[0][-1] == "[":
        cond_start_index = cond_block[0].index("(") + 1
        cond_end_index = cond_block[0].index(")")
        condd = cond_block[0][cond_start_index:cond_end_index]
        if check(condd):
            for k in range(start, end+1):
                del program[start-1]
#               print(program)
#           print(cond_block)
            loop_end = cond_block.index("]\n")
            for j in cond_block[1:loop_end]:
                main(j)
        else:
#           print(cond_block.index("]\n")+1)
            for k in range(start, start+cond_block.index("]\n")+1):
                del program[start]
#               print(program)
            main(program[start-1])
    elif cond_block[0][0:4] == "elif" and cond_block[0][5] == "(" and cond_block[0][-3] == ")" and cond_block[0][-1]=="[":
        cond_start_index = cond_block[0].index("(") + 1
        cond_end_index = cond_block[0].index(")")
        condd = cond_block[0][cond_start_index:cond_end_index]
#       print(cond_block)
        if check(condd):
            for k in range(start, end+1):
                del program[start-1]
#               print(program)
            loop_end = cond_block.index("]\n")
            for j in cond_block[1:loop_end]:
                main(j)
        else:
#           print(cond_block.index("]\n")+1)
            for k in range(start, start+cond_block.index("]\n")+1):
                del program[start]
#               print(program)
            main(program[start-1])
    elif cond_block[0][0:4] == "else" and cond_block[0][-1]=="[":
        for k in range(start, end + 1):
            del program[start - 1]
#           print(program)
        loop_end = cond_block.index("]\n")
        for j in cond_block[1:loop_end]:
            main(j)

"""A Function that makes an output"""
def write(raw, text=''):
    assert raw[0] == '"' and raw[-1] == '"'

    plain_txt = raw[1:-1].split()
    for i in plain_txt:
        if "{" not in i or "}" not in i:
            text += ' ' + i
        else:
            assert i[1:-1] in stack
            current = stack[i[1:-1]]
            if(type(current)) == "str":
                text += ' ' + current
            else:
                text += ' ' + f"{current}"
    print(text)

"""A Function for handling loops"""
def loop(start_l, end_l):
#   print(start_l, end_l)
#   print(program[start_l:end_l])
    loop_block = program[start_l:end_l]
    loop_cond_body = loop_block[0]
    loop_lst = loop_cond_body.split()
    varr = loop_lst[0]
#   print(loop_lst)
    assert varr in stack
    assert loop_lst[1] == varr and loop_lst[4] == varr
    assert loop_lst[5] in signs

    cond1 = varr + ' ' + loop_lst[2] + ' ' + loop_lst[3]
#   print(cond1)
    if loop_lst[6] not in stack:
        cond1_res = check(cond1)
        if cond1_res:
            block_size = end_l - start_l - 2
            for i in range(block_size):
                main(loop_block[i])
            stack[varr] += float(loop_lst[6])
            main(program[start_l - 1])
        else:
            for l in range(start_l - 1, end_l):
                del program[start_l - 1]
    else:
        cond1_res = check(cond1)
        if cond1_res:
            block_size = end_l - start_l - 2
            for i in range(block_size):
                main(loop_block[i])
            stack[varr] += stack[loop_lst[6]]
            main(program[start_l - 1])
        else:
            for l in range(start_l - 1, end_l):
                del program[start_l - 1]

def main(line):
    # print(main_pr)
    lst = line.split()
    # print(lst)
    if lst:

        if lst[0] == "varbl":
            var_declaring(lst)

        elif lst[0][:5] == "write":
            raw = line[6:].strip()
            write(raw)

        elif lst[0] == "calc":
            if lst[1] in stack.keys() and lst[3] in stack.keys():
                calc(float(stack[lst[1]]), lst[2], float(stack[lst[3]]))
            elif lst[1] in stack.keys() and lst[3] not in stack.keys():
                calc(float(stack[lst[1]]), lst[2], float(lst[3]))
            elif lst[1] not in stack.keys() and lst[3] in stack.keys():
                calc(float(lst[1]), lst[2], float(stack[lst[3]]))
            else:
                calc(float(lst[1]), lst[2], float(lst[3]))

        elif lst[0] == "begin" and lst[1] == "cond":
            start = program.index("begin cond\n") + 1
#           print(start)
            end = program.index("end cond\n") + 1
#           print(end)
#           print(program)
            conditional(start, end)

        elif lst[0] == "begin" and lst[1] == "loop":
            start_l = program.index("begin loop\n") + 1
            end_l = program.index("end loop\n") + 1
            loop(start_l, end_l)

        elif lst[0][:2] == "**":
            pass

for line in program:
    main(line)

# for key, value in stack.items():  # Printing the variable/value table
#    print(key, ":", value)
