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
    time_start = time()
    output = function(*args)
    time_stop = time() - time_start

    return output, time_stop


def get_formatted_output(sorted_seq, rand_seq, reversed_seq):
    titles = ("Метод", "Отсортированная",	"Случайная", "Отсортированная в обратном порядке")
    methods = ("Метод пузырька", "Сортировка выбором", "Быстрая сортировака", "Встроенная")
    width = (max((len(i) for i in methods))+2, len(titles[1])+2, len(titles[2])+2, len(titles[3])+2)
    line = "+"+(width[0]+1)*"-"+(width[1]+1)*"-"+(width[2]+1)*"-"+width[3]*"-"+"+"+'\n'
    result = line[:]+"|"
    for i in range(4):
        result += titles[i].center(width[i])+"|"
    result += "\n"+line
    for i in range(4):
        result += "|"+methods[i].center(width[0])+"|"
        result += sorted_seq[i].center(width[1])+"|"
        result += rand_seq[i].center(width[2])+"|"
        result += reversed_seq[i].center(width[3])+"|\n"
    result += line
    print(result)


if __name__ == "__main__":
    sequence_length = input("Введите число N: ")

    if not sequence_length.isdigit():
        raise TypeError("Please enter an integer.")
    else:
        sequence_length = int(sequence_length)

    sorted_sequence = gen_sorted_sequence(sequence_length)
    assert check(sorted_sequence)

    reversed_sequence = list(reversed(sorted_sequence))
    assert not check(reversed_sequence)

    rand_sequence = gen_rand_sequence(sequence_length)

    method1 = (stopwatch(bubble_sort, sorted_sequence),
               stopwatch(bubble_sort, rand_sequence),
               stopwatch(bubble_sort, reversed_sequence),)
    assert check(method1[0][0]) and check(method1[1][0]) and check(method1[2][0])

    method2 = (stopwatch(selection_sort, sorted_sequence),
               stopwatch(selection_sort, rand_sequence),
               stopwatch(selection_sort, reversed_sequence),)
    assert check(method2[0][0]) and check(method2[1][0]) and check(method2[2][0])

    method3 = (stopwatch(quick_sort, reversed_sequence),
               stopwatch(quick_sort, rand_sequence),
               stopwatch(quick_sort, reversed_sequence),)
    assert check(method3[0][0]) and check(method3[1][0]) and check(method3[2][0])

    method4 = (stopwatch(sorted, sorted_sequence),
               stopwatch(sorted, rand_sequence),
               stopwatch(sorted, reversed_sequence),)
    assert check(method4[0][0]) and check(method4[1][0]) and check(method4[2][0])

    sorted_sequence_time = (f"{method1[0][1]:.2f}", f"{method2[0][1]:.2f}", f"{method3[0][1]:.2f}",
                            f"{method4[0][1]:.2f}")
    rand_sequence_time = (f"{method1[1][1]:.2f}", f"{method2[1][1]:.2f}", f"{method3[1][1]:.2f}",
                          f"{method4[1][1]:.2f}")
    reversed_sequence_time = (f"{method1[0][1]:.2f}", f"{method2[0][1]:.2f}", f"{method3[0][1]:.2f}",
                              f"{method4[0][1]:.2f}")

    print(method1[2][1])
