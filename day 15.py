def one():
	data = [f.strip() for f in open("day 15 data.txt")]
	caves = []
	for f in data:
		caves.append([int(diff) for diff in f])
	return dijkstra_ish(caves, [0, 0], [len(caves) - 1, len(caves[0]) - 1])


# more like all_search, cause this is hella slows
def dijkstra_ish(caves, start, end):
	total_dist = []
	for line in caves:
		total_dist.append([float('inf') for i in range(len(line))])
	total_dist[start[0]][start[1]] = 0
	
	visited = []
	to_visit = []
	current = start
	while not current == end:
		for neighbour in find_neighbours(caves, current):
			if neighbour not in visited and neighbour not in to_visit:
				to_visit.append(neighbour)
			# check if the path through this is the shortest path to the neighbour
			if total_dist[neighbour[0]][neighbour[1]] > total_dist[current[0]][current[1]] + caves[neighbour[0]][neighbour[1]]:
				total_dist[neighbour[0]][neighbour[1]] = total_dist[current[0]][current[1]] + caves[neighbour[0]][neighbour[1]]
		to_visit = sorted(to_visit, key=lambda pos: total_dist[pos[0]][pos[1]])
		visited.append(current)
		if not len(to_visit) == 0:
			current = to_visit.pop(0)
	return total_dist[end[0]][end[1]]
	

def find_neighbours(caves, point):
	neighbours = []
	x, y = point
	for i in [-1, 1]:
		if 0 <= x + i < len(caves):
			neighbours.append([x + i, y])
		if 0 <= y + i < len(caves[0]):
			neighbours.append([x, y + i])
	return neighbours


def two():
	data = [f.strip() for f in open("day 15 data.txt")]
	caves = []
	for f in data:
		caves.append([int(diff) for diff in f])
	caves = create_large_map(caves)
	return a_star_ish(caves, [0, 0], [len(caves) - 1, len(caves[0]) - 1])


# this is sort of astar, which is probably a lot faster than dijkstra above. But also: because we don't have to
# keep track of the actual path, the dijkstra one could be done more efficiently by not tracking the path
# this implementation of astar uses taxicab distance as additional heuristic
def a_star_ish(caves, start, end):
	total_dist = []
	for line in caves:
		total_dist.append([float('inf') for i in range(len(line))])
	total_dist[start[0]][start[1]] = 0
	
	visited = []
	to_visit = []
	current = start
	prev_heuristics = []
	while not current == end:
		for neighbour in find_neighbours(caves, current):
			if neighbour not in visited and neighbour not in to_visit:
				to_visit.append(neighbour)
			# check if the path through this is the shortest path to the neighbour
			if total_dist[neighbour[0]][neighbour[1]] > total_dist[current[0]][current[1]] + caves[neighbour[0]][
				neighbour[1]]:
				total_dist[neighbour[0]][neighbour[1]] = total_dist[current[0]][current[1]] + caves[neighbour[0]][
					neighbour[1]]
		taxicab_heuristic = abs(end[0] - current[0]) + abs(end[1] - current[1])
		if taxicab_heuristic % 50 == 0 and taxicab_heuristic not in prev_heuristics:
			print("Hooray, only " + str(taxicab_heuristic) + " to go")
			prev_heuristics.append(taxicab_heuristic)
		to_visit = sorted(to_visit, key=lambda pos: total_dist[pos[0]][pos[1]] + taxicab_heuristic)
		visited.append(current)
		if not len(to_visit) == 0:
			current = to_visit.pop(0)
	return total_dist[end[0]][end[1]]


def create_large_map(caves):
	new_caves = []
	temp_caves = []
	# first create all full lines:
	for line in caves:
		new_line = []
		for i in range(5):
			new_line += [f + i for f in line]
		temp_caves.append(new_line)
	for i in range(5):
		for line in temp_caves:
			new_caves.append([f + i for f in line])
	for i in range(len(new_caves)):
		for j in range(len(new_caves[0])):
			if new_caves[i][j] > 9:
				new_caves[i][j] -= 9
	return new_caves
		
	
print(one())
print(two())