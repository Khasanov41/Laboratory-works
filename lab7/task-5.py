"""
Задача 4: Вычисление биномиальных коэффициентов
"""
from core import read_input


def digits(string, number=0):
	if string == "." or string == '':
		return number
	if string[0].isdigit():
		number += 1
	return digits(string[1:], number)


if __name__ == "__main__":
	print(digits(read_input()))
