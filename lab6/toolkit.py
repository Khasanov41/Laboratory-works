"""
Набор функций, необходимых для программ шестой лабораторной работы.

(c) Хасанов Ислам, КЭ-101
"""
from os import listdir
from math import ceil, floor
from time import time, strftime, localtime
from contextlib import contextmanager


@contextmanager
def stopwatch(output=None):
    """
    Outputs the date and execution time of the program.

    :param output: The path to the output file.
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


def get_points(x, y, radius):
    """
    Searches and counts points with integer
    coordinates inside a circle.

    :param x: The abscissa of the circle center (float)
    :param y: The ordinate of the circle center (float)
    :param radius: Radius of the circle (float)
    :return count: The number of points (int)
    """
    borders = {'left': ceil(x - radius), 'top': floor(y + radius),
               'right': floor(x + radius), 'bottom': ceil(y - radius)}

    count = 0
    for x in range(borders['left'], borders['right'] + 1):
        for y in range(borders['bottom'], borders['top'] + 1):
            if (x - x)**2 + (y - y)**2 <= radius**2:
                count += 1
    return count


def get_txt_files_from_current_dir():
    """
    :return: List of .txt files
    """
    return [file for file in listdir(path='.') if file.endswith('.txt')]


def find_input_data(files):
    """
    Searches among files input.txt and returns its content.

    :param files: List of .txt files
    :return data or None: String data if input.txt contains anything
    """
    if "input.txt" in files:
        with open(r"input.txt", 'r') as input_file:
            data = input_file.read()
            return data
    else:
        return None


def write_to_output(data, mode='w'):
    """
    Writes input data into the output.txt.

    :param mode: Give 'a' to add data without rewriting
    :param data: String data
    """
    with open(r"output.txt", mode) as output_file:
        output_file.write(data+'\n')


def get_prime_numbers(upper_bound):
    """
    One of the implementations of the sieve of Eratosthenes.
    Source: https://pythonist.ru/resheto-eratosfena/

    :param upper_bound: Integer
    :return prime_numbers: List of prime numbers
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

    :param elements: Iterable object with integer elements
    :return multi: Integer
    """
    multi = 1
    for element in elements:
        multi *= element
    return multi
