import os
from contextlib import contextmanager


def split_tape(key, buffer, limit=None):
	"""
	Read tape and generate segments with max available size.

	:param int key: Key of tape.
	:param int limit: Number of elements to read from file.
	:param int buffer: Max element that can be stored in RAM.
	:return: Segment from tape or [None] if limit is reached.
	"""
	segment = []
	delivered = 0
	with open(_dir+str(key)+'.tape', 'r') as source:
		for e in source:
			segment.append(int(e.strip()))
			delivered += 1
			if delivered == limit and limit is not None:
				if len(segment) != 0:
					yield segment
					segment.clear()
					delivered = 0
				yield [None]
			if len(segment) == buffer:
				yield segment
				segment.clear()
		if len(segment) != 0:
			yield segment


@contextmanager
def tapes(num, sqc_len, segment=(0, 999)):
	"""
	Генерирует ленты для работы внешней сортировки в папке ./tapes вида 0.tape, 1.tape, ..., <number>.tape.
	исходной последовательностью, которую необходимо отсортироват.
	После работы очищает директорию ./tapes и сохраняет результат в result.tape.
	Работа с лентами будет невозможна без вызова этой функции

	!BUG: PermissionError while removing _dir.

	:param tuple | list segment:
	:param int sqc_len:
	:param int num: Количество лент
	:return:
	"""
	from random import randint
	if not os.path.exists(_dir):
		os.mkdir(_dir)
	try:
		with open(_dir + "0.tape", 'w') as source:  # Creating source tape.
			for _ in range(sqc_len):
				source.write(str(randint(*segment)) + "\n")
		for key in range(1, num):  # Creating empty tapes.
			open(_dir + str(key)+".tape", 'w').close()
		yield ["result"]
	finally:
		for key in range(num):
			try:
				os.remove(_dir+str(key)+'.tape')
			except OSError as er:
				print(f"Error deleting the {key}'.tape':\n{er}\nPlease delete it manually.")
		print("Done!")


def chek_tape(key):
	return os.path.getsize(_dir + str(key) + ".tape")


def clear_tape(key):
	try:
		open(_dir+str(key)+'.tape', 'w').close()
	except OSError as err:
		print(f"Can't clear {key}.tape:\n{err}")


def write_seg(num, segment):
	with open(_dir+str(num)+'.tape', 'a') as tape:
		for e in segment:
			tape.write(str(e) + "\n")


def read_tape(key):
	with open(_dir+str(key)+'.tape') as t:
		txt = t.read()
		txt = txt.split('\n')
		print(txt)


def test_read_write():
	pass


_dir = os.path.join("tapes/")


if __name__ == "__main__":
	a = split_tape(1, 2)
	for i in range(6):
		print(next(a))
