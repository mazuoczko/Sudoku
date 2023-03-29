import random


def main():
    print(random_element())


def random_element():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(9):
        a = list_of_numbers[x]
        i = random.randrange(0, 9)
        j = random.randrange(0, 9)
        board[i][j] = a

    solve(board)

    for _ in range(81):
        i = random.randrange(0, 9)
        j = random.randrange(0, 9)
        board[i][j] = 0

    return board


def find_0(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)


def solve(board):
    find = find_0(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, number, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == number and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == number and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != pos:
                return False

    return True


if __name__ == "__main__":
    main()
