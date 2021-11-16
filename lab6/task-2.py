"""
task-2.py
Программа получает список файлов в текущей директории,
определяет присутствует ли в директории файл input.txt.
Если файл input.txt имеется в текущей директории, то
программа считывает из input.txt число и выводит в файл output.txt:
- само число,
- количество цифр в числе,
- сумму цифр в числе,
- произведение цифр в числе.
Если файл input.txt не обнаружен в рабочем каталоге, то
выдаётся соответствующее сообщение.

(c) Хасанов Ислам, КЭ-101
"""
from os import listdir


def get_txt_files_from_current_dir():
    return [file for file in listdir(path='.') if file.endswith('.txt')]


def find_input_data(files):
    if "input.txt" in files:
        with open(r"input.txt", 'r') as input_file:
            return input_file.readline()
    else:
        return None


def multiply_elements(elements):
    multi = 1
    for element in elements:
        multi *= element
    return multi


def get_formatted_output(number):
    digits = list(map(int, [i for i in number]))
    sum_of_digits = sum(digits)
    multi_of_digits = multiply_elements(digits)
    return f"Число: {number}\n" \
           f"Количество цифр: {len(number)}\n" \
           f"Сумма цифр: {sum_of_digits}\n" \
           f"Произведение цифр: {multi_of_digits}\n"


if __name__ == "__main__":
    text_files = get_txt_files_from_current_dir()
    input_data = find_input_data(text_files).rstrip()
    if input_data.isdigit():
        output = get_formatted_output(input_data)
        with open(r"output.txt", 'w') as output_file:
            output_file.write(output)
    else:
        print("Файл с входными данными не обнаружен")
