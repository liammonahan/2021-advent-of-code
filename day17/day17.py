
xc, yc = open('input.txt', 'r').read().strip('target area: ').split(', ')
xcoord = [int(i) for i in xc.lstrip('x=').split('..')]
ycoord = [int(i) for i in yc.lstrip('y=').split('..')]


initials_in_target = set()
highest = set()
xrange = range(xcoord[0], xcoord[1] + 1)
yrange = range(ycoord[0], ycoord[1] + 1)
for initial_x_vel in range(0, 200):
    for initial_y_vel in range(-300, 1200):
        x_pos, y_pos = 0, 0
        x_vel, y_vel = initial_x_vel, initial_y_vel
        highest_y = y_pos

        for i in range(1200):

            # step
            x_pos += x_vel
            y_pos += y_vel
            if x_vel > 0:
                x_vel -= 1
            elif x_vel < 0:
                x_vel += 1
            y_vel -= 1

            # optimization to stop stepping after we have overshot the target
            if x_pos > xcoord[1]:
                break
            if y_pos < ycoord[0]:
                break

            highest_y = max(highest_y, y_pos)

            if x_pos in xrange and y_pos in yrange:
                highest.add(highest_y)
                initials_in_target.add((initial_x_vel, initial_y_vel))


# part1
print(max(highest))

# part2
print(len(initials_in_target))
