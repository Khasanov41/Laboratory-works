"""
Набор функций, необходимых для программ шестой лабораторной работы.

(c) Хасанов Ислам, КЭ-101
"""
from os import listdir


def get_txt_files_from_current_dir():
    return [file for file in listdir(path='.') if file.endswith('.txt')]


def find_input_data(files):
    """
    Searches among files input.txt and returns its content.

    :param files: list of .txt files
    :return data or None: string data if input.txt contains anything
    """
    if "input.txt" in files:
        with open(r"input.txt", 'r') as input_file:
            data = input_file.readline()
            return data
    else:
        return None


def write_to_output(data):
    """
    Writes input data into the output.txt.

    :param data: string data
    """
    with open(r"output.txt", 'w') as output_file:
        output_file.write(data+'\n')


def get_prime_numbers(upper_bound):
    """
    One of the implementations of the sieve of Eratosthenes.
    Source: https://pythonist.ru/resheto-eratosfena/

    :param upper_bound: integer
    :return prime_numbers: list of prime numbers
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

    :param elements: iterable object with integer elements
    :return multi: integer
    """
    multi = 1
    for element in elements:
        multi *= element
    return multi