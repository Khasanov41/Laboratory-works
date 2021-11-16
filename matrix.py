from random import randint


def rand_matrix(n,m): # функция генерации случайной матрицы n-m
	if n == 0 or m == 0:
		print("Ошибка: неверные размеры матрицы!")
	else:
		return [[randint(0,9) for j in range(m)] for i in range(n)]


def mult_matrix(A,B): # функция вычисления произведение двух матриц
	size_of_left = len(A), len(A[0]) 
	size_of_right = len(B), len(B[0])
	if size_of_left[1] == size_of_right[0]:
		# Новая матрица с высотой левой матрицы, а шириной правой
		C = [[0 for i in range(size_of_right[1])] for j in range(size_of_left[0])]
		
		for i in range(size_of_left[0]):
			for j in range(size_of_right[1]):
				for k in range(size_of_left[1]):
					C[i][j] += A[i][k]*B[k][j]
	else:
		print('Ошибка: неверные размеры мариц!')
	return C


def dif_matrix(A, B, dif=False):
	"""
	Если dif = True, то возврящает разность матриц, иначе - сумму.
	"""
	# Коэфициент, в зависимости от которого
	# на выходе получим ли разность, либо сумму матриц.
	k = -1 if dif else 1
	
	# Размеры исходных матриц.
	size_of_left = len(A), len(A[0]) 
	size_of_right = len(B), len(B[0])
	
	if size_of_left[0] == size_of_right[0] and size_of_left[1] == size_of_right[1]:
		C = [[0 for i in range(size_of_left[1])] for j in range(size_of_left[0])]
		for i in range(size_of_left[0]):
			for j in range(size_of_left[1]):
				C[i][j] = A[i][j] + B[i][j] * k
		return C
	else:
		print('Ошибка: неверные размеры мариц!')

def show_matrix(A):
	# Находим наибольшую длинну элемента матрицы.
	count = 0
	for i in A:
		count = max(len(str(max(i))), count)	
	
	for i in range(len(A)):
		for j in A[i]:
			print("%s%s" %(' '*(count-len(str(j))), str(j)), end=" ")
		print()	# Переход на следующую строку.

