def read_input(file="input.txt"):
    with open(file, "r") as file:
        data = file.read().strip()
        return data


def check_point(board, pos, shape):
    return all((0 <= pos[0] < shape[0],
                0 <= pos[1] < shape[1],
                board[pos[0]][pos[1]] == 0,))


if __name__ == "__main__":
    a = (8, 10)
    matrix = [[0] * a[0]] * a[1]
    x_y = (0, 11)
    print(check_point(matrix, x_y, a))
