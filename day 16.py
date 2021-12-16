# test data:
# data for ex 1
# data = "8A004A801A8002F478"
# data = "620080001611562C8802118E34"
# data = "C0015000016115A2E0802F182340"
# data = "A0016C880162017C3686B18A3D4780"

# data for ex 2
# data = "C200B40A82"
# data = "04005AC33890"
# data = "880086C3E88112"
# data = "CE00C43D881120"
# data = "D8005AC2A8F0"
# data = "F600BC2D8F"
# data = "9C005AC2F8F0"
# data = "9C0141080250320F1802104A08"

# the data structure: each element is a dict with one of the following structures:
# {"version": version nr, "type_id": type id, "elements": [elements]}
# {"version": version nr, "type_id": type id, "value": numeric value}
def one():
    data = open("day 16 data.txt").readline()
    _, hierarchy = parse_bin(hex_to_bin(data))
    return count_versions(hierarchy)


hex_to_bin_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


def hex_to_bin(line):
    new_line = ""
    for char in line:
        new_line += hex_to_bin_map[char]
    return new_line


dyn_bin_to_dec = {}
def bin_to_dec(line):
    if line in dyn_bin_to_dec:
        return dyn_bin_to_dec[line]
    num = 0
    for char in line:
        num *= 2
        num += int(char)
    dyn_bin_to_dec[line] = num
    return num


# returns (line, packet, amount), where line is the rest of the unparsed line, packet is the parsed packet, and amount
# is the amount of packages left to parse if amount >= 0, and -1 otherwise
def parse_bin(line):
    line, version = eat_next(line, 3)
    version = bin_to_dec(version)
    line, type_id = eat_next(line, 3)
    type_id = bin_to_dec(type_id)
    
    # if the packet is a number literal
    if type_id == 4:
        zero_at_start = False
        num_line = ""
        while not zero_at_start:
            line, subline = eat_next(line, 5)
            zero_at_start = subline[0] == "0"
            num_line += subline[1:5]
        num = bin_to_dec(num_line)
        return line, {"version": version, "type_id": type_id, "value": num}
    
    # the packet is some operator
    line, length_type_id = eat_next(line, 1)
    # the next 15 bits are a number that represents the total length in bits of the next packages
    if length_type_id == "0":
        line, length = eat_next(line, 15)
        length = bin_to_dec(length)
        line, subline = eat_next(line, length)
        elements = []
        while not subline == "":
            subline, elem = parse_bin(subline)
            elements.append(elem)
        return line, {"version": version, "type_id": type_id, "elements": elements}
    # the next 11 bits are a number that represents the number of packages that follow
    else:
        line, amount = eat_next(line, 11)
        amount = bin_to_dec(amount)
        elements = []
        for i in range(amount):
            line, elem = parse_bin(line)
            elements.append(elem)
        return line, {"version": version, "type_id": type_id, "elements": elements}


def count_versions(hierarchy):
    # if the hierarchy is only a number, print the version only
    if "value" in hierarchy:
        return hierarchy["version"]
    # if it isn't, calculate it for each element, and add it to the current
    version_number = 0
    for elem in hierarchy["elements"]:
        version_number += count_versions(elem)
    return version_number + hierarchy["version"]


# returns the next subline of lenght -amount-, and the rest of the line
def eat_next(line, amount):
    word = line[0:amount]
    new_line = ""
    if len(line) >= amount + 1:
        new_line = line[amount:]
    return new_line, word


def two():
    data = open("day 16 data.txt").readline()
    _, hierarchy = parse_bin(hex_to_bin(data))
    return interp(hierarchy)


def interp(hierarchy):
    operand = hierarchy["type_id"]
    # type id 0: sum
    if operand == 0:
        num = 0
        for elem in hierarchy["elements"]:
            num += interp(elem)
        return num
    # type id 1: product
    elif operand == 1:
        num = 1
        for elem in hierarchy["elements"]:
            num *= interp(elem)
        return num
    # type 2: minimum
    elif operand == 2:
        nums = []
        for elem in hierarchy["elements"]:
            nums.append(interp(elem))
        return min(nums)
    # type 3: maximum
    elif operand == 3:
        nums = []
        for elem in hierarchy["elements"]:
            nums.append(interp(elem))
        return max(nums)
    # type 4: number
    elif operand == 4:
        return hierarchy["value"]
    # type 5: greater than
    elif operand == 5:
        num1 = interp(hierarchy["elements"][0])
        num2 = interp(hierarchy["elements"][1])
        if num1 > num2:
            return 1
        return 0
    # type 6: less than
    elif operand == 6:
        num1 = interp(hierarchy["elements"][0])
        num2 = interp(hierarchy["elements"][1])
        if num1 < num2:
            return 1
        return 0
    # type 7: equal
    elif operand == 7:
        num1 = interp(hierarchy["elements"][0])
        num2 = interp(hierarchy["elements"][1])
        if num1 == num2:
            return 1
        return 0
    

print(one())
print(two())
