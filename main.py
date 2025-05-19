import numpy as np
import re

fallout = 0  # $
stored = 0   # %
grid = None
input_p = 0
stored_in = "" # Change this
program = ";[.;]" # and this
pc = 0
code_list = []
callstack = []
width = 0
height = 0

def resolve_row(row):
    global height
    return row % height

def resolve_col(col):
    global width
    return col % width

def resolve(arg):
    global fallout, stored
    if arg == "$":
        return int(fallout)
    elif arg == "%":
        return int(stored)
    else:
        return int(arg)

def shift_up(matrix, col_index, insert=0):
    global fallout
    col_index = resolve_col(col_index)
    fallen = matrix[0, col_index]
    matrix[:-1, col_index] = matrix[1:, col_index]
    fallout = fallen
    insert = resolve(insert)
    matrix[-1, col_index] = insert
    return matrix

def shift_down(matrix, col_index, insert=0):
    global fallout
    col_index = resolve_col(col_index)
    fallen = matrix[-1, col_index]
    matrix[1:, col_index] = matrix[:-1, col_index]
    fallout = fallen
    insert = resolve(insert)
    matrix[0, col_index] = insert
    return matrix

def shift_left(matrix, row_index, insert=0):
    global fallout
    row_index = resolve_row(row_index)
    fallen = matrix[row_index, 0]
    matrix[row_index, :-1] = matrix[row_index, 1:]
    fallout = fallen
    insert = resolve(insert)
    matrix[row_index, -1] = insert
    return matrix

def shift_right(matrix, row_index, insert=0):
    global fallout
    row_index = resolve_row(row_index)
    fallen = matrix[row_index, -1]
    matrix[row_index, 1:] = matrix[row_index, :-1]
    fallout = fallen
    insert = resolve(insert)
    matrix[row_index, 0] = insert
    return matrix

def extract_width_and_height(text):
    re_match = re.search(r'\b([1-9]\d*)x([1-9]\d*)\b', text)
    if re_match:
        width = int(re_match.group(1))
        height = int(re_match.group(2))
        return width, height
    else:
        return 16, 16

def interpret_command(command):
    global grid, fallout, stored, stored_in, input_p, pc, code_list

    match command[0]:
        case "+":
            fallout += 1
        case "-":
            fallout -= 1
        case "#":
            stored = fallout
        case "@":
            fallout = stored
        case ".":
            print(chr(int(fallout) % 256), end="", flush=True)
        case ";":
            if input_p < len(stored_in):
                fallout = ord(stored_in[input_p])
                input_p += 1
            else:
                fallout = 0

        case "!":
            fallout = fallout % 256
        case "[":
            if fallout != 0:
                callstack.append(pc)
                return
            level = 1

            while True:
                pc += 1

                if pc == len(code_list):
                    print("Mismatched loop: no ] for [")
                    quit(1)
                                
                match code_list[pc]:
                    case "[":
                        level += 1
                    case "]":
                        level -= 1
                        if level == 0:
                            break

        case "]":
            if not callstack:
                print("Mismatched loop: no [ for ]")
                quit(1)
            if fallout != 0:
                pc = callstack[-1]
                return
            callstack.pop()

        case ">":
            command = command[1:]
            first, last = command.split(',', 1)
            shift_right(grid, resolve(first), last)
        case "<":
            command = command[1:]
            first, last = command.split(',', 1)
            shift_left(grid, resolve(first), last)
        case "^":
            command = command[1:]
            first, last = command.split(',', 1)
            shift_up(grid, resolve(first), last)
        case "v":
            command = command[1:]
            first, last = command.split(',', 1)
            shift_down(grid, resolve(first), last)

def interpret(code):
    global grid, pc, code_list, callstack, width, height

    callstack = []
    pc = 0
    command_pattern = r'[><\^v](?:\d+|\$|%),(?:\d+|\$|%)|[+\-#@.;\[\]!]'
    width, height = extract_width_and_height(code)
    grid = np.zeros((height, width))
    code = re.sub(r'\s', '', code).lower()
    code_list = re.findall(command_pattern, code)
    while pc < len(code_list):
        interpret_command(code_list[pc])
        pc += 1

interpret(program)
