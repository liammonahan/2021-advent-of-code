
from utils import readinput

lines = readinput()
lines = [[int(o) for o in line] for line in lines]


def increase(octopuses):
    return [[o + 1 for o in line] for line in octopuses]


def increment_neighbor(matrix, flashed, i, j):
    if i < 0 or i > 9 or j < 0 or j > 9 or (i, j) in flashed:
        return
    matrix[i][j] += 1


def print_board(_input):
    for line in _input:
        print(''.join(str(i) for i in line))
    print()


def flash(lines):
    flashed = set()

    while True:
        any_flashed = False
        for i, line in enumerate(lines):
            for j, oct in enumerate(line):
                if oct > 9 and (i, j) not in flashed:
                    flashed.add((i, j))
                    any_flashed = True
                    lines[i][j] = 0  # reset

                    increment_neighbor(lines, flashed, i - 1, j)  # up
                    increment_neighbor(lines, flashed, i - 1, j + 1)  # up right
                    increment_neighbor(lines, flashed, i, j + 1)  # right
                    increment_neighbor(lines, flashed, i + 1, j + 1)  # down right
                    increment_neighbor(lines, flashed, i + 1, j)  # down
                    increment_neighbor(lines, flashed, i + 1, j - 1)  # down left
                    increment_neighbor(lines, flashed, i, j - 1)  # left
                    increment_neighbor(lines, flashed, i - 1, j - 1)  # left up

        if not any_flashed:
            return len(flashed)


def part1():
    octopuses = lines
    flashes = 0
    for step in range(1, 101):
        octopuses = increase(octopuses)
        flashes += flash(octopuses)

    return flashes


def part2():
    octopuses = lines
    for step in range(1, 500):
        octopuses = increase(octopuses)
        flashes = flash(octopuses)
        if flashes == 100:
            return step


print(part1())
print(part2())
