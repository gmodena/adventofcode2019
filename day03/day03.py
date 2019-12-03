def wire(path):
    coords = {}
    cur_x, cur_y = 0, 0
    steps = 0
    for move in path.split(','):
        direction = move[0]
        magnitude = int(move[1:])
        for _ in range(magnitude):
            if direction == 'D':
                cur_y -= 1
            elif direction == 'U':
                cur_y += 1
            elif direction == 'R':
                cur_x +=1
            elif direction == 'L':
                cur_x -= 1
            steps += 1
            coords[(cur_x, cur_y)] = steps
    return coords

if __name__ == '__main__':
    with open('input.txt') as infile:
        paths = infile.readlines()

    A = wire(paths[0].strip())
    B = wire(paths[1].strip())

    print(min([abs(x) + abs(y) for x, y in set(A.keys()).intersection(set(B.keys()))]))
    print(min([A[x] + B[x] for x in set(A.keys()).intersection(set(B.keys()))]))