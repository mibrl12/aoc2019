
def run_intcode(intcode_str: str) -> str:
    opcodes = [int(opcode) for opcode in intcode_str.split(',')]

    i = 0
    while i < len(opcodes):
        if opcodes[i] == 99:
            break
        if opcodes[i] == 1:
            opcodes[opcodes[i + 3]] = opcodes[opcodes[i + 1]] + opcodes[opcodes[i + 2]]
        elif opcodes[i] == 2:
            opcodes[opcodes[i + 3]] = opcodes[opcodes[i + 1]] * opcodes[opcodes[i + 2]]
        i += 4

    return ','.join(map(str, opcodes))


with open('input.txt') as f:
    print(f'Day 02. Part 1: \n{run_intcode(f.readline())}')
