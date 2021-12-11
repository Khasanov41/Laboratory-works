def read_input(file="input.txt"):
    with open(file, "r") as file:
        data = file.read().strip()
        return data


def check_move(field, pos, shape):
    return (0 <= pos[0] < shape[0]) \
            and (0 <= pos[1] < shape[1]) \
            and (field[pos[1]][pos[0]] == 0)


def check_field(field):
    for row in field:
        if 0 in row:
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
    rate = 0
    for move in moves:
        next_move = pos[0]+move[0], pos[1]+move[1]
        if check_move(field, next_move, shape):
            cur_rate = count_move(field, next_move, shape, moves)
            if cur_rate > rate:
                next_pos = next_move
                rate = cur_rate
        else:
            continue
    if rate == 0 and check_field(field):
        return None
    elif rate == 0:
        return field
    else:
        return take_path(field, next_pos, shape, moves, step+1)



if __name__ == "__main__":
    sides = (8, 8)
    position = (4, 4)
    board = [[0] * sides[0]] * sides[1]
    horse_moves = ((-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1))
    # print(count_move(board, position, sides, horse_moves))
