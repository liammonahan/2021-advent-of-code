
from utils import readgroups


coords, instructions = readgroups()
coords = [tuple(int(i) for i in c.split(',')) for c in coords]
instructions = [l.split(' ')[-1].split('=') for l in instructions]
folds = [tuple([a[0], int(a[1])]) for a in instructions]


def count_marks(grid):
    return len(grid)


def print_grid(grid):
    max_x = max(x for (x, y) in grid.keys())
    max_y = max(y for (x, y) in grid.keys())

    mystr = ''
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in grid:
                mystr += '#'
            else:
                mystr += ' '
        mystr += '\n'
    return mystr


def part1():
    grid = {}
    for x, y in coords:
        grid[(x, y)] = True

    for axis, fold in folds:
        new_grid = {}
        if axis == 'x':
            for (x, y) in grid:
                if x < fold:
                    new_grid[(x, y)] = True
                else:
                    diff = x - fold
                    new_grid[(fold - diff, y)] = True
        elif axis == 'y':
            for (x, y) in grid:
                if y > fold:
                    diff = y - fold
                    new_grid[(x, fold - diff)] = True
                else:
                    new_grid[(x, y)] = True
        grid = new_grid
        return count_marks(grid)


def part2():
    grid = {}
    for x, y in coords:
        grid[(x, y)] = True

    for axis, fold in folds:
        new_grid = {}
        if axis == 'x':
            for (x, y) in grid:
                if x > fold:
                    diff = x - fold
                    new_grid[(fold - diff, y)] = True
                else:
                    new_grid[(x, y)] = True
        elif axis == 'y':
            for (x, y) in grid:
                if y > fold:
                    diff = y - fold
                    new_grid[(x, fold - diff)] = True
                else:
                    new_grid[(x, y)] = True
        grid = new_grid

    return print_grid(grid)


print(part1())
print(part2())
