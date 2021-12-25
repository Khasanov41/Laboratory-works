import os
from contextlib import contextmanager


def split_tape(key, buffer, limit=None, sep=None):
	"""
	Read tape and generate segments with max available size.
	If the limit is reached, the separator is returned.

	:param int key: Key of tape.
	:param sep: Separator.
	:param int limit: The number of items between separators.
	:param int buffer: Max items that can be stored in RAM.
	:return list: Segment from tape or separator if limit is reached.
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
				yield [sep]
			if len(segment) == buffer:
				yield segment
				segment.clear()
	if len(segment) != 0:
		yield segment


@contextmanager
def tapes(tape_num, sqc_len, sqc_range=(0, 999)):
	"""
	Creates files in the form of 0.tape, 1.tape, ..., num.tape in ./tapes folder, where 0, 1, ..., num are keys.
	A random sequence of a given length is generated in a tape with a key of 0.
	You can quickly get the environment for external sorting.
	After work, all files are deleted, leaving the file with the result.

	Warning! All functions from this module work correctly only in the context of this one.

	:param tuple | list sqc_range: A range of numbers to generate a random sequence.
	:param int sqc_len:	The length of the generated sequence.
	:param int tape_num: The number of files to be created.
	:return list: The key to the file where the result will be written.
	"""
	from random import randint
	if not os.path.exists(_dir):
		os.mkdir(_dir)
	try:
		with open(_dir + "0.tape", 'w') as source:  # Creating source tape.
			for _ in range(sqc_len):
				source.write(str(randint(*sqc_range)) + "\n")
		for key in range(1, tape_num):  			# Creating empty tapes.
			open(_dir + str(key)+".tape", 'w').close()
		yield ["result"]
	finally:
		for key in range(tape_num):
			try:
				os.remove(_dir+str(key)+'.tape')
			except OSError as er:
				print(f"Error deleting the {key}'.tape':\n{er}\nPlease delete it manually.")


def chek_tape(key):
	"""
	Checks if the tape is empty.

	:param int key: Key of tape to check.
	:return: True, if not empty, otherwise False.
	"""
	return os.path.getsize(_dir + str(key) + ".tape")


def clear_tape(key):
	try:
		open(_dir+str(key)+'.tape', 'w').close()
	except OSError as err:
		print(f"Can't clear {key}.tape:\n{err}")


def write_seg(key, segment, unload=False):
	"""
	Writes a sequence to tape.
	:param int key: Key of tape to write.
	:param list | tuple segment: Sequence to write.
	:param bool unload: Clear original list if it's True.
	:return: True, if the recording was successful, otherwise False.
	"""
	try:
		with open(_dir + str(key) + '.tape', 'a') as tape:
			for e in segment:
				tape.write(str(e) + "\n")
		if unload:
			segment.clear()
		return True
	except (OSError, TypeError):
		return False


def print_tape(key):
	with open(_dir+str(key)+'.tape') as t:
		txt = t.read()
		txt = txt.split('\n')
		print(*txt)


_dir = os.path.join("tapes/")
