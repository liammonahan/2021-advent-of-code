diagnostics = [line.strip() for line in open('input.txt', 'r')]


def get_index(diagnostics, i):
    zeros = []
    ones = []
    for diag in diagnostics:
        if diag[i] == '0':
            zeros.append(diag)
        else:
            ones.append(diag)

    return zeros, ones


def to_decimal(num):
    return int(num, 2)


i = 0
oxygens = diagnostics.copy()
while len(oxygens) > 1:
    zeros, ones = get_index(oxygens, i)
    if len(zeros) > len(ones):
        oxygens = zeros
    else:
        oxygens = ones  # covers equals
    i += 1


i = 0
co2s = diagnostics.copy()
while len(co2s) > 1:
    zeros, ones = get_index(co2s, i)
    if len(ones) < len(zeros):
        co2s = ones
    else:
        co2s = zeros  # covers equals
    i += 1


oxygen_rating = to_decimal(oxygens[0])
co2_rating = to_decimal(co2s[0])

print(oxygen_rating * co2_rating)
