from typing import List


def run_intcode(intcode_str: str, first=12, second=2) -> List[int]:
    opcodes = [int(opcode) for opcode in intcode_str.split(',')]

    opcodes[1] = first
    opcodes[2] = second

    i = 0
    while i < len(opcodes):
        if opcodes[i] == 99:
            break
        if opcodes[i] == 1:
            opcodes[opcodes[i + 3]] = opcodes[opcodes[i + 1]] + opcodes[opcodes[i + 2]]
        elif opcodes[i] == 2:
            opcodes[opcodes[i + 3]] = opcodes[opcodes[i + 1]] * opcodes[opcodes[i + 2]]
        i += 4

    return opcodes


def find_target_pair(intcode_str: str, target_output: int):
    for noun in range(100):
        for verb in range(100):
            output = run_intcode(intcode_str, noun, verb)
            if output[0] == target_output:
                return noun, verb


with open('input.txt') as f:
    intcode_str = f.readline()
    day_1_solution = ",".join(map(str, run_intcode(intcode_str)))
    print(f'Day 02. Part 1: \n{day_1_solution}')
    target_pair = find_target_pair(intcode_str, target_output=19690720)
    day_2_solution = 100 * target_pair[0] + target_pair[1]
    print(f'Day 02. Part 2: \n{day_2_solution}')
