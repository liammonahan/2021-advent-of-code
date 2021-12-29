
import ast
import copy
import itertools

from utils import readinput

lines = readinput()


LEFT = 0
RIGHT = 1


def left_sibling(root, path):
    try:
        index = list(reversed(path)).index(RIGHT)
    except ValueError:
        # This is the left-most, so no sibling
        return None
    index = len(path) - index - 1
    newpath = path[:index]

    curr = root
    for dir in newpath:
        curr = curr[dir]

    # then go left once
    curr = curr[LEFT]
    newpath.append(LEFT)

    # then keep going right
    while type(curr) is list:
        curr = curr[RIGHT]
        newpath.append(RIGHT)

    return newpath


def right_sibling(root, path):
    try:
        index = list(reversed(path)).index(LEFT)
    except ValueError:
        # This is the right-most, so no sibling
        return None
    index = len(path) - index - 1
    newpath = path[:index]

    curr = root
    for dir in newpath:
        curr = curr[dir]

    # then go right once
    curr = curr[RIGHT]
    newpath.append(RIGHT)

    # then keep going left
    while type(curr) is list:
        curr = curr[LEFT]
        newpath.append(LEFT)

    return newpath


def explode(root, path, left, right):
    lsib = left_sibling(root, path)
    rsib = right_sibling(root, path)

    curr = root
    if lsib is not None:
        for dir in lsib[:-1]:
            curr = curr[dir]
        curr[lsib[-1]] = curr[lsib[-1]] + left

    curr = root
    if rsib is not None:
        for dir in rsib[:-1]:
            curr = curr[dir]
        curr[rsib[-1]] = curr[rsib[-1]] + right

    insert_at(root, path, 0)

    return root


def insert_at(root, path, new):
    curr = root
    for dir in path[:-1]:
        curr = curr[dir]
    curr[path[-1]] = new

    return root


def split(root, path, val):
    leftval = val // 2
    if leftval * 2 < val:
        rightval = leftval + 1
    else:
        rightval = leftval
    insert_at(root, path, [leftval, rightval])


def _reduce_explode(rpn, root, path, depth=0):
    if type(rpn) is list:
        left, right = rpn

        if depth >= 4:
            return explode(root, path, left, right)

        leftpath = path.copy()
        leftpath.append(LEFT)
        rightpath = path.copy()
        rightpath.append(RIGHT)

        _reduce_explode(left, root=root, path=leftpath, depth=depth + 1)
        _reduce_explode(right, root=root, path=rightpath, depth=depth + 1)

    return root


def reduce_explode(rpn):
    original = rpn
    new = copy.deepcopy(original)
    changed = True
    while changed:
        new = _reduce_explode(new, new, path=[])
        if new == original:
            changed = False
        original = new
    return new


class StopException(Exception):
    def __init__(self, root):
        self.root = root


def reduce_split(rpn, root, path, depth=0):
    if type(rpn) is int:
        if rpn >= 10:
            split(root, path, rpn)
            # terminate early so that we go back to do more explode checks first
            # exceptions were the easiest way to interrupt the other recursion branches
            raise StopException(root)
    else:
        left, right = rpn

        leftpath = path.copy()
        leftpath.append(LEFT)
        rightpath = path.copy()
        rightpath.append(RIGHT)

        root = reduce_split(left, root=root, path=leftpath, depth=depth + 1)
        root = reduce_split(right, root=root, path=rightpath, depth=depth + 1)

    return root


def reduce(rpn):
    original = rpn
    new = copy.deepcopy(original)
    changed = True
    while changed:
        new = reduce_explode(new)
        try:
            new = reduce_split(new, new, path=[])
        except StopException as e:
            new = e.root
        if new == original:
            changed = False
        original = new
    return new


def magnitude(tree):
    if type(tree) is int:
        return tree
    left, right = tree
    return magnitude(left) * 3 + magnitude(right) * 2


def part1():
    _lines = lines.copy()
    rpn = ast.literal_eval(_lines.pop(0))
    for line in _lines:
        line = ast.literal_eval(line)
        rpn = [rpn, line]
        rpn = reduce(rpn)
    return magnitude(rpn)


def part2():
    _lines = lines.copy()
    max_magnitude = 0
    for left, right in itertools.permutations(_lines, r=2):
        result = [ast.literal_eval(left), ast.literal_eval(right)]
        result = reduce(result)
        max_magnitude = max(magnitude(result), max_magnitude)
    return max_magnitude


print(part1())
print(part2())
