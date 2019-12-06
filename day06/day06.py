from collections import defaultdict


def part1(graph=None):
    orbits = {}

    def count_orbits(src):
        if src not in orbits:
            orbits[src] = sum(1 + count_orbits(dst) for dst in graph.get(src, ""))
        return orbits[src]
    return sum((count_orbits(src) for src in graph))


def part2(graph=None):
    def find_path(graph = None, src=None, dst=None):
        path = set()
        cur = src
        while True:
            _next = graph[cur]
            path.add(_next)
            if _next == dst:
                break
            cur = _next
        return path

    you_to_com = find_path(graph, 'YOU', 'COM')
    san_to_com = find_path(graph, 'SAN', 'COM')

    delta_you_to_san = len(set(you_to_com).difference(set(san_to_com)))
    delta_san_to_you = len(set(san_to_com).difference(set(you_to_com)))
    return delta_you_to_san + delta_san_to_you


with open('input.txt') as infile:
    graph = defaultdict(set)
    for line in infile.readlines():
        line = line.strip()
        dst, src = line.split(')')

        graph[dst].add(src)
    print(part1(graph))

with open('input.txt') as infile:
    graph = {}
    for line in infile.readlines():
        line = line.strip()
        dst, src = line.split(')')

        graph[src] = dst

    print(part2(graph))


