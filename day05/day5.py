
from collections import defaultdict

lines = [line.strip() for line in open('input.txt', 'r')]
initial = defaultdict(lambda: defaultdict(int))


# for debugging
def print_field(field):
    for x in range(1, 4):
        for y in range(1, 4):
            val = field[x][y]
            if val == 0:
                print('.', end='')
            else:
                print(val, end='')
        print()


def score(field):
    overlapping = 0
    for x, ydir in field.items():
        for y, count in ydir.items():
            if count >= 2:
                overlapping += 1
    print(overlapping)


def dopart(part2=False):
    field = initial.copy()
    for line in lines:
        start, end = line.split(' -> ')
        x1, y1 = [int(x) for x in start.split(',')]
        x2, y2 = [int(x) for x in end.split(',')]

        if x1 == x2:
            smally, bigy = sorted([y1, y2])
            for y in range(smally, bigy + 1):
                field[x1][y] += 1
        elif y1 == y2:
            smallx, bigx = sorted([x1, x2])
            for x in range(smallx, bigx + 1):
                field[x][y1] += 1
        elif part2:
            # diagonal
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1

            for i in range(abs(x1 - x2) + 1):
                field[x1 + dx * i][y1 + dy * i] += 1

    score(field)


dopart()
dopart(part2=True)
