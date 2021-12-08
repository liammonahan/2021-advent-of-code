
from utils import readinput

lines = readinput()
lines = [line.split(' | ') for line in lines]
lines = [(i.split(), o.split()) for i, o in lines]


DIGIT_MAP = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}


def deduce_mapping(inputs, outputs):
    # These hold if we know the wiring mapping for sure
    deduced = {c: None for c in 'abcdefg'}

    # every wiring possibility is open until we start deducing
    possibles = {c: set('abcdefg') for c in list('abcdefg')}

    # we only stop when every digit has been deduced
    while any(value is None for value in deduced.values()):
        for scrambled in inputs + outputs:
            scrambled = set(scrambled)
            if len(scrambled) == 2:  # digital display "1"
                possibles['c'] &= scrambled
                possibles['f'] &= scrambled
            elif len(scrambled) == 3:  # digital display "7"
                possibles['a'] &= scrambled
                possibles['c'] &= scrambled
                possibles['f'] &= scrambled
            elif len(scrambled) == 4:  # digital display "4"
                possibles['b'] &= scrambled
                possibles['c'] &= scrambled
                possibles['d'] &= scrambled
                possibles['f'] &= scrambled
            elif len(scrambled) == 5:
                # digital display: 2, 3, 5 (they all have a, d, and g union turned on)
                possibles['a'] &= scrambled
                possibles['d'] &= scrambled
                possibles['g'] &= scrambled
            elif len(scrambled) == 6:
                # digital display: 0, 6, 9 (they all have a, b, f, and g union turned on)
                possibles['a'] &= scrambled
                possibles['b'] &= scrambled
                possibles['f'] &= scrambled
                possibles['g'] &= scrambled
            # digital display "8" can't deduce anything because every digit would intersect with possibles

        for c, possible in possibles.items():
            if len(possible) == 1:
                definite = possible.pop()
                deduced[definite] = c
                for _, other in possibles.items():
                    other.difference_update(set(definite))

    def translate(mapping, chars):
        return ''.join(sorted(mapping[c] for c in chars))

    output_chars = [translate(deduced, c) for c in outputs]
    digits = [DIGIT_MAP[c] for c in output_chars]
    final = int(''.join(str(d) for d in digits))

    return final


def part1():
    return sum(len([s for s in out if len(s) in [2, 4, 3, 7]]) for _, out in lines)


def part2():
    return sum(deduce_mapping(i, o) for i, o in lines)


print(part1())
print(part2())
