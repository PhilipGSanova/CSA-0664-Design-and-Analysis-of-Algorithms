def find_empty_location(board, l):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

def used_in_row(board, row, num):
    return num in board[row]

def used_in_col(board, col, num):
    return num in [board[i][col] for i in range(9)]

def used_in_box(board, row, col, num):
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    return any(num == board[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3))

def is_safe(board, row, col, num):
    return not used_in_row(board, row, num) and not used_in_col(board, col, num) and not used_in_box(board, row, col, num)

def solve_sudoku(board):
    l = [0, 0]
    if not find_empty_location(board, l):
        return True
    row, col = l[0], l[1]
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

# Example Sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    for row in board:
        print(row)
else:
    print("No solution exists")
