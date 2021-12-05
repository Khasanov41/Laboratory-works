from functools import lru_cache


from core import write_out, get_input


@lru_cache(None)
def P(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n >= 2:
        return ((2*n - 1) * x * P(n-1, x) - (n-1)*P(n-2, x)) / n


if __name__ == "__main__":
	n, x = get_input("Enter n and x: ")
	n, x = int(n), float(x)
	results = [P(i, x) for i in range(n + 1)]
	out = " ".join(map(str, results))
	write_out(out)
