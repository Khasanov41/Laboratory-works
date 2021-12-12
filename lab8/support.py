from random import randint


def gen_rand_sequence(length):
    return [randint(0, 9999) for _ in range(length)]


def gen_sorted_sequence(stop, start=0, step=1):
    return [i for i in range(start, stop, step)]


def check(sequence):
    for i in range(1, len(sequence)):
        if sequence[i-1] > sequence[i]:
            return False
    return True


def make_table(array):
    """
    Creates a table based on a two-dimensional array with string data.
    Each row of the array is a row of the table. The first line is the title.
    All array strings must be of the same length (they can be complemented with empty strings "").

    :param list | tuple array: Two-dimensional array with string data
    :return string: String in the form of a table.
    """
    size = (len(array), len(array[0]))
    # Getting the maximum width of each column.
    width = [0 for _ in range(len(array[0]))]
    for col in range(size[1]):
        for row in range(size[0]):
            width[col] = max(width[col], len(array[row][col])+2)
    # Header separator.
    sep = '+'+'-'*(sum(width)+len(width)-1)+'+\n'

    # Adds a table header.
    table = sep
    for col in range(size[1]):
        table += "|"+array[0][col].center(width[col])
    else:
        table += "|\n"+sep

    # Adds the body of the table.
    for row in range(1, size[0]):
        for col in range(size[1]):
            table += "|"+array[row][col].center(width[col])
        table += "|\n"
    else:
        table += sep

    return table


def write_out(name, d):
    with open(name, "w") as file:
        file.write(d)
