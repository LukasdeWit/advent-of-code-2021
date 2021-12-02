
def one():
    depth = 0
    forward = 0
    for line in open("day 2 data.txt"):
        if line.split()[0] == "forward":
            forward += int(line.split()[1])
        elif line.split()[0] == "down":
            depth += int(line.split()[1])
        elif line.split()[0] == "up":
            depth -= int(line.split()[1])
    return depth * forward


def two():
    aim = 0
    depth = 0
    forward = 0
    for line in open("day 2 data.txt"):
        if line.split()[0] == "forward":
            forward += int(line.split()[1])
            depth += aim * int(line.split()[1])
        elif line.split()[0] == "down":
            aim += int(line.split()[1])
        elif line.split()[0] == "up":
            aim -= int(line.split()[1])
    return depth * forward


print(one())
print(two())