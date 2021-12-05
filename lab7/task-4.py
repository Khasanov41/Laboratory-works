from core import write_out, get_input


def func(n, m):
	if (m == 0 and 0 <= m <=n) or (m == n and 0 <= m <= n):
		return 1
	return func(n-1, m) + func(n-1, m-1)


if __name__ == "__main__":
	x, y = map(int, get_input("Enter n and m: "))

	write_out(str(func(x, y)))
