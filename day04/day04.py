if __name__ == '__main__':
    part1, part2 = 0, 0
    for n in range(307237, 769058+1):
        n = str(n)
        is_increasing = list(n) == sorted(n)
        counts = map(n.count, n)
        if is_increasing and any(map(lambda x: x > 1, counts)):
            part1 += 1
        if is_increasing and 2 in counts:
            part2 += 1
    print(part1)
    print(part2)
