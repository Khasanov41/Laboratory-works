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
