"""
Напишите программу, которая решает головоломку (Ханойские башни)
для данного числа дисков n печатает последовательность перекладываний в формате a b c,
где a — номер перекладываемого диска, b — номер стержня с которого снимается данный диск,
c — номер стержня на который надевается данный диск.

Например, строка 1 2 3 означает перемещение диска номер 1 со стержня 2 на стержень 3.
В одной строке печатается одна команда. Диски пронумерованы числами от 1 до n в порядке возрастания диаметров.
Входные данные
	Вводится натуральное число n.
Выходные данные
	Программа должна вывести минимальный (по количеству произведенных операций)
	способ перекладывания пирамидки из данного числа дисков.

"""


def hanoi(h, f, t, c):
	if h >= 1:
		hanoi(h-1, f, c, t)
		print(h, f, t)
		hanoi(h-1, c, t, f)


if __name__ == "__main__":
	inp = int(input("Enter N: "))
	hanoi(inp, "1", "3", "2")
