diags = [line.strip() for line in open('input.txt', 'r')]


def get_index(i):
    zeros = 0
    ones = 1
    for diag in diags:
        if diag[i] == '0':
            zeros += 1
        else:
            ones += 1

    return zeros, ones


def most_common(i):
    zeros, ones = get_index(i)
    return '0' if zeros > ones else '1'


def least_common(i):
    zeros, ones = get_index(i)
    return '1' if zeros > ones else '0'


def to_decimal(num):
    return int(num, 2)


n = len(diags[0])
gamma_rate = to_decimal(''.join(most_common(i) for i in range(n)))
epsilon_rate = to_decimal(''.join(least_common(i) for i in range(n)))

print(gamma_rate * epsilon_rate)
