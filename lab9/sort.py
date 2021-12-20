def merge_sort(*args):
    """
    Simple k-way merge sorting (generator).
    Warning: The original lists are cleared after merging!

    :param list | tuple args: Sorted lists to merge.
    :return: An element of merged list.
    """
    while any(args):  # while non empty list is existing
        args = [i for i in args if i]  # Delete empty lists
        mi, arr = args[0][0], args[0]
        # Finding minimal element from first elements of lists
        for arg in args:
            if arg[0] < mi:
                arr, mi = arg, arg[0]
        yield arr.pop(0)


def insert_sort(arr):
    """
    Simple insertion sort. It sorts the original list.

    :param list arr: Unsorted list
    """
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1], j = arr[j], j-1
        arr[j+1] = key


def test_merge_merge(args):
    from functools import reduce
    # Merge sorting done by standard Python tools.
    reference = sorted(reduce(lambda x, y: x + y, args))
    test = [i for i in merge_sort(*args)]
    assert test == reference, "Merge sort error!"


def test_insert_sort(arg):
    reference = sorted(arg)
    insert_sort(arg)
    assert reference == arg, "Insertion sort error!"


if __name__ == "__main__":
    test_set = [1, 3, 4, 6], [5, 9, 11, 12], [0, 0, 11, 66]
    test_set_1 = [1, 7, 4, 3, 2, 0, 9, 10, 33, 5]
    test_merge_merge(test_set)
    test_insert_sort(test_set_1)
