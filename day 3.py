
def one():
    data = [line.strip() for line in open("day 3 data.txt")]
    word_size = len(data[0])
    bitcount = count_bits(data, word_size)
    gamma = ""
    epsilon = ""
    for bit in bitcount:
        if bit < len(data) / 2:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return bin_str_to_dec(gamma) * bin_str_to_dec(epsilon)
    

def count_bits(data, word_size):
    bitcount = [0] * word_size
    for word in data:
        for i in range(word_size):
            if word[i] == "1":
                bitcount[i] += 1
    return bitcount


def bin_str_to_dec(var):
    num = 0
    inc = 1
    for char in var[::-1]:
        if char == "1":
            num += inc
        inc *= 2
    return num


def two():
    data = [line.strip() for line in open("day 3 data.txt")]
    oxy = find_oxy(data, 0)
    co = find_co(data, 0)
    return bin_str_to_dec(oxy) * bin_str_to_dec(co)


def find_oxy(d, index):
    data = [word for word in d]
    new_data = [word for word in d]
    wordcount = len(data)
    bitcount = count_bits(data, len(data[0]))
    expected_bit = "0"
    if bitcount[index] >= (wordcount / 2):
        expected_bit = "1"
    
    for word in data:
        if word[index] != expected_bit:
            new_data.remove(word)
    if len(new_data) == 1:
        return new_data[0]
    elif index + 1 == len(new_data[0]):
        return new_data[0]
    else:
        return find_oxy(new_data, index + 1)
        

def find_co(d, index):
    data = [word for word in d]
    new_data = [word for word in d]
    wordcount = len(data)
    bitcount = count_bits(data, len(data[0]))
    expected_bit = "0"
    if bitcount[index] < (wordcount / 2):
        expected_bit = "1"
    
    for word in data:
        if word[index] != expected_bit:
            new_data.remove(word)
    if len(new_data) == 1:
        return new_data[0]
    elif index + 1 == len(new_data[0]):
        return new_data[0]
    else:
        return find_co(new_data, index + 1)
    

print(one())
print(two())
