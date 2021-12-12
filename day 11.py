

def one():
    data = []
    for line in open("day 11 data.txt"):
        data.append([int(f) for f in line.strip()])
    
    flash_amount = 0
    for step in range(100):
        # add 1 to each octopus
        flash = []
        for i in range(len(data)):
            for j in range(len(data[0])):
                data[i][j] += 1
                if data[i][j] == 10:
                    flash.append([i, j])
                    flash_amount += 1
        # flash all octopodes            
        while not len(flash) == 0:
            cur = flash.pop(0)
            for neighbour in get_neighbours(data, cur[0], cur[1]):
                if data[neighbour[0]][neighbour[1]] == 9:
                    data[neighbour[0]][neighbour[1]] = 10
                    flash.append([neighbour[0], neighbour[1]])
                    flash_amount += 1
                elif data[neighbour[0]][neighbour[1]] < 9:
                    data[neighbour[0]][neighbour[1]] += 1
        # set all flashing octopodes to 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == 10:
                    data[i][j] = 0
        
    
    return flash_amount
    

def get_neighbours(data, x, y):
    neighbours = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not x + i < 0 and not x + i > len(data) - 1 and not y + j < 0 and not y + j > len(data) - 1:
                neighbours.append([x + i, y + j])
    return neighbours


def two():
    data = []
    for line in open("day 11 data.txt"):
        data.append([int(f) for f in line.strip()])
    
    step = 0
    while not all_zeroes(data):
        step += 1
        # add 1 to each octopus
        flash = []
        for i in range(len(data)):
            for j in range(len(data[0])):
                data[i][j] += 1
                if data[i][j] == 10:
                    flash.append([i, j])
        # flash all octopodes            
        while not len(flash) == 0:
            cur = flash.pop(0)
            for neighbour in get_neighbours(data, cur[0], cur[1]):
                if data[neighbour[0]][neighbour[1]] == 9:
                    data[neighbour[0]][neighbour[1]] = 10
                    flash.append([neighbour[0], neighbour[1]])
                elif data[neighbour[0]][neighbour[1]] < 9:
                    data[neighbour[0]][neighbour[1]] += 1
        # set all flashing octopodes to 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == 10:
                    data[i][j] = 0
        
    
    return step


def all_zeroes(data):
    for line in data:
        for point in line:
            if not point == 0:
                return False
    return True


print(one())
print(two())
