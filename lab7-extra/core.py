def read_input(file="input.txt"):
    with open(file, "r") as file:
        data = file.read().strip()
        return data


def get_output(data):
    """
    Creates a table based on a two-dimensional array with string data.
    Each row of the array is a row of the table. The first line is the title.
    All array strings must be of the same length (they can be complemented with empty strings "").

    :param list | tuple data: Two-dimensional array with string data
    :return string: String in the form of a table.
    """
    if data is None:
        return "Маршрут не существует"
    else:
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
            table += "|\n"
        else:
            table += sep

        return table


def check_move(field, pos, shape):
    return (0 <= pos[0] < shape[0]) \
            and (0 <= pos[1] < shape[1]) \
            and (field[pos[1]][pos[0]] == 0)


def print_field(field):
    for row in field:
        print(row)
    print()


def check_field(field):
    for row in field:
        if 0 in row or len(field) == 1:
            return False
    return True


def count_move(field, pos, shape, moves):
    count = 0
    for move in moves:
        next_move = pos[0]+move[0], pos[1]+move[1]
        if check_move(field, next_move, shape):
            count += 1
    return count


def take_path(field, pos, shape, moves, step=1):
    field[pos[1]][pos[0]] = step
    next_pos = None
    rate = 9
    for move in moves:
        next_move = pos[0]+move[0], pos[1]+move[1]
        if check_move(field, next_move, shape):
            cur_rate = count_move(field, next_move, shape, moves)
            if cur_rate < rate:
                next_pos = next_move
                rate = cur_rate
        else:
            continue
    if rate == 9 and not check_field(field):
        return None
    elif rate == 9:
        return field
    else:
        return take_path(field, next_pos, shape, moves, step+1)


def _test_result(shape, moves):
    for x in range(shape[0]):
        for y in range(shape[1]):
            field = [[0] * shape[0] for _ in range(shape[1])]
            result = take_path(field, (x, y), shape, moves)
            if result is not None:
                print(x, y)
                print_field(result)


if __name__ == "__main__":
    sides = (10, 10)
    horse_moves = ((-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1))
    _test_result(sides, horse_moves)
