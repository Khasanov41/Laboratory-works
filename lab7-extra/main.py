from core import read_input, find_next_move


if __name__ == "__main__":
    inp = "M=10, N=10, X=1, Y=1"    # read_input()

    # Parsing input data.
    trans_table = str.maketrans({'M': '', 'N': '', 'X': '', 'Y': '', ',': '', '=': ''})
    inp = tuple(map(int, inp.translate(trans_table).split()))
    sides, x_y = inp[0:2], inp[2:4]

    board = [[0] * x_y[0]] * x_y[1]
    moves = ((-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1))

