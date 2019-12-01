def part1(mass: int) -> int:
    return mass // 3 - 2


def part2(mass: int) -> int:
    fuel = part1(mass)
    if fuel > 0:
        return fuel + part2(fuel)
    return 0


if __name__ == '__main__':
    with open('input.txt') as infile:
        sol_part_1, sol_part_2 = 0, 0

        for line in infile:
            line = int(line.strip())
            sol_part_1 += part1(line)
            sol_part_2 += part2(line)

        print(f'Part 1: {sol_part_1}')
        print(f'Part 2: {sol_part_2}')
