cells = [0]
pointer = 0
code = ''
code_pointer = 0

file_name = input('File name: ')
with open(file_name) as f:
    for c in f.read():
        if c in ['<', '>', '+', '-', ',', '.', '[', ']']:
            code += c

while code_pointer < len(code) and (c := code[code_pointer]):
    if c == '<' and pointer > 0:
        pointer -= 1
    if c == '>':
        pointer += 1
        if pointer == len(cells): cells.append(0)
    if c == '+':
        cells[pointer] += 1
        if cells[pointer] == 256: cells[pointer] = 0
    if c == '-':
        cells[pointer] -= 1
        if cells[pointer] == -1: cells[pointer] = 255
    if c == ',':
        cells[pointer] = ord(input(': '))
    if c == '.':
        print(chr(cells[pointer]))
    
    if c == '[' and cells[pointer] == 0:
        unmatched_count = 1
        while unmatched_count > 0:
            code_pointer += 1
            if code[code_pointer] == '[': unmatched_count += 1
            if code[code_pointer] == ']': unmatched_count -= 1
    if c == ']' and cells[pointer] != 0:
        unmatched_count = 1
        while unmatched_count > 0:
            code_pointer -= 1
            if code[code_pointer] == ']': unmatched_count += 1
            if code[code_pointer] == '[': unmatched_count -= 1
    
    code_pointer += 1
