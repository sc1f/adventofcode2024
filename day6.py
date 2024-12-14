from utils import open_input

directions = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

facing = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

def in_bounds(board, row, col):
    return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])

def traverse(board, row, col):
    currdir = board[row][col]
    while in_bounds(board, row, col):
        movement = directions[currdir]
        if not in_bounds(board, row+movement[0], col+movement[1]):
            # print("leaving at", row, col)
            break

        nextpos = board[row+movement[0]][col+movement[1]]
        nextdir = currdir
        if nextpos == "#":
            nextdir = facing[currdir]
            movement = directions[nextdir]
            # print("turning", nextdir, row, col)
        board[row][col] = "X"
        row += movement[0]
        col += movement[1]
        currdir = nextdir
    
    count = 0
    for row in board:
        for c in row:
            if c == "X":
                count += 1
    # print("\n".join(["".join(r) for r in board]))
    return count + 1

def traverse2(board, row, col, obs_row, obs_col):
    if row == obs_row and col == obs_col:
        return False
    new_board = [b[:] for b in board]
    new_board[obs_row][obs_col] = "#"
    states = {}
    currdir = new_board[row][col]
    steps = 0
    
    while steps < 10000 and in_bounds(new_board, row, col):
        state = (row, col, currdir)
        if state in states:
            return True
            
        states[state] = steps
        movement = directions[currdir]
        next_row, next_col = row + movement[0], col + movement[1]
        
        if not in_bounds(new_board, next_row, next_col):
            return False
            
        nextpos = new_board[next_row][next_col]
        if nextpos == "#":
            currdir = facing[currdir]
        else:
            row, col = next_row, next_col
            
        steps += 1
            
    return False

def find_loop(board, row, col):
    loops = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                if traverse2(board, row, col, i, j):
                    loops.add((i, j))
    return len(loops)

def calc(f):
    board = []
    for line in f:
        board.append(list(line.strip()))
    row, col = 0,0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "^":
                row, col = i, j
    print(find_loop(board, row, col))
    
open_input("day6.in", calc)