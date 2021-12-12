from sorts import *
from support import *


if __name__ == "__main__":
    seq_len = input("Введите число N: ")

    while not seq_len.isdigit():
        print("Пожалуйста, вводите целое число.")
        seq_len = input("Введите число N: ")
    else:
        seq_len = int(seq_len)
    if seq_len > 1000:
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
