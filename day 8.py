# segments reminder
#  aa
# b  c
#  dd
# e  f
#  gg
# 0 = abcefg (6), 1 = cf (2), 2 = acdeg (5), 3 = acdfg (5), 4 = bcdf (4),
# 5 = abdfg (5), 6 = abdefg (6), 7 = acf (3), 8 = abcdefg (7), 9 = abcdfg (6)
#
# determine the numbers:
# we can find which numbers are 1 (2 bars), 4 (4 bars), 7 (3 bars), 8 (7 bars)
# we can find 9 because it's a 6-bar character that contains all bars that are also in 4
# knowing 9, we can find 0 because it's a 6-bar character that contains all bars that are also in 7
# knowing 9 and 0, we can find 6 because it's the last leftover 6-bar character
# we can find 3 because it's a 5-bar character that contains all bars that are also in 7
# knowing 3, we can find 5 because it's a 5-bar character and all its bars are also in 6
# knowing all other numbers, we can find 2 by elimination

def one():
    data = parse_data("day 8 data.txt")
    total = 0
    for line in data:
        for code in line[1]:
            if len(code) == 2 or len(code) == 3 or len(code) == 4 or len(code) == 7:
                total += 1
    return total


def parse_data(filename):
    data = []
    for line in open(filename):
        letters = line.split(" | ")[0].split(' ')
        code = line.split(" | ")[1].strip().split(' ')
        data.append([letters, code])
    return data
    

def two():
    data = parse_data("day 8 data.txt")
    total = 0
    for line in data:
        letter_mapping = find_letter_mapping(line[0])
        total += parse_code(letter_mapping, line[1])
    return total


def find_letter_mapping(line):
    mapping = [''] * 10
    # first, find 1, 4, 7 and 8
    new_line = [f for f in line]
    for num in line:
        if len(num) == 2:
            mapping[1] = ''.join(sorted(num))
            new_line.remove(num)
        elif len(num) == 4:
            mapping[4] = ''.join(sorted(num))
            new_line.remove(num)
        elif len(num) == 3:
            mapping[7] = ''.join(sorted(num))
            new_line.remove(num)
        elif len(num) == 7:
            mapping[8] = ''.join(sorted(num))
            new_line.remove(num)
    line = [f for f in new_line]
    
    # find 9 and 3
    for num in line:
        if len(num) == 5:
            bars_in_seven = True
            for char in mapping[7]:
                if not char in num:
                    bars_in_seven = False
            if bars_in_seven:
                mapping[3] = ''.join(sorted(num))
                new_line.remove(num)
        if len(num) == 6:
            bars_in_four = True
            for char in mapping[4]:
                if not char in num:
                    bars_in_four = False
            if bars_in_four:
                mapping[9] = ''.join(sorted(num))
                new_line.remove(num)
    line = [f for f in new_line]
    
    # find 0
    for num in line:
        if len(num) == 6:
            bars_in_seven = True
            for char in mapping[7]:
                if not char in num:
                    bars_in_seven = False
            if bars_in_seven:
                mapping[0] = ''.join(sorted(num))
                new_line.remove(num)
    line = [f for f in new_line]
    
    # find 6
    for num in line:
        if len(num) == 6:
            mapping[6] = ''.join(sorted(num))
            new_line.remove(num)
    line = [f for f in new_line]
    
    # find 5
    for num in line:
        if len(num) == 5:
            all_bars_in_six = True
            for char in num:
                if not char in mapping[6]:
                    all_bars_in_six = False
            if all_bars_in_six:
                mapping[5] = ''.join(sorted(num))
                new_line.remove(num)
    line = [f for f in new_line]
    
    mapping[2] = ''.join(sorted(line[0]))
    return mapping


def parse_code(letter_mapping, code):
    total = 0
    for num in code:
        total *= 10
        total += letter_mapping.index(''.join(sorted(num)))
    return total


print(one())
print(two())
