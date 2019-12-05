from typing import List
from copy import copy
from operator import add, mul
import math


opcodes = {1: add,
           2: mul,
           3: 'input',
           4: 'output',
           5: 'jit',
           6: 'jif',
           7: lambda x, y: 1 if x < y else 0,
           8: lambda x, y: 1 if x == y else 0,
           99: 'halt'}


def int_len(n: int) -> int:
    return int(math.log10(max(1, n)))+1


def part1(program: List[int], inp=1) -> List[int]:
    pos = 0
    while pos < len(program):
        op = program[pos]
        modes = [0, 0, 0]

        op_len = int_len(op)
        if op_len > 2:
            modes = [op // (10 ** i) % 10 for i in range(2, 5)]
            op %= 100

        try:
            param1 = program[pos+1] if modes[0] == 0 else pos+1
            param2 = program[pos+2] if modes[1] == 0 else pos+2
            param3 = program[pos+3] if modes[2] == 0 else pos+3
        except IndexError:
            print("error", modes, pos, len(program))

        if opcodes[op] == 'halt':
            break
        elif opcodes[op] == 'input':
            program[param1] = inp
            pos += 2
        elif opcodes[op] == 'output':
            print(program[param1])
            pos += 2
        elif opcodes[op] == 'jit':
            pos = program[param2] if program[param1] != 0 else pos+3
        elif opcodes[op] == 'jif':
            pos = program[param2] if program[param1] == 0 else pos+3
        else:
            program[param3] = opcodes[op](program[param1], program[param2])
            pos += 4
    return program


if __name__ == '__main__':
    with open('input.txt') as infile:
        program = list(map(int, infile.read().strip().split(',')))

        part1(copy(program), inp=1)
        part1(copy(program), inp=5)
