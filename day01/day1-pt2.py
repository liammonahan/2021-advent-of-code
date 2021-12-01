sweeps = [int(line.strip()) for line in open('day1-sweeps.txt', 'r')]

increases = 0

# [a, b, c, d, e] becomes ( (a,b,c), (b,c,d), (c,d,e))
windows = zip(sweeps[:-1], sweeps[1:], sweeps[2:])
summed_windows = [sum(measurements) for measurements in windows]
pairs = zip(summed_windows[:-1], summed_windows[1:])
for a, b in pairs:
    if b > a:
        increases += 1

print(increases)
