from collections import defaultdict

from utils import readinput


lines = readinput()


# maps nodes to neighbors
G = defaultdict(set)
for line in lines:
    a, b = line.split('-')
    G[a].add(b)
    G[b].add(a)  # add both directions


def lower2(_visited):
    has2 = 0
    for k, v in _visited.items():
        if k.islower() and v > 1:
            has2 += 1
    return has2


def explore(current, dest, count, visited, double_visit):
    visited[current] += 1
    if current == dest:
        count += 1
    else:
        for neighbor in G[current]:
            if neighbor.isupper() or visited[neighbor] == 0:
                count = explore(neighbor, dest, count, visited, double_visit)
            elif double_visit and neighbor not in ['start', 'end'] and lower2(visited) < 1:
                count = explore(neighbor, dest, count, visited, double_visit)
    visited[current] -= 1
    return count


def part1():
    visited = defaultdict(int)
    return explore(current='start', dest='end', count=0, visited=visited, double_visit=False)


def part2():
    visited = defaultdict(int)
    return explore(current='start', dest='end', count=0, visited=visited, double_visit=True)


print(part1())
print(part2())
