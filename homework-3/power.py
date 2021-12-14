def Power(a, b):
    """
    Recursively calculates the exponentiation of a number.

    @param int a: The basis.
    @param int b: The degree.
    @return float | int: The base is raised to a degree.
    """
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b == -1:
        return 1 / a
    elif b < -1:
        return Power(a, -1) * Power(a, b+1)
    return Power(a, 1) * Power(a, b-1)


if __name__ == "__main__":
    while True:
        x, y = map(int, input().split())
        # print(Power(x, y))
        print(x**y)
