"""
Набор функций, необходимых для программ шестой лабораторной работы.

P.S.: Если честно, концепция свалки функций под названием 'toolkit' мне
не особо нравится, но и плодить модули для каждой задачи тоже не хочется.

(c) Хасанов Ислам, КЭ-101
"""
from os import listdir
from math import ceil, floor
from time import time, strftime, localtime
from contextlib import contextmanager


def PrintRectangle(a, b, file):
    """
    Prints a rectangle of characters '*'
    with sides a and b to the file.

    :param int a: Width of rectangle.
    :param int b: High of rectangle.
    :param string file: Path to output.
    :return None:
    """
    if a > 0 and b > 0:
        rectangle = a * '* ' + '\n'
        for _ in range(b - 2):
            rectangle += f"*{(a*2-3)*' '}*\n"
        rectangle += a * '* '
    else:
        rectangle = '**\n**'
    with open(file, 'w') as output:
        output.write(rectangle)


def PrintSquare(a, file):
    """
    Prints a square of
    characters * with side a to the file.

    :param int a: Side of square.
    :param string file: Path to output.
    :return None:
    """
    if a > 0:
        square = a * '* ' + '\n'
        for _ in range(a-2):
            square += f"*{(a*2-3)*' '}*\n"
        square += a * '* '
    else:
        square = '**\n**'
    with open(file, 'w') as output:
        output.write(square)


@contextmanager
def stopwatch(output=None):
    """
    Outputs the date and execution time of the program.

    :param string output: The path to the output file.
            If not specified, it outputs to the stdout.
    """
    try:
        date = strftime("%d.%m.%Y %H:%M", localtime())
        if output is None:
            print(date)
        else:
            with open(output, 'w') as output_file:
                output_file.write(date+"\n")

        time_start = time()
        yield time_start
    finally:
        finish = time() - time_start

        if output is None:
            print(finish)
        else:
            with open(output, 'a') as output_file:
                output_file.write(str(finish)+"\n")


def get_points(x_center, y_center, radius):
    """
    Searches and counts points with integer
    coordinates inside a circle.

    :param float x_center: The abscissa of the circle center.
    :param float y_center: The ordinate of the circle center.
    :param float radius: Radius of the circle.
    :return int count: The number of points.
    """
    # The area of points that need to be checked.
    shape = {'left': ceil(x_center - radius), 'top': floor(y_center + radius),
             'right': floor(x_center + radius), 'bottom': ceil(y_center - radius)}

    count = 0
    for x in range(shape['left'], shape['right'] + 1):
        for y in range(shape['bottom'], shape['top'] + 1):
            # Checking the point with the x and y coordinates for entering the area of the circle.
            if (x - x_center)**2 + (y - y_center)**2 <= radius**2:
                count += 1
    return count


def get_txt_files_from_current_dir():
    """
    Returns list of .txt files.

    :return list[string]:
    """
    return [file for file in listdir(path='.') if file.endswith('.txt')]


def find_input_data(files):
    """
    Searches among files input.txt and returns its content.

    :param list[string] | string files: List of .txt files
    :return data | None: String data if input.txt contains anything.
    """
    if "input.txt" in files:
        with open(r"input.txt", 'r') as input_file:
            data = input_file.read()
            return data
    else:
        return None


def write_to_output(data, mode='w', newline=True):
    """
    Writes input data into the output.txt.

    :param bool newline: Adds '\n' if it's True.
    :param string mode: Give 'a' to add data without rewriting
    :param string data: String data
    """
    with open(r"output.txt", mode) as output_file:
        output_file.write(data+'\n' if newline else data)


def get_prime_numbers(upper_bound):
    """
    One of the implementations of the sieve of Eratosthenes.
    Source: <https://pythonist.ru/resheto-eratosfena/>

    :param int upper_bound:
    :return list[int] prime_numbers: List of prime numbers
    """
    sieve = set(range(2, upper_bound + 1))
    prime_numbers = []
    while sieve:
        prime = min(sieve)
        prime_numbers.append(prime)
        sieve -= set(range(prime, upper_bound + 1, prime))
    return prime_numbers


def multiply_elements(elements):
    """
    Multiplies the elements of the iterable object.

    :param list[int] elements:
    :return int multi:
    """
    multi = 1
    for element in elements:
        multi *= element
    return multi
