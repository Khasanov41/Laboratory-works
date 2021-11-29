def bubble_sort(sequence, reverse=False):
    """
    Simple exchange sorting.

    :param bool reverse: Sorting mode. False - ascending order, True - descending order.
    :param list sequence:
    :return list sorted_sequence:
    """
    sorted_sequence = sequence.copy()

    for i in range(len(sorted_sequence)-1):
        for j in range(len(sorted_sequence)-1, i, -1):
            if sorted_sequence[j-1] > sorted_sequence[j] and not reverse:
                sorted_sequence[j-1], sorted_sequence[j] = sorted_sequence[j], sorted_sequence[j-1]
            elif sorted_sequence[j-1] < sorted_sequence[j] and reverse:
                sorted_sequence[j-1], sorted_sequence[j] = sorted_sequence[j], sorted_sequence[j-1]

    return sorted_sequence


def selection_sort(sequence, reverse=False):
    """
    Simple selection sorting.

    :param bool reverse: Sorting mode. False - ascending order, True - descending order.
    :param list sequence:
    :return list sorted_sequence:
    """
    sequence = sequence.copy()
    sorted_sequence = []

    while len(sequence) != 0:
        minimal = min(sequence) if not reverse else max(sequence)
        sequence.remove(minimal)
        sorted_sequence.append(minimal)

    return sorted_sequence


def quick_sort(sequence, reverse=False):
    """
    Simple quick sorting.

    :param list sequence:
    :param bool reverse: Sorting mode. False - ascending order, True - descending order.
    :return list: Sorted sequence.
    """
    if len(sequence) <= 1:
        return sequence

    key = sequence[len(sequence)//2]
    left = [elem for elem in sequence if elem < key]
    middle = [key] * sequence.count(key)
    right = [elem for elem in sequence if elem > key]

    if reverse:
        left, right = right, left

    return quick_sort(left, reverse) + middle + quick_sort(right, reverse)
