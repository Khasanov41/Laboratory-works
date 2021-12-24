def minimal(arg):
    """
    Finds the smallest element of the first elements of the input lists and returns it.
    This function can be used as a simple merge sort
    if the elements of the input lists are in non-decreasing order.

    Warning: This way modify original lists!
    *For better performance, there is a way to use bin tree (min-heap) instead of brut force.

    :param list arg: List of lists.
    :return: The minimum of the first items in the lists.
    """
    while any(arg):  # while there are non-empty lists.
        arg = [i for i in arg if i]  # Exclude empty lists.
        mi, arr = arg[0][0], arg[0]
        for i in arg:  # Finding minimum from first items in the lists.
            if i[0] < mi:
                arr, mi = i, i[0]
        yield arr.pop(0)


def test_minimal(arg):
    from functools import reduce
    # Merge sorting done by high-level Python tools.
    reference = sorted(reduce(lambda x, y: x + y, arg))
    # Merge sorting done by minimal function.
    arg = [sorted(i) for i in arg]
    test = [i for i in minimal(arg)]

    assert test == reference, f"Error in minimal function!\nReference:{reference}\nTest:{test}"


def insert_sort(arr):
    """
    Simple insertion sort. This way modify the original list.
    Warning: This way modifies the original list!

    :param list arr: Unsorted list.
    """
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1], j = arr[j], j-1
        arr[j+1] = key
    return arr


def test_insert_sort(arg):
    reference = sorted(arg)
    insert_sort(arg)
    assert reference == arg, "Insertion sort error!"


if __name__ == "__main__":
    test_sqc = [[124, 1493, 2844], [139, 390, 1, 111], [144, 450, 0]]
    test_minimal(test_sqc)
