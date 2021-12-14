"""
main.py
Вычисляет возведение числа в степень.

Ввод (STDIN):
    a - целое число, основание степени;
    b - целое числе, степень.
Вывод (STDOUT):
    a ** b = c, где c - это a возведённое в степень b.
Пример:
    2 3 -> 2 ** 3 = 8
    1 0 -> 1 ** 0 = 1
Примечание: Чтобы протестировать функцию Power, запустите power.py.

(c) Хасанов Ислам (КЭ-101)
"""

from power import Power


if __name__ == "__main__":
    text = "Calculating the power of a number"
    print("~" * len(text) + '\n' + text + "\n" + "~" * len(text) + "\n")
    base = input("Enter the base: ")
    while not base.isdigit():
        base = input("Please enter an integer: ")
    else:
        base = int(base)
    deg = input("Enter the degree: ")
    while not deg.isdigit():
        deg = input("Please enter an integer: ")
    else:
        deg = int(deg)
    print(f"\n{'-' * len(text)}\n{base} ** {deg} = {Power(base, deg)}")
