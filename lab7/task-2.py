from core import write_out, get_input


def div(x, y, s=0):
	if x >= y:
		s += 1
		return div(x - y, y, s)
	return s


if __name__ == "__main__":
	inp = get_input("Enter the divisible and the divisor separated by a space:\n")
	x, y = map(int, inp)
	out = f"div({x},{y})={div(x, y)}"
	write_out(out)
