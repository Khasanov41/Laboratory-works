from os import listdir


def get_txt_files_from_current_dir():
    return [file for file in listdir(path='.') if file.endswith('.txt')]


text_files = get_txt_files_from_current_dir()

if "input.txt" in text_files:
    with open(r"input.txt", 'r') as input_file:
        data = input_file.readline()

    digits = list(map(int, [i for i in data]))

    sum_of_digits = sum(digits)
    multi_of_digits = 1
    for digit in digits:
        multi_of_digits *= digit

    output = f"Число: {data}\n" \
             f"Количество цифр: {len(data)}\n" \
             f"Сумма цифр: {sum_of_digits}\n" \
             f"Произведение цифр: {multi_of_digits}"

    with open(r"output.txt", 'w') as output_file:
        output_file.write(output)

else:
    print("Файл с входными данными не обнаружен")
