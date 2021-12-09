
from utils import readinput

lines = readinput()
lines = [[int(i) for i in line] for line in lines]

num_rows = len(lines)
num_cols = len(lines[0])


def get_adjacent(i, j):
    # top, bottom, left, right
    positions = []
    if i > 0:
        positions.append(lines[i - 1][j])
    if i < num_rows - 1:
        positions.append(lines[i + 1][j])
    if j > 0:
        positions.append(lines[i][j - 1])
    if j < num_cols - 1:
        positions.append(lines[i][j + 1])
    return positions


def part1():
    low = []
    for i, row in enumerate(lines):
        for j, cell in enumerate(row):
            if all(cell < adj for adj in get_adjacent(i, j)):
                low.append(cell)
    return sum(i + 1 for i in low)


def points_above(i, j, found):
    points = []
    n = 1
    above = None
    while above != 9 and (i - n) >= 0:
        above = lines[i - n][j]
        if above != 9:
            if (i - n, j) not in found:
                points.append(above)
                found.add((i - n, j))
                points.extend(points_left(i - n, j, found))
                points.extend(points_right(i - n, j, found))
        n += 1
    return points


def points_below(i, j, found):
    points = []
    n = 1
    below = None
    while below != 9 and (i + n) < num_rows:  # TODO fencepost
        below = lines[i + n][j]
        if below != 9:
            if (i + n, j) not in found:
                points.append(below)
                found.add((i + n, j))
                points.extend(points_left(i + n, j, found))
                points.extend(points_right(i + n, j, found))
        n += 1
    return points


def points_left(i, j, found):
    points = []
    n = 1
    left = None
    while left != 9 and (j - n) >= 0:
        left = lines[i][j - n]
        if left != 9:
            if (i, j - n) not in found:
                points.append(left)
                found.add((i, j - n))
                points.extend(points_above(i, j - n, found))  # call above and below for [i][j - n]
                points.extend(points_below(i, j - n, found))
        n += 1
    return points


def points_right(i, j, found):
    points = []
    n = 1
    right = None
    while right != 9 and (j + n) < num_cols:
        right = lines[i][j + n]
        if right != 9:
            if (i, j + n) not in found:
                points.append(right)
                found.add((i, j + n))
                points.extend(points_above(i, j + n, found))  # call above and below for [i][j - n]
                points.extend(points_below(i, j + n, found))
        n += 1
    return points


def get_basin(i, j):
    # branch out from the center
    # find the 4 corners of the tee
    # iterate through positions to left/right and top/bottom of each tee

    found = set()

    points_left(i, j, found)
    points_right(i, j, found)
    points_above(i, j, found)
    points_below(i, j, found)

    return [lines[i][j] for i, j in found]


def part2():
    # use the low points to find basins
    low_points = []
    for i, row in enumerate(lines):
        for j, cell in enumerate(row):
            if all(cell < adj for adj in get_adjacent(i, j)):
                low_points.append((i, j))

    basins = [get_basin(*point) for point in low_points]
    basins.sort(key=lambda b: len(b))
    basins = basins[-3:]  # largest 3 basins once sorted
    print(len(basins[0]) * len(basins[1]) * len(basins[2]))


print(part1())
print(part2())
