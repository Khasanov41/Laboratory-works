from random import randint

from sorts import *


def gen_rand_sequence(length):
    return [randint(0, 9999) for _ in range(length)]


def gen_sorted_sequence(stop, start=0, step=1):
    return [i for i in range(start, stop, step)]


def check(sequence):
    for i in range(1, len(sequence)):
        if sequence[i-1] > sequence[i]:
            return False
    return True


def make_table(array):
    """
    Creates a table based on a two-dimensional array with string data.
    Each row of the array is a row of the table. The first line is the title.
    All array strings must be of the same length (they can be complemented with empty strings "").

    :param list | tuple array: Two-dimensional array with string data
    :return string: String in the form of a table.
    """
    size = (len(array), len(array[0]))
    # Getting the maximum width of each column.
    width = [0 for _ in range(len(array[0]))]
    for col in range(size[1]):
        for row in range(size[0]):
            width[col] = max(width[col], len(array[row][col])+2)
    # Header separator.
    sep = '+'+'-'*(sum(width)+len(width)-1)+'+\n'

    # Adds a table header.
    table = sep
    for col in range(size[1]):
        table += "|"+array[0][col].center(width[col])
    else:
        table += "|\n"+sep

    # Adds the body of the table.
    for row in range(1, size[0]):
        for col in range(size[1]):
            table += "|"+array[row][col].center(width[col])
        table += "|\n"
    else:
        table += sep

    return table


def write_out(name, d):
    with open(name, "w") as file:
        file.write(d)


if __name__ == "__main__":
    seq_len = input("Введите число N: ")

    if not seq_len.isdigit():
        raise TypeError("Пожалуйста, вводите целое число.")
    else:
        seq_len = int(seq_len)
    print("Ведётся расчёт данных. Пожалуйста, подождите...")

    sort_seq = gen_sorted_sequence(seq_len)
    # assert check(sort_seq)
    rev_seq = list(reversed(sort_seq))
    # assert not check(rev_seq)
    rand_seq = gen_rand_sequence(seq_len)
    method0 = bubble_sort(sort_seq, rand_seq, rev_seq)
    # assert check(method0[0][0]) and check(method0[0][1]) and check(method0[0][2])
    method1 = selection_sort(sort_seq, rand_seq, rev_seq)
    # assert check(method1[0][0]) and check(method1[0][1]) and check(method1[0][2])
    method2 = nr_quick_sort(sort_seq, rand_seq, rev_seq)
    # assert check(method2[0][0]) and check(method2[0][1]) and check(method2[0][2])
    method3 = stand_sort(sort_seq, rand_seq, rev_seq)
    # assert check(method3[0][0]) and check(method3[0][1]) and check(method3[0][2])

    data = [("Метод", "Отсортированная", "Случайная", "Отсортированная в обратном порядке")]
    methods_name = ["Метод пузырька", "Сортировка выбором", "Быстрая сортировка", "Встроенная"]
    count = 0
    for method in method0, method1, method2, method3:
        line = [methods_name[count]]
        for t in method[1]:
            line.append(str(f"{t:.3f}"))
        data.append(line)
        count += 1

    out = make_table(data)
    write_out("output.txt", out)
    print("Готово! Результат записан в output.txt.")
