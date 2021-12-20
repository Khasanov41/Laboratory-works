import os
import os.path
from contextlib import contextmanager


def segments(source, limit):
	segment = []
	for line in open(source, 'r'):
		e = int(line.strip())
		segment.append(e)
		if len(segment) == limit:
			yield segment
			segment = []
	else:
		yield segment


@contextmanager
def tapes(number, seq_len, segment=(0, 999)):
	"""
	Генерирует ленты для работы внешней сортировки в папке ./tapes вида 0.tape, 1.tape, ..., <number>.tape.
	исходной последовательностью, которую необходимо отсортироват.
	После работы очищает директорию ./tapes и сохраняет результат в result.tape.
	Работа с лентами будет невозможна без вызова этой функции

	:param segment:
	:param seq_len:
	:param int number: Количество лент
	:return:
	"""
	from random import randint
	# from shutil import rmtree
	if not os.path.exists(_dir):
		os.mkdir(_dir)
	try:
		# Creating source tape
		with open(_dir + "0.tape", 'w') as source:
			for _ in range(seq_len):
				source.write(str(randint(*segment)) + "\n")
		yield _dir + "0.tape"
		# Creating empty tapes
		for i in range(1, number+1):
			with open(_dir + str(i)+".tape", 'w'):
				pass
	finally:
		print("Directory is deleted.")  # rmtree(_dir)


def write_seg(num, segment):
	with open(_dir+str(num)+'.tape', 'a') as tape:
		for e in segment:
			tape.write(str(e) + "\n")


_dir = os.path.join("tapes/")


if __name__ == "__main__":
	LIMIT = 3
	FILES = 5
	SEQ = 20
	# with tapes(FILES, SEQ) as file:
	# for seg in segments(file, LIMIT):
	# print(seg)
	seg = [1, 2, 3, 4, 5, 6, 7]
	write_seg(0, seg)
