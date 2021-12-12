

def one():
    data = [f.strip() for f in open("day 12 data.txt")]
    caves = create_caves(data)
    paths = find_paths(caves, "start", caves.keys())
    return len(paths)


def create_caves(data):
    caves = {}
    for line in data:
        key, value = line.split('-')
        if key not in caves:
            caves[key] = []
        if value not in caves:
            caves[value] = []
        caves[key].append(value)
        caves[value].append(key)
    return caves


def find_paths(caves, key, valid_nodes):
    if key == "end":
        return [["end"]]
    new_valid_nodes = [n for n in valid_nodes]
    if key.islower():
        new_valid_nodes.remove(key)
    valid_paths = []
    for node in caves[key]:
        if node in new_valid_nodes:
            for answer in find_paths(caves, node, new_valid_nodes):
                valid_paths.append([key] + answer)
    return valid_paths


def two():
    data = [f.strip() for f in open("day 12 data.txt")]
    caves = create_caves(data)
    total_paths = find_paths_doubles(caves, False, "start", [])
    return total_paths


# long lists are inefficient so let's try just using numbers
def find_paths_doubles(caves, double, key, visited):
    if key == "end":
        return 1
    if key in visited:
        if double:
            return 0
        else:
            if key == "start":
                return 0
            double = True
    new_visited = [f for f in visited]
    if key.islower():
        new_visited.append(key)
    total = 0
    for node in caves[key]:
        total += find_paths_doubles(caves, double, node, new_visited)
    return total 


print(one())
print(two())
