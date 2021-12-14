
def one():
    data = [f.strip() for f in open("day 14 data.txt")]
    template = data[0]
    instructions = {}
    for point in data[2:]:
        instr, letter = point.split(" -> ")
        instructions[instr] = letter
    for i in range(10):
        template = step(template, instructions)
    letters = {}
    for l in template:
        if l not in letters:
            letters[l] = 0
        letters[l] += 1
    min_letter = min(letters, key=letters.get)
    max_letter = max(letters, key=letters.get)
    return letters[max_letter] - letters[min_letter]
    
    
def step(template, instructions):
    new_template = template[0]
    for i in range(len(template) - 1):
        instr = template[i:i + 2]
        if instr in instructions:
            new_template += instructions[instr]
        new_template += template[i + 1]
    return new_template
    

# okay, wild idea: we do the same as with the lanternfish of day 6, except we count pairs
def two():
    data = [f.strip() for f in open("day 14 data.txt")]
    template = data[0]
    instructions = {}
    for point in data[2:]:
        instr, letter = point.split(" -> ")
        instructions[instr] = [instr[0] + letter, letter + instr[1]]

    instruction_counts = {}
    for i in range(len(template) - 1):
        instr = template[i:i + 2]
        if instr not in instruction_counts:
            instruction_counts[instr] = 0
        instruction_counts[instr] += 1
    
    for i in range(40):
        instruction_counts = step_smart(instructions, instruction_counts)
    
    letters = {}
    for l in instruction_counts:
        if l[0] not in letters:
            letters[l[0]] = 0
        letters[l[0]] += instruction_counts[l]
    letters[template[-1]] += 1
    min_letter = min(letters, key=letters.get)
    max_letter = max(letters, key=letters.get)
    return letters[max_letter] - letters[min_letter]


def step_smart(instructions, instruction_counts):
    new_instruction_count = {}
    for instr in instruction_counts:
        for new_instr in instructions[instr]:
            if new_instr not in new_instruction_count:
                new_instruction_count[new_instr] = 0
            new_instruction_count[new_instr] += instruction_counts[instr]
    return new_instruction_count
    

print(one())
print(two())
