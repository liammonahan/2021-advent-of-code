
import ast

from utils import readinput

lines = readinput()


def explode(val, left, right):
    rm = rightmost(left)
    if rm is None:
        return 0
    else:
        return rm + val


def rightmost(tree):
    if not tree:
        return None
    if type(tree) == int:
        return tree
    else:
        right = tree[-1]
        return rightmost(right)


def reduce(rpn, parent=None, depth=0):
    if type(rpn) is int:
        return rpn
    else:
        left, right = rpn

        if depth > 4:
            print(f'depth is {depth}')
            print(rpn)
            print(f'{lefthalf=}, {righthalf=}')
            ancestor = None
            while ancestor is None:
                up = parent
            left = explode(left, lefthalf, righthalf)

        return [
            reduce(left, parent=rpn, depth=depth+1),
            reduce(right, parent=rpn, depth=depth+1),
        ]


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


rpn = ast.literal_eval(lines.pop(0))
for line in lines:
    line = ast.literal_eval(line)
    rpn = [rpn, line]
    print()
    print(rpn)
    rpn = reduce(rpn)
    print(rpn)
