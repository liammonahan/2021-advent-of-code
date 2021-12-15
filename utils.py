

def readgroups(filename='input.txt'):
    groups = open(filename, 'r').read().strip().split('\n\n')
    groups = [[line.strip() for line in group.split('\n')] for group in groups]
    return groups


def readinput(filename='input.txt'):
    lines = open(filename, 'r').readlines()
    lines = [line.strip() for line in lines]
    if len(lines) == 1:
        return lines[0]
    return lines


def to_ints(lst):
    return [int(item) for item in lst]