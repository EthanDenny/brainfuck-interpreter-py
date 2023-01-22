import sys


def execute(code: str):
    cells = [0]
    mem_ptr = 0
    code_ptr = 0

    while code_ptr < len(code):
        match code[code_ptr]:
            case '<':
                if mem_ptr > 0: mem_ptr -= 1
            case '>':
                mem_ptr += 1
                if mem_ptr == len(cells): cells.append(0)
            case '+':
                cells[mem_ptr] += 1
                if cells[mem_ptr] == 256: cells[mem_ptr] = 0
            case '-':
                cells[mem_ptr] -= 1
                if cells[mem_ptr] == -1: cells[mem_ptr] = 255
            case ',':
                cells[mem_ptr] = ord(input(': '))
            case '.':
                print(chr(cells[mem_ptr]), end='')
            
            case '[':
                if cells[mem_ptr] == 0:
                    unmatched_count = 1
                    while unmatched_count > 0:
                        code_ptr += 1
                        if code[code_ptr] == '[': unmatched_count += 1
                        if code[code_ptr] == ']': unmatched_count -= 1
            case ']':
                if cells[mem_ptr] != 0:
                    unmatched_count = 1
                    while unmatched_count > 0:
                        code_ptr -= 1
                        if code[code_ptr] == ']': unmatched_count += 1
                        if code[code_ptr] == '[': unmatched_count -= 1
            
        code_ptr += 1


def parse_file(filepath: str):
    code = ''

    with open(filepath) as f:
        for c in f.read():
            if c in {'<', '>', '+', '-', ',', '.', '[', ']'}:
                code += c
    
    execute(code)


def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = input('File name: ')
    
    parse_file(filepath)


if __name__ == '__main__':
    main()
