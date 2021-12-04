from time import perf_counter


def timer(function):
    def wrapper(*args):
        times = []
        outputs = []
        for arg in args:
            time_start = perf_counter()
            outputs.append(function(arg))
            times.append(perf_counter()-time_start)
        return outputs, times
    return wrapper


@timer
def bubble_sort(sequence, reverse=False):
    """
    Simple exchange sorting.

    :param bool reverse: Sorting mode. False - ascending order, True - descending order.
    :param list sequence:
    :return list sorted_seq:
    """
    sorted_seq = sequence.copy()

    for i in range(len(sorted_seq)-1):
        for j in range(len(sorted_seq)-1, i, -1):
            if sorted_seq[j-1] > sorted_seq[j] and not reverse:
                sorted_seq[j-1], sorted_seq[j] = sorted_seq[j], sorted_seq[j-1]
            elif sorted_seq[j-1] < sorted_seq[j] and reverse:
                sorted_seq[j-1], sorted_seq[j] = sorted_seq[j], sorted_seq[j-1]

    return sorted_seq


@timer
def selection_sort(sequence, reverse=False):
    """
    Simple selection sorting.

    :param bool reverse: Sorting mode. False - ascending order, True - descending order.
    :param list sequence:
    :return list: sorted list
    """
    sorted_seq = sequence.copy()

    for i in range(len(sorted_seq)-1):
        cur, j = i, i + 1
        while j < len(sorted_seq):
            if sorted_seq[j] < sorted_seq[cur] and not reverse:
                cur = j
            elif sorted_seq[j] > sorted_seq[cur] and reverse:
                cur = j
            j += 1
        sorted_seq[i], sorted_seq[cur] = sorted_seq[cur], sorted_seq[i]
    return sorted_seq


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


@timer
def stand_sort(sequence):
    return list(reversed(sequence))


@timer
def nr_quick_sort(seq, rec=False):
    return quick_sort(seq, rec)
