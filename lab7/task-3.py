from core import write_out, get_input


def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)


if __name__ == "__main__":
	x, y = map(int, get_input("Enter a and b: "))
	out = f"НОД({x},{y})={gcd(x, y)}"
	write_out(out)
