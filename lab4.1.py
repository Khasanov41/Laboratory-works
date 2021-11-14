﻿"""
СПИСОК - это структура данных, которую вы можете использовать для хранения коллекции различных данных в одной переменной.
Список может быть записан в виде последовательности значений (элементов), разделенных запятыми, в квадратных скобках,
например, lst = [item1, item2]. Списки могут содержать элементы разных типов, но обычно все элементы в списке одного типа.
Списки, так же как и строки, поддерживают операции среза и обращения по индексу.
"""

squares = [1, 4, 9, 16, 25]  # Создание нового списка
print(squares)

# Выведите на экран подсписок [4, 9, 16].
print(squares[1:4])

""" 
Вы можете добавлять новые элементы в конец списка, используя метод append() и конкатенацию. 
В отличие от строк, списки являются изменяемым типом, то есть их содержимое можно изменить с помощью lst[index] = new_item 
"""

animals = ['elephant', 'lion', 'tiger', "giraffe"]  # Создание нового списка
print(animals)
animals += ["monkey", 'dog']  # Добавление новых элементов в список с помощью операции конкатенации
print(animals)
animals.append("dino")  # Добавление нового элемента с помощью метода append()
print(animals)

# Замените элемент 'dino' на 'dinosaur'
animals[len(animals) - 1] = "dinosaur"
print(animals)

""" 
Также возможно присвоение срезов, что может изменить размер списка или полностью его очистить.  
"""

animals = ['elephant', 'lion', 'tiger', "giraffe", "monkey", 'dog']  # Создание нового списка
print(animals)

animals[1:3] = ['cat']  # Замена сразу двух элементов - 'lion' и 'tiger' - на один элемент - 'cat'
print(animals)

animals[1:3] = []  # Удаление элементов 'cat' и 'giraffe' из списка
print(animals)

# Теперь полностью очистите список
animals.clear()
print(animals)
