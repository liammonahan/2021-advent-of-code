from collections import defaultdict

from utils import readinput


lines = readinput()


# maps nodes to neighbors
G = defaultdict(set)
for line in lines:
    a, b = line.split('-')
    G[a].add(b)
    G[b].add(a)  # add both directions


def part1():
    visited = set()

    def explore(current, dest, count):
        visited.add(current)

        if current == dest:
            count += 1
        else:
            for neighbor in G[current]:
                if neighbor.isupper() or neighbor not in visited:
                    count = explore(neighbor, dest, count)

        if current in visited:
            visited.remove(current)

        return count

    return explore(current='start', dest='end', count=0)


def part2():
    visited = defaultdict(int)

    def lower2(_visited):
        has2 = 0
        for k, v in _visited.items():
            if k.islower() and v > 1:
                has2 += 1
        return has2

    def explore(current, dest, count):
        visited[current] += 1

        if current == dest:
            count += 1
        else:
            for neighbor in G[current]:
                if neighbor.isupper():
                    count = explore(neighbor, dest, count)
                elif visited[neighbor] == 0:
                    count = explore(neighbor, dest, count)
                elif neighbor not in ['start', 'end'] and lower2(visited) < 1:
                    count = explore(neighbor, dest, count)

        visited[current] -= 1

        return count

    return explore(current='start', dest='end', count=0)


print(part1())
print(part2())
