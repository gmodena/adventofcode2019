from typing import List, Tuple, Optional
from copy import copy
from operator import add, mul

TARGET = 19_690_720
OFFSET = 4

opcodes = {1: add, 2: mul, 99: 'halt'}


def part1(program: List[int], noun=12, verb=2) -> List[int]:
    pos = 0
    program[1] = noun
    program[2] = verb
    while pos < len(program):
        op = program[pos]
        if op in opcodes:
            if opcodes[op] == 'halt':
                break
            l = program[pos+1]
            r = program[pos+2]
            dst = program[pos+3]
            program[dst] = opcodes[op](program[l],  program[r])
            pos += OFFSET
        else:
            pos += 1
    return program


def part2(program: List[int], target: Optional[int] = None) -> Optional[Tuple[int, int]]:
    if not target:
        return
    for i in range(100):
        for j in range(100):
            if part1(copy(program), noun=i, verb=j)[0] == target:
                return i, j


if __name__ == '__main__':
    with open('input.txt') as infile:
        program = list(map(int, infile.read().strip().split(',')))
        print(part1(copy(program))[0])

        noun, verb = part2(copy(program), target=TARGET)
        print(100 * noun + verb)




