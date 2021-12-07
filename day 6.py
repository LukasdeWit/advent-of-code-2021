# this was my naive implementation for one, it'll be left here as a warning for naive readers

#def one():
#    data = [int(f) for f in open("day 6 data.txt").readline().split(',')]
#    for i in range(80):
#        data = age_and_spawn_fish(data)
#    return len(data)

def one():
    data = [int(f) for f in open("day 6 data.txt").readline().split(',')]
    fish_setup(data)
    for i in range(80):
        fish_step()
    return count_fish()


# this was my naive implementation for one, it'll be left here as a warning for naive readers
def age_and_spawn_fish(data):
    fish_spawned = 0
    for i in range(len(data)):
        if data[i] == 0:
            fish_spawned += 1
            data[i] = 6
        else:
            data[i] -= 1
    for i in range(fish_spawned):
        data.append(8)
    return data


def two():
    data = [int(f) for f in open("day 6 data.txt").readline().split(',')]
    fish_setup(data)
    for i in range(256):
        fish_step()
    return count_fish()


fish_list = [0] * 9
def fish_setup(data):
    for i in range(len(fish_list)):
        fish_list[i] = 0
    for fish in data:
        fish_list[fish] += 1


def fish_step():
    new_fish = fish_list[0]
    for i in range(len(fish_list) - 1):
        fish_list[i] = fish_list[i + 1]
    fish_list[6] += new_fish
    fish_list[8] = new_fish
    

def count_fish():
    total = 0
    for fish in fish_list:
        total += fish
    return total


print(one())
print(two())
