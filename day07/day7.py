
import statistics

from utils import readinput, to_ints

initial = to_ints(readinput().split(','))


def gauss(n):
    return (n * (n + 1)) / 2


def part1():
    median = int(statistics.median(initial))
    distances = 0
    for position in initial:
        distances += abs(position - median)
    print(distances)


def get_fuel_use(values, i):
    distances = 0
    for position in values:
        distance = abs(position - i)
        distances += gauss(distance)
    return int(distances)


def part2():
    # Ideas for improvement if speed was a factor:
    # * use binary search to find the best centroid (i)
    # * start in the middle of the range and work out from there

    print(min(get_fuel_use(initial, i) for i in range(min(initial), max(initial) + 1)))


part1()
part2()
