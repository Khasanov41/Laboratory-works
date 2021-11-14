def mod_div(x, y):
    """Вычисление r = x % y, d = x // y."""
    r, b, q = abs(x), abs(y), 0
    # k = -1 if x * y < 0 else 1
    while r >= b:
        r -= b
        q += 1
    if x > 0 and y > 0:
        return r, q
    elif x < 0 and x < 0:
        return r, q + 1
    elif x < 0:
        return r, (q + 1) * -1
    elif y < 0:
        return r, q * -1


def degree(base, deg):
    res = 1
    for _ in range(deg):
        res *= base
    return res


if __name__ == '__main__':
    print("Вычисление r = x % y, d = x // y.")
    x1, y1 = map(int, (input('Делимое: '), input('Делитель: ')))
    result = mod_div(x1, y1)
    print(f"{x1} % {y1} = {result[0]}")
    print(f"{x1} // {y1} = {result[1]}")

    print("Вычисление степени.")
    x1, y1 = map(int, (input('Основание: '), input('Степень: ')))
    result = degree(x1, y1)
    print(f"{x1}**{y1} = {result}")
