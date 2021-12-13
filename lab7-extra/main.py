"""
main.py

Находит маршрут обхода конем шахматной доски, заданных размеров, из заданного начального положения коня.
Входные данные (файл input.txt):
    M, N - размеры шахматной доски.
    X, Y - начальные координаты расположения коня.
Выходные данные (файл output.txt):
    Таблица с номером хода в каждой ячейки поля, если маршрут существует
    и "Маршрут не существует" в противном случае.
Пример входных данных:
    M=5 N=5 X=1 Y=1

(c) Хасанов Ислам, КЭ-101
GitHub: https://github.com/Khasanov41/Laboratory-works.git
"""
import core


if __name__ == "__main__":
    inp = core.read_input()  # Use "M=10, N=10, X=10, Y=10" for test.

    # Parsing input data.
    trans_table = str.maketrans({'M': '', 'N': '', 'X': '', 'Y': '', ',': '', '=': ''})
    inp = tuple(map(int, inp.translate(trans_table).split()))
    sides, position = inp[0:2], inp[2:4]

    position = core.convert_pos(position, sides)
    board = [[0] * sides[0] for _ in range(sides[1])]
    horse_moves = ((-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1))

    route = core.take_path(board, position, sides, horse_moves)
    table = "Маршрут не существует" if route is None else core.make_table(route)
    core.write_output(table)
