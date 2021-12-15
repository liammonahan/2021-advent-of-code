
import math
import collections

from utils import readgroups

polymer_template, insertion_rules = readgroups()
polymer_template = polymer_template[0]
_insertion_rules = [rule.split(' -> ') for rule in insertion_rules]
insertion_rules = {a: b for a, b in _insertion_rules}


def part1():
    current = polymer_template
    for step in range(1, 11):
        new = current
        offset = 0
        for i in range(len(new) - 1):
            segment = current[i:i+2]
            if segment in insertion_rules:
                new = new[:i+1+offset] + insertion_rules[segment] + new[i+1+offset:]
                offset += 1
        current = new

    appearances = collections.Counter(current)
    most_common = appearances.most_common()[0]
    least_common = appearances.most_common()[-1]
    return most_common[1] - least_common[1]


def part2():
    current = collections.defaultdict(int)
    for i in range(len(polymer_template) - 1):
        segment = polymer_template[i:i + 2]
        current[segment] += 1

    for step in range(1, 41):
        new = current.copy()

        for pair, count in current.items():
            if pair in insertion_rules:
                new[pair] -= count
                a = pair[0] + insertion_rules[pair]
                b = insertion_rules[pair] + pair[1]
                new[a] += count
                new[b] += count

        current = new

    # just in case.  not really necessary for these inputs
    current = {a: b for a, b in current.items() if b != 0}

    final = collections.defaultdict(int)
    for key, count in current.items():
        final[key[0]] += count
        final[key[1]] += count

    appearances = collections.Counter(final)
    most_common = appearances.most_common()[0]
    least_common = appearances.most_common()[-1]

    return math.ceil((most_common[1] - least_common[1]) / 2)


print(part1())
print(part2())
