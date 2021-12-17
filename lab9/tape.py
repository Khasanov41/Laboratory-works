import os, os.path
from contextlib import contextmanager


@contextmanager
def tapes(number):
	



def gen_source(leng, start=0, stop=999):
	from random import randint

	try:
		if not os.path.exists(dir):
			os.mkdir(dir)
		source = open(dir + "0.tape", 'w')
		source.write(" ".join(str(randint(start, stop)) for _ in range(leng)))
		source.write("\n")
		return 0
	except OSError:
		print("Error: Failed to create a directory with the source!")
		return 1
	finally:
		source.close()

def gen_tape(number):
	try:
		print(dir)
		for i in range(number):
			
		#pass
	except OSError:
		print("Error: Failed to create a directory with the source!")
		return 1


def read_tape(size, files):
	pass


_dir = os.path.join("tapes/")


if __name__ == "__main__":
	gen_tape(10)
	gen_source(10)
