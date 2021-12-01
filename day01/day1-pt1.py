sweeps = [int(line.strip()) for line in open('day1-sweeps.txt', 'r')]

increases = 0

# [a, b, c, d] becomes ( (a,b), (b,c), (c,d))
pairs = zip(sweeps[:-1], sweeps[1:])
for a, b in pairs:
    if b > a:
        increases += 1

print(increases)
