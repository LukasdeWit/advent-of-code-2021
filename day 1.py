
def one():
    prev = 0
    increased = -1
    for line in open("day 1 data.txt"):
        if int(line) > prev:
            increased += 1
        prev = int(line)
    return increased


def two():
    depths = [int(line) for line in open("day 1 data.txt")]
    prev = depths[0] + depths[1] + depths[2]
    increased = 0
    for i in range(3, len(depths)):
        n_val = depths[i] + depths[i - 1] + depths[i - 2]
        if n_val > prev:
            increased += 1
        prev = n_val
    return increased


print(one())
print(two())
