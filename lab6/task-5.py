import numpy as np


from toolkit import write_to_output, find_input_data


def convert_matrix_to_str(matrix):
    # Находим наибольшую длинну элемента матрицы.
    max_len = 0
    for i in range(len(matrix)):
        for j in matrix[i]:
            max_len = max(max_len, len(str(j)))

    string_matrix = ""
    for i in range(len(matrix)):
        for j in matrix[i]:
            string_matrix += f"{str(j)}{' '* (max_len - len(str(j)))} "
        string_matrix += "\n"

    return string_matrix


def div_by_line(matrix):
    new_matrix = np.array(matrix, float)
    for i in range(len(matrix)):
        line = matrix.take(i, axis=0)
        line = np.array(line, float) / max(np.setdiff1d(line, 0))
        new_matrix[i] = line
    return new_matrix


def format_output(a, b, c):
    output = "Матрица A:\n"+a+"Матрица B:\n"+b+"Матрица A*B:\n"+c
    return output


if __name__ == "__main__":
    input_data = tuple(find_input_data('input.txt').split('\n'))

    N, M = map(int, input_data[0].split())
    K = int(input_data[1].replace('Пусть K = ', ''))

    matrix_A = np.random.randint(-100, 100, (N, M))
    str_A = convert_matrix_to_str(matrix_A)

    matrix_A = div_by_line(matrix_A)

    matrix_B = np.random.randint(-100, 100, (M, K))
    str_B = convert_matrix_to_str(matrix_B)

    matrix_C = matrix_A.dot(matrix_B)
    str_C = convert_matrix_to_str(matrix_C)

    formatted_output = format_output(str_A, str_B, str_C)
    write_to_output(formatted_output, newline=False)
