import statistics

from utils import readinput

lines = readinput()

MATCHES = {'(': ')', '[': ']', '{': '}', '<': '>'}


def part1():
    stack = []
    corrupted = []
    for line in lines:
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.insert(0, char)
            else:
                popped = stack.pop(0)
                if MATCHES.get(popped) != char:
                    corrupted.append(char)
                    break  # to next line

    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return sum(points.get(c) for c in corrupted)


def part2():
    completed = []
    for line in lines:
        stack = []
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.insert(0, char)
            else:
                popped = stack.pop(0)
                if MATCHES.get(popped) != char:
                    break  # to next line
        else:
            completed.append(MATCHES[c] for c in stack)

    points = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in completed:
        score = 0
        for char in line:
            score *= 5
            score += points[char]
        scores.append(score)

    return statistics.median(scores)


print(part1())
print(part2())
