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
from toolkit import get_txt_files_from_current_dir, find_input_data, write_to_output, multiply_elements


def get_formatted_output(number):
    """
    Formats the number according to the task.

    :param number: string
    :return: formatted string
    """
    digits = list(map(int, [i for i in number]))
    sum_of_digits = sum(digits)
    multi_of_digits = multiply_elements(digits)
    return f"Число: {number}\n" \
           f"Количество цифр: {len(number)}\n" \
           f"Сумма цифр: {sum_of_digits}\n" \
           f"Произведение цифр: {multi_of_digits}"


if __name__ == "__main__":
    text_files = get_txt_files_from_current_dir()
    input_data = find_input_data(text_files).strip()

    if input_data.isdigit():
        output = get_formatted_output(input_data)
        write_to_output(output)
    else:
        print("Файл с входными данными не обнаружен")
