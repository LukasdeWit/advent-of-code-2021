
def one():
    boards, instructions = parse_data("day 4 data.txt")
    found_winning_board = False
    cur_instr_pos = -1
    winning_board = -1
    
    while not found_winning_board:
        cur_instr_pos += 1
        instr = instructions[cur_instr_pos]
        add_num(boards, instr)
        found_winning_board, winning_board = check_boards(boards)
    
    return count_vals(boards[winning_board]) * int(instructions[cur_instr_pos])


def parse_data(filename):
    f = open(filename)
    instructions = f.readline().strip().split(',')
    boards = []
    while f.readline() != '':
        boards.append(read_board(f))
    return boards, instructions


def read_board(lines):
    board = []
    for i in range(5):
        line = lines.readline().strip().split(' ')
        while '' in line:
            line.remove('')
        board.append(line)
    return board


def add_num(boards, num):
    for board in boards:
        for line in board:
            if num in line:
                line[line.index(num)] = 'X'


def check_boards(boards):
    board_height = len(boards[0])
    board_width = len(boards[0][0])
    for board in boards:
        # check horizontal
        for line in board:
            if line == ['X', 'X', 'X', 'X', 'X']:
                return True, boards.index(board)
        for i in range(board_width):
            found = True
            for j in range(board_height):
                if board[j][i] != 'X':
                    found = False
            if found:
                return True, boards.index(board)
    return False, -1


def count_vals(board):
    total = 0
    for line in board:
        for val in line:
            if val != 'X':
                total += int(val)
    return total


def two():
    boards, instructions = parse_data("day 4 data.txt")
    cur_instr_pos = -1
    
    while len(boards) > 1:
        cur_instr_pos += 1
        instr = instructions[cur_instr_pos]
        add_num(boards, instr)
        boards = check_and_remove_boards(boards)
    
    board_winning, final_instr = check_boards(boards)
    while not board_winning:
        cur_instr_pos += 1
        instr = instructions[cur_instr_pos]
        add_num(boards, instr)
        board_winning, _ = check_boards(boards)
        
    return count_vals(boards[0]) * int(instructions[cur_instr_pos])


def check_and_remove_boards(boards):
    new_boards = [b for b in boards]
    board_height = len(boards[0])
    board_width = len(boards[0][0])
    for board in boards:
        to_remove = False
        for line in board:
            if line == ['X', 'X', 'X', 'X', 'X']:
                to_remove = True
        for i in range(board_width):
            found = True
            for j in range(board_height):
                if board[j][i] != 'X':
                    found = False
            if found:
                to_remove = True
        if to_remove:
            new_boards.remove(board)
    return new_boards
    

print(one())
print(two())
