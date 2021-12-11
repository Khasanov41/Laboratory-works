"""
!!! BUG WITH COORDINATES !!!
"""
import core


if __name__ == "__main__":
    inp = "M=10, N=10, X=9, Y=9"    # core.read_input()

    # Parsing input data.
    trans_table = str.maketrans({'M': '', 'N': '', 'X': '', 'Y': '', ',': '', '=': ''})
    inp = tuple(map(int, inp.translate(trans_table).split()))
    sides, position = inp[0:2], inp[2:4]

    board = [[0] * sides[0] for _ in range(sides[1])]
    horse_moves = ((-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1))

    path = core.take_path(board, position, sides, horse_moves)
    result = core.get_output(path)
    print(result)
