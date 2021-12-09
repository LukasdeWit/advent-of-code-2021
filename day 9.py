
def one():
    data = []
    for line in open("day 9 data.txt"):
        data_line = [int(f) for f in line.strip()]
        data.append(data_line)
    local_minima = find_local_minima(data)
    # now we calculate DANGER LEVEL
    total = 0
    for minimum in local_minima:
        total += data[minimum[0]][minimum[1]]
    total += len(local_minima)
    return total


# making this method way too specific because I'm afraid of what puzzle 2 will be
def find_local_minima(data):
    local_minima = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            minimum = True
            for neighbour in find_neighbours_values(data, i, j):
                if neighbour <= data[i][j]:
                    minimum = False
            if minimum:
                local_minima.append([i, j])
    return local_minima
                

# x and y are probably flipped here but I'm sure that won't become a problem later
def find_neighbours_values(data, x, y):
    neighbours = []
    if not x == 0:
        neighbours.append(data[x - 1][y])
    if not x == len(data) - 1:
        neighbours.append(data[x + 1][y])
    if not y == 0:
        neighbours.append(data[x][y - 1])
    if not y == len(data[0]) - 1:
        neighbours.append(data[x][y + 1])
    return neighbours


def two():
    data = []
    for line in open("day 9 data.txt"):
        data_line = [int(f) for f in line.strip()]
        data.append(data_line)
    local_minima = find_local_minima(data)
    # find a basin for each minimum
    basins = []
    for minimum in local_minima:
        basins.append(hill_climbing(data, minimum[0], minimum[1]))
    # calculate top three basin multiplied
    total = 1
    for i in range(3):
        size, basins = pop_largest_basin(basins)
        total *= size
    return total


# returns the size of the hill (or the basin in this case) (let's call this stupid hill climbing)
def hill_climbing(data, x, y):
    prev_points = [[x, y]]
    current_points = [[x, y]]
    while len(current_points) > 0:
        cur = current_points.pop(0)
        for p in find_neighbours_locations(data, cur[0], cur[1]):
            if p not in prev_points:
                current_points.append(p)
                prev_points.append(p)
    return prev_points


def find_neighbours_locations(data, x, y):
    neighbours = []
    if not x == 0:
        if not data[x - 1][y] == 9:
            neighbours.append([x - 1, y])
    if not x == len(data) - 1:
        if not data[x + 1][y] == 9:
            neighbours.append([x + 1, y])
    if not y == 0:
        if not data[x][y - 1] == 9:
            neighbours.append([x, y - 1])
    if not y == len(data[0]) - 1:
        if not data[x][y + 1] == 9:
            neighbours.append([x, y + 1])
    return neighbours


def pop_largest_basin(basins):
    new_basins = [b for b in basins]
    largest_index = -1
    largest_size = -1
    for i in range(len(basins)):
        if len(basins[i]) > largest_size:
            largest_index = i
            largest_size = len(basins[i])
    new_basins.pop(largest_index)
    return largest_size, new_basins


print(one())
print(two())
