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


def test_func(tests, func1, func2):
    """
    Tests the function by comparing it with a reference.

    :param tuple | list tests: Test set - arguments for the functions.
    :param func1: The function under test.
    :param func2: The reference function.
    """
    errors = [0, 0]  # Warnings, critical errors.

    for test in tests:
        print(f"Testing {func1.__name__}{test}", end="... ")
        try:
            if func1(*test) == func2(*test):
                print("Ok.")
            else:
                print(f"Warning! {func1(*test)} is not {func2(*test)}.")
                errors[0] += 1
        except:
            errors[1] += 1
            print("Critical error!")

    print(f"\n{'-' * 30}"
          f"Total {len(tests)} tests:"
          f"\n- {len(tests)-sum(errors)} successful"
          f"\n- {errors[0]} warnings"
          f"\n- {errors[1]} critical errors.")


if __name__ == "__main__":
    if input("Run a test? (y/n): ") in ('y', 'yes'):
        test_set = ((0, 1), (0, 22), (1, 0), (100, 0), (2, 99), (-1, 9), (1, -1), (10, -9), (0, -1), (-3, -3))
        test_func(test_set, Power, pow)
    else:
        print("Terminating...")
