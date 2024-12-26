from utils import solve

good = ["X", "M", "A", "S"]
goodrev = ["S", "A", "M", "X"]

def start_search(ws, row, col):
    elem = ws[row][col]
    return elem == "X" or elem == "S"

def is_match(word):
    return word == good or word == goodrev

def is_sam_match(word):
    return "".join(word) in ["MSAMS", "SMASM", "SSAMM", "MMASS"]

def search(ws, row, col, rows, cols):
    # right
    count = 0
    if is_match(ws[row][col:col+4]):
        count += 1

    # down
    if row + 3 < rows:
        word = [
            ws[row][col],
            ws[row+1][col],
            ws[row+2][col],
            ws[row+3][col],
        ]
        if is_match(word):
            count += 1
    
    # bottom left diag
    if row + 3 < rows and col - 3 >= 0:
        word = [
            ws[row][col],
            ws[row+1][col-1],
            ws[row+2][col-2],
            ws[row+3][col-3],
        ]
        if is_match(word):
            count += 1

    # bottom right diag
    if row + 3 < rows and col + 3 < cols:
        word = [
            ws[row][col],
            ws[row+1][col+1],
            ws[row+2][col+2],
            ws[row+3][col+3],
        ]
        if is_match(word):
            count += 1 

    return count

def search2(ws, row, col, rows, cols):
    if row + 3 > rows or col + 3 > cols:
        return 0

    """
    S . S
    . A .
    M . M
    """
    word = [
        ws[row][col],
        ws[row][col+2],
        ws[row+1][col+1],
        ws[row+2][col],
        ws[row+2][col+2]
    ]
    if is_sam_match(word):
        return 1
    else:
        return 0

def calc(f):
    ws = []
    for line in f:
        ws.append(list(line.strip()))
    count = 0
    rows = len(ws)
    cols = len(ws[0])

    for row in range(rows):
        for col in range(cols):
            # count += search(ws, row, col, rows, cols)
            count += search2(ws, row, col, rows, cols)
    print(count)

solve("day4.in", calc)