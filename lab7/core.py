def write_out(data):
	with open(r"output.txt", 'w') as txt:
		txt.write(data+"\n")


def get_input(message):
	data = input(message)
	data = list(data.split())
	return data


def read_input(file="input.txt"):
	with open(file, 'r') as txt:
		return txt.read().strip()
