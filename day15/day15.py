
from utils import readinput

lines = readinput()
_grid = [[int(o) for o in line] for line in lines]

grid1 = {}
n = len(_grid)
m = len(_grid[0])
for i in range(n):
    for j in range(m):
        grid1[(i, j)] = _grid[i][j]


grid2 = {}
for x in range(5):
    for y in range(5):
        for i in range(n):
            for j in range(m):
                value = (_grid[i][j] + x + y)
                if value > 9:
                    value %= 9

                ii = (n * x) + i
                jj = (m * y) + j
                grid2[(ii, jj)] = value


def get_neighbors(v, max_i, max_j, grid):
    i, j = v
    neighbors = []
    if i > 0:
        neighbors.append(((i - 1, j), grid[(i - 1, j)]))
    if j > 0:
        neighbors.append(((i, j - 1), grid[(i, j - 1)]))
    if i < max_i:
        neighbors.append(((i + 1, j), grid[(i + 1, j)]))
    if j < max_j:
        neighbors.append(((i, j + 1), grid[(i, j + 1)]))
    return neighbors


def a_star(start, stop, grid):
    max_i = stop[0]
    max_j = stop[1]

    open_set = set([start])
    closed_set = set()
    costs = {start: 0}
    parents = {start: start}

    while open_set:
        curr = None

        for v in open_set:
            if curr is None or costs[v] + grid[v] < costs[curr] + grid[curr]:
                curr = v

        if curr == stop:
            # found a path.  trace it back to the beginning
            path = []
            while parents[curr] != curr:
                path.append(curr)
                curr = parents[curr]

            # don't append start because we don't count its cost anyway
            return path

        for (neighbor, weight) in get_neighbors(curr, max_i, max_j, grid):
            if neighbor not in open_set and neighbor not in closed_set:
                open_set.add(neighbor)
                parents[neighbor] = curr
                costs[neighbor] = costs[curr] + weight
            else:
                # check for updated cost
                if costs[neighbor] > costs[curr] + weight:
                    costs[neighbor] = costs[curr] + weight
                    parents[neighbor] = curr

                    if neighbor in closed_set:
                        closed_set.remove(neighbor)
                        open_set.add(neighbor)

        open_set.remove(curr)
        closed_set.add(curr)


def get_score(path, grid):
    return sum(grid[v] for v in path)


def part1():
    grid = grid1
    max_i = len(_grid) - 1
    max_j = len(_grid[0]) - 1
    path = a_star((0, 0), (max_i, max_j), grid)
    return get_score(path, grid)


def part2():
    grid = grid2
    max_i = len(_grid) * 5 - 1
    max_j = len(_grid[0]) * 5 - 1

    path = a_star((0, 0), (max_i, max_j), grid)
    return get_score(path, grid)


print(part1())
print(part2())
