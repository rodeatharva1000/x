
def print_board(board, n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(board[i][j], "  ", end="")
        print()
    print("_"*(n*4))

def isValid(board, i, j, n):
    for x in range(1, i):
        if board[x][j] == 1:
            return False
        
    x, y = i-1, j-1
    while x > 0 and y > 0:
        if board[x][y] == 1:
            return False
        x = x-1
        y = y-1

    x, y = i-1, j+1
    while x>0 and y<=n:
        if board[x][y] == 1:
            return False
        x -= 1
        y += 1
    return True

def solve(board, n, row):
    if row == n+1:
        print_board(board, n)
        return True
    for col in range(1, n+1):
        if isValid(board, row, col, n):
            board[row][col] = 1
            if solve(board, n, row+1):
                return True
            board[row][col] = 0
    return False

n = int(input("Enter N : "))
b = [[0]*(n+1) for _ in range(n+1)]
b[1][2] = 1
if not solve(b, n, 2):
    print("no solution :(")

