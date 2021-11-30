from random import randint
from time import time

from sorts import *


def gen_rand_sequence(length):
    return [randint(0, 99999) for _ in range(length)]


def gen_sorted_sequence(stop, start=0, step=1):
    return [i for i in range(start, stop, step)]


def check(sequence):
    for i in range(1, len(sequence)):
        if sequence[i-1] > sequence[i]:
            return False
    return True


def stopwatch(function, *args):
    times = []
    outputs = []
    for arg in args:
        time_start = time()
        outputs.append(function(arg))
        times.append(time()-time_start)
    return outputs, times


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


if __name__ == "__main__":
    seq_len = input("Введите число N: ")

    if not seq_len.isdigit():
        raise TypeError("Пожалуйста, вводите целое число.")
    else:
        seq_len = int(seq_len)

    sort_seq = gen_sorted_sequence(seq_len)
    assert check(sort_seq)

    rev_seq = list(reversed(sort_seq))
    assert not check(rev_seq)

    rand_seq = gen_rand_sequence(seq_len)

    method1 = (stopwatch(bubble_sort, sort_seq),
               stopwatch(bubble_sort, rand_seq),
               stopwatch(bubble_sort, rev_seq),)
    assert check(method1[0][0]) and check(method1[1][0]) and check(method1[2][0])

    method2 = (stopwatch(selection_sort, sort_seq),
               stopwatch(selection_sort, rand_seq),
               stopwatch(selection_sort, rev_seq),)
    assert check(method2[0][0]) and check(method2[1][0]) and check(method2[2][0])

    method3 = (stopwatch(quick_sort, rev_seq),
               stopwatch(quick_sort, rand_seq),
               stopwatch(quick_sort, rev_seq),)
    assert check(method3[0][0]) and check(method3[1][0]) and check(method3[2][0])

    method4 = (stopwatch(sorted, sort_seq),
               stopwatch(sorted, rand_seq),
               stopwatch(sorted, rev_seq),)
    assert check(method4[0][0]) and check(method4[1][0]) and check(method4[2][0])

    sorted_sequence_time = (f"{method1[0][1]:.2f}", f"{method2[0][1]:.2f}", f"{method3[0][1]:.2f}",
                            f"{method4[0][1]:.2f}")
    rand_sequence_time = (f"{method1[1][1]:.2f}", f"{method2[1][1]:.2f}", f"{method3[1][1]:.2f}",
                          f"{method4[1][1]:.2f}")
    reversed_sequence_time = (f"{method1[0][1]:.2f}", f"{method2[0][1]:.2f}", f"{method3[0][1]:.2f}",
                              f"{method4[0][1]:.2f}")

    print(method1[2][1])
