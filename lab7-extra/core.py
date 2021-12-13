def read_input(file="input.txt"):
    with open(file, "r") as txt:
        data = txt.read().strip()
        return data


def write_output(data, file="output.txt"):
    with open(file, 'w') as txt:
        txt.write(data + "\n")


def take_path(field, pos, shape, moves, step=1):
    """
    Recursively creates a matrix with the route of the chess board moves,
    by applying Warnsdorff's rule. If the chessboard cannot be filled
    with moves, then None is returned.

    :param list field: Two - dimensional matrix (board).
    :param list | tuple pos: The positions of the figure, with (1, 1) being the lower-left corner of the board.
    :param list | tuple shape: The width and height of the board.
    :param list | tuple moves: A set of moves of the figure.
    :param int step: The number of steps the figure has taken. Don't change manually!
    :return: None or two-dimensional matrix with figure's moves.
    """
    field[pos[1]][pos[0]] = str(step)  # Mark the cell with the current move number.
    next_pos = None
    rate = len(moves)  # The number of maximum possible moves from a given position.
    for move in moves:
        # Searches for the position with the lowest rate.
        next_move = pos[0]+move[0], pos[1]+move[1]
        if _check_move(field, next_move, shape):
            cur_rate = _count_move(field, next_move, shape, moves)
            if cur_rate < rate:
                next_pos = next_move
                rate = cur_rate
        else:
            continue
    if rate == len(moves) and not _check_field(field):
        return None  # Unable to find a route.
    elif rate == len(moves):
        return field  # Route found.
    else:
        # Search next move.
        return take_path(field, next_pos, shape, moves, step+1)


def make_table(data):
    """
    Creates a table based on a two-dimensional array with string data.
    Each row of the array is a row of the table. All array strings
    must be of the same length (they can be complemented with empty strings "").

    :param list | tuple data: Two-dimensional array with string data.
    :return: String in the form of a table.
    """
    size = (len(data), len(data[0]))
    # Getting the maximum width of each column.
    width = [0 for _ in range(len(data[0]))]
    for col in range(size[1]):
        for row in range(size[0]):
            width[col] = max(width[col], len(data[row][col])+2)
    # Header separator.
    sep = '+'+'-'*(sum(width)+len(width)-1)+'+\n'
    # Adds a table header.
    table = sep
    for col in range(size[1]):
        table += "|"+data[0][col].center(width[col])
    else:
        table += "|\n"+sep
    # Adds the body of the table.
    for row in range(1, size[0]):
        for col in range(size[1]):
            table += "|"+data[row][col].center(width[col])
        table += "|\n" + sep

    return table


def convert_pos(pos, shape):
    """
    Translates the position to the index of the matrix.

    :param tuple | list pos: Abscissa and ordinate.
    :param tuple | list shape: The width and height of the field.
    :return: The index of a two-dimensional matrix.
    """
    return pos[0]-1, shape[1]-pos[1]


def _check_move(field, pos, shape):
    return (0 <= pos[0] < shape[0]) \
            and (0 <= pos[1] < shape[1]) \
            and (field[pos[1]][pos[0]] == 0)


def _print_field(field):
    for row in field:
        print(row)
    print()


def _check_field(field):
    for row in field:
        if 0 in row or len(field) == 1:
            return False
    return True


def _count_move(field, pos, shape, moves):
    count = 0
    for move in moves:
        next_move = pos[0]+move[0], pos[1]+move[1]
        if _check_move(field, next_move, shape):
            count += 1
    return count


def _test_result(shape, moves):
    for x in range(shape[0]):
        for y in range(shape[1]):
            field = [[0] * shape[0] for _ in range(shape[1])]
            result = take_path(field, (x, y), shape, moves)
            if result is not None:
                print(x, y)
                _print_field(result)
