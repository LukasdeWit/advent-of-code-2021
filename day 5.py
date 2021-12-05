
def one():
    data = [line.strip().split(" -> ") for line in open("day 5 data.txt")]
    for point in data:
        for coord_pair in point:
            coords = coord_pair.split(',')
            for i in range(2):
                coords[i] = int(coords[i])
            point[point.index(coord_pair)] = coords
            
    data = remove_non_hori_verti(data)
    vent_coords = {}
    for point in data:
        for coord_pair in get_all_intermediates(point):
            if not str(coord_pair) in vent_coords:
                vent_coords[str(coord_pair)] = 0
            vent_coords[str(coord_pair)] += 1
    total = 0
    for coord in vent_coords:
        if vent_coords[coord] > 1:
            total += 1
    return total
    

def remove_non_hori_verti(data):
    new_data = [d for d in data]
    for point in data:
        if not (point[0][0] == point[1][0] or point[0][1] == point[1][1]):
            new_data.remove(point)
    return new_data


def get_all_intermediates(point):
    inter_points = []
    # vertical line
    if point[0][0] == point[1][0]:
        min_val, max_val = min(point[0][1], point[1][1]), max(point[0][1], point[1][1])
        for i in range(min_val, max_val + 1):
            inter_points.append([point[0][0], i])
    
    # horizontal line
    elif point[0][1] == point[1][1]:
        min_val, max_val = min(point[0][0], point[1][0]), max(point[0][0], point[1][0])
        for i in range(min_val, max_val + 1):
            inter_points.append([i, point[0][1]])
    
    # diagonal line (lines are only ever vertical, horizontal or diagonal)
    else:
        cur_point_x, cur_point_y = point[0][0], point[0][1]
        inter_points.append([cur_point_x, cur_point_y])
        while cur_point_x != point[1][0]:
            if point[1][0] < cur_point_x:
                cur_point_x -= 1
            else:
                cur_point_x += 1
            if point[1][1] < cur_point_y:
                cur_point_y -= 1
            else:
                cur_point_y += 1
            inter_points.append([cur_point_x, cur_point_y])
        
    return inter_points
    

def two():
    data = [line.strip().split(" -> ") for line in open("day 5 data.txt")]
    for point in data:
        for coord_pair in point:
            coords = coord_pair.split(',')
            for i in range(2):
                coords[i] = int(coords[i])
            point[point.index(coord_pair)] = coords
    
    vent_coords = {}
    for point in data:
        for coord_pair in get_all_intermediates(point):
            if not str(coord_pair) in vent_coords:
                vent_coords[str(coord_pair)] = 0
            vent_coords[str(coord_pair)] += 1
    total = 0
    for coord in vent_coords:
        if vent_coords[coord] > 1:
            total += 1
    return total


print(one())
print(two())
