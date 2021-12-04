

def readgroups(input_file):
    groups = open(input_file, 'r').read().strip().split('\n\n')
    groups = [[line.strip() for line in group.split('\n')] for group in groups]
    return groups


def to_ints(lst):
    return [int(item) for item in lst]