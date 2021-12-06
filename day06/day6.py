
from utils import *
from collections import defaultdict

_initial = to_ints(readinput().split(','))
initial = defaultdict(int)
for ttl in _initial:
    initial[ttl] += 1


def advance(state):
    new = defaultdict(int)

    # spawn the 0s
    new[8] = state[0]
    new[6] = state[0]

    # tick down the 1 - 8s
    for i in range(1, 9):
        new[i-1] += state[i]

    return new


def part1():
    state = initial.copy()
    for day in range(80):
        state = advance(state)
    print(sum(state.values()))


def part2():
    state = initial.copy()
    for day in range(256):
        state = advance(state)
    print(sum(state.values()))


part1()
part2()