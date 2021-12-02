instructions = [line.strip() for line in open('input.txt', 'r')]
instructions = [ins.split() for ins in instructions]
instructions = [tuple([ins[0], int(ins[1])]) for ins in instructions]

horizontal, depth, aim = 0, 0, 0

for direction, length in instructions:
    if direction == 'forward':
        horizontal += length
        depth += aim * length
    elif direction == 'up':
        aim -= length
    elif direction == 'down':
        aim += length

print(horizontal * depth)
