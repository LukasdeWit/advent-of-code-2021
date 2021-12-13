
def one():
    data = [f.strip() for f in open("day 13 data.txt")]
    nodes = []
    folds = []
    
    for line in data:
        if not len(line) == 0 and ',' in line:
            x, y = line.split(',')
            nodes.append([int(x), int(y)])
        elif not len(line) == 0 and '=' in line:
            x, y = line[11:].split('=')
            folds.append([x, int(y)])
    
    nodes = fold_over(nodes, folds[0])
    return len(nodes)


def fold_over(nodes, fold):
    new_nodes = []
    if fold[0] == 'x':
        for node in nodes:
            if node not in new_nodes and node[0] < fold[1]:
                new_nodes.append(node)
            elif node[0] > fold[1]:
                new_x = 2 * fold[1] - node[0]
                if [new_x, node[1]] not in new_nodes:
                    new_nodes.append([new_x, node[1]])
    elif fold[0] == 'y':
        for node in nodes:
            if node not in new_nodes and node[1] < fold[1]:
                new_nodes.append(node)
            elif node[1] > fold[1]:
                new_y = 2 * fold[1] - node[1]
                if [node[0], new_y] not in new_nodes:
                    new_nodes.append([node[0], new_y])
    return new_nodes


def two():
    data = [f.strip() for f in open("day 13 data.txt")]
    nodes = []
    folds = []
    
    for line in data:
        if not len(line) == 0 and ',' in line:
            x, y = line.split(',')
            nodes.append([int(x), int(y)])
        elif not len(line) == 0 and '=' in line:
            x, y = line[11:].split('=')
            folds.append([x, int(y)])
    
    for fold in folds:
        nodes = fold_over(nodes, fold)
    make_nice_grid(nodes)
    return len(nodes)


def make_nice_grid(nodes):
    max_x, max_y = 0, 0
    for node in nodes:
        if node[0] > max_x:
            max_x = node[0]
        if node[1] > max_y:
            max_y = node[1]
    nice_grid = []
    for i in range(max_y + 1):
        nice_grid.append(['.'] * (max_x + 1))
    for node in nodes:
        nice_grid[node[1]][node[0]] = '#'
    for line in nice_grid:
        print(''.join(line))


print(one())
print(two())
