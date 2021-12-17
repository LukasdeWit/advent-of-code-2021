
def one():
    data = open("day 17 data.txt").readline()
    x_range, y_range = data[13:].split(", ")
    x_min, x_max = [int(x) for x in x_range[2:].split("..")]
    y_min, y_max = [int(y) for y in y_range[2:].split("..")]
    
    # because math exists, we can do some simple reductions in the problem
    # We want to know if there is some x_speed where the probe will fal through the box vertically (x_speed == 0
    # when x_min <= x_pos <= x_max. we could do this check to make this work on arbitrary datasets, but through
    # observation of the datasets we know this to be true in our case. That means we need to find an y_speed that makes
    # the probe not overshoot the box. We know that, because the starting y_pos == 0, the probe should go through (x, 0)
    # at some point, where x is the pos of the vertical line. we also know that the step from 0 can't be larger than
    # abs(y_min) (this because in our datasets, the box' y coords are all below 0). that means the speed we should shoot
    # the probe up with is abs(y_min) - 1. Then just calculate the y value that this ends up at.
    return sum([f for f in range(abs(y_min))])
        

# takes the x-bounds of the box and the speed of the probe, and returns a list of x-positions where the probe is within
# these bounds
def is_in_trajectory(x_min, x_max, x_speed):
    total = 0
    cur_speed = x_speed
    x_positions = []
    while cur_speed > 0:
        total += cur_speed
        cur_speed -= 1
        if x_min <= total <= x_max:
            x_positions += [x_speed - cur_speed]
    return x_positions


def two():
    data = open("day 17 data myrte.txt").readline()
    x_range, y_range = data[13:].split(", ")
    x_min, x_max = [int(x) for x in x_range[2:].split("..")]
    y_min, y_max = [int(y) for y in y_range[2:].split("..")]
    
    # keep track of all hits
    total = []
    # calculate how many x_speeds shoot through our box, and at how many places
    # x_shots is a map that holds all the "amount of steps" that a direct line could hit the box
    x_shots = {}
    for i in range(1, x_max + 1):
        x_positions = is_in_trajectory(x_min, x_max, i)
        extreme_position = (i + 1) * i // 2
        if not len(x_positions) == 0:
            x_shots[i] = x_positions
            
    # for each direct line, calculate all possible y's that hit the box in that many steps
    for x_speed in x_shots:
        for step in x_shots[x_speed]:
            for y_speed in range(y_min, abs(y_min) + 1):
                if y_min <= step * y_speed - ((step - 1) * step // 2) <= y_max:
                    if (x_speed, y_speed) not in total:
                        total.append((x_speed, y_speed))
        
    # then, for each indirect line, calculate all possible y's that hit the box
    for x_speed in x_shots:
        if x_speed in x_shots[x_speed]:
            for y_speed in range(y_min, abs(y_min) + 1):
                if y_hits_box(y_min, y_max, y_speed, x_speed) and (x_speed, y_speed) not in total:
                    total.append((x_speed, y_speed))
                    
    return len(total)


def y_hits_box(y_min, y_max, y_speed, min_steps):
    total = 0
    hit = False
    for i in range(min_steps):
        total += y_speed
        y_speed -= 1
    while total >= y_min and not hit:
        total += y_speed
        y_speed -= 1
        if y_min <= total <= y_max:
            hit = True
    return hit


print(one())
print(two())
