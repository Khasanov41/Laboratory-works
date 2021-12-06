"""
Задача 1 из informatics.msk.ru
Определить можно ли с использованием только операций «прибавить 3» и «прибавить 5»
получить из числа 1 число N (N - натуральное, не превышает 200. Разумеется, само
число 1 получить можно, просто не применяя никаких операций.
Входные данные
	Вводится число N
Выходные данные
	Выведите слово YES, если число N можно получить из числа 1, или NO - в противном случае.
"""
from functools import lru_cache


@lru_cache(None)
def func(n, cur=1):
	if cur > n:
		return False
	elif cur == n:
		return True
	else:
		return any((func(n, cur+3), func(n, cur+5)))


if __name__ == "__main__":
	num = input("Enter N: ")
	if func(int(int(num))):
		print("YES")
	else:
		print("NO")
