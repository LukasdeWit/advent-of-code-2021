
def one():
    data = [int(f) for f in open("day 7 data.txt").readline().split(',')]
    median = calc_median(data)
    return dist_from(data, median)
    

def calc_median(data):
    index = len(data) // 2
    data.sort()
    return data[index]


def dist_from(data, number):
    total = 0
    for num in data:
        total += abs(num - number)
    return total


def two():
    data = [int(f) for f in open("day 7 data.txt").readline().split(',')]
    avg = calc_avg(data)
    # okay so this is super ugly, but I find it hard to deal with an average that is really close to n.5
    dist = int(min(expensive_dist_from(data, avg - 1), expensive_dist_from(data, avg), expensive_dist_from(data, avg + 1)))
    return dist


def expensive_dist_from(data, number):
    total = 0
    for num in data:
        dist = abs(num - number)
        total += ((dist + 1) * (dist / 2))
    return total


def calc_avg(data):
    return round(sum(data) / len(data))


print(one())
print(two())
