
corrupted_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

opening_chars = ['(', '[', '{', '<']
closing_chars = [')', ']', '}', '>']
opening_closing_map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def one():
    data = [f.strip() for f in open("day 10 data.txt")]
    total = 0
    for line in data:
        brackets = []
        for character in line:
            if character in opening_chars:
                brackets.append(character)
            if character in closing_chars:
                opening = brackets.pop()
                if not opening_closing_map[opening] == character:
                    total += corrupted_points[character]
                    break
    return total


incomplete_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def two():
    data = [f.strip() for f in open("day 10 data.txt")]
    # first filter out all corrupted lines
    new_data = [f for f in data]
    for line in data:
        brackets = []
        for character in line:
            if character in opening_chars:
                brackets.append(character)
            if character in closing_chars:
                opening = brackets.pop()
                if not opening_closing_map[opening] == character:
                    new_data.remove(line)
                    break
    
    # then complete all correct lines
    data = [f for f in new_data]
    scores = []
    for line in data:
        brackets = []
        score = 0
        for character in line:
            if character in opening_chars:
                brackets.append(character)
            if character in closing_chars:
                opening = brackets.pop()
        for bracket in brackets[::-1]:
            score *= 5
            score += incomplete_points[opening_closing_map[bracket]]
        scores.append(score)
    scores.sort()
    return scores[(len(scores) - 1) // 2]


print(one())
print(two())
