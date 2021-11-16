"""
task-3.py
Програма анализирует рабочий каталог на наличие input.txt,
если файл найден считывает из него число N.
Выведит в файл output.txt все простые числа от 1 до N.
Если файл не найден, то выведит соответствующее сообщение.

(c) Хасанов Ислам, КЭ-101
"""
from toolkit import get_txt_files_from_current_dir, find_input_data, get_prime_numbers, write_to_output


if __name__ == "__main__":
    text_files = get_txt_files_from_current_dir()
    input_data = find_input_data(text_files).strip()

    if input_data.isdigit():
        prime_numbers = get_prime_numbers(int(input_data))
        write_to_output(" ".join([str(i) for i in prime_numbers]))
    else:
        print("Файл с входными данными не обнаружен")
