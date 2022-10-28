import sys

cells = [0]
pointer = 0
code = ''
code_pointer = 0


if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input('File name: ')

with open(filename) as f:
    for c in f.read():
        if c in ['<', '>', '+', '-', ',', '.', '[', ']']:
            code += c

def get_curr_command():
    return code[code_pointer]

while code_pointer < len(code):
    match get_curr_command():
        case '<':
            if pointer > 0: pointer -= 1
        case '>':
            pointer += 1
            if pointer == len(cells): cells.append(0)
        case '+':
            cells[pointer] += 1
            if cells[pointer] == 256: cells[pointer] = 0
        case '-':
            cells[pointer] -= 1
            if cells[pointer] == -1: cells[pointer] = 255
        case ',':
            cells[pointer] = ord(input(': '))
        case '.':
            print(chr(cells[pointer]), end='')
        
        case '[':
            if cells[pointer] == 0:
                unmatched_count = 1
                while unmatched_count > 0:
                    code_pointer += 1
                    if get_curr_command() == '[': unmatched_count += 1
                    if get_curr_command() == ']': unmatched_count -= 1
        case ']':
            if cells[pointer] != 0:
                unmatched_count = 1
                while unmatched_count > 0:
                    code_pointer -= 1
                    if get_curr_command() == ']': unmatched_count += 1
                    if get_curr_command() == '[': unmatched_count -= 1
        
    code_pointer += 1
