"""
quad_equ.py

Вычисляет корни квадратного уравнения по заданным коэффициентам.
Выводит результат в следующей форме:
    - Если уравнение не имеет вещественных корней:
        Уравнение
        (<a>)*X^2+(<b>)*X+(<c>)=0
        Количество корней: < количество вещественных корней>
    - Если уравнение имеет вещественные корни:
        Уравнение
        (<a>)*X^2+(<b>)*X+(<c>)=0
        Количество корней: <количество вещественных корней>
        <1-й корень уравнения (меньший из двух корней)>
        <2-й корень уравнения>.

    Примичание: a, b, c имеют пять знаков после запятой.

(С) Хасанов Ислам, КЭ-101
"""


def get_roots(k1, k2, k3):
    discriminant = (lambda a1, b1, c1: b1 * b1 + 4 * a1 * c1)(k1, k2, k3)
    if k1 == 0:
        return -k3 / k2, -k3 / k2
    elif discriminant >= 0:
        return -k2 - discriminant ** 0.5, -k2 + discriminant ** 0.5
    else:
        return


def get_result(k1, k2, k3):
    roots = get_roots(k1, k2, k3)

    if roots is None:
        count = 0
    elif roots[0] == roots[1]:
        count = 1
    else:
        count = 2

    result = f"Уравнение\n" \
             f"({float(k1):.5f})*X^2+({float(k2):.5f})*X+({float(k3):.5f})=0\n" \
             f"Количество корней: {count}"

    if not count == 0:
        result += f"\n{roots[0]:.5f}"
        result += f"\n{roots[1]:.5f}"

    return result


if __name__ == '__main__':
    # Uncomment to get the tests
    # test_input = ((1, -7, 12), (1, 4, 4), (4, 0, -16), (0, 4, 5))
    # print(*(get_result(*test) for test in test_input), sep="\n")

    print("Введите коэффициенты уравнения через пробел. Например: 1 4 3")
    coefficients = input("Коэффициенты: ")

    a, b, c = map(float, coefficients.split())
    print(get_result(a, b, c))
