instructions = [line.strip() for line in open('input.txt', 'r')]
instructions = [ins.split() for ins in instructions]
instructions = [tuple([ins[0], int(ins[1])]) for ins in instructions]

horizontal, depth = 0, 0

for direction, length in instructions:
    if direction == 'forward':
        horizontal += length
    elif direction == 'up':
        depth -= length
    elif direction == 'down':
        depth += length

print(horizontal * depth)
