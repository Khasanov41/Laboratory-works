﻿"""
КОРТЕЖИ практически идентичны спискам.
Единственное существенное различие между кортежами и списками заключается в том, что они не могут быть изменены:
вы не можете добавлять, изменять или удалять элементы из кортежа.
Кортежи создаются с помощью запятых, заключенных в скобки, например (a, b, c). 
Заметьте, что для создания кортежа из одного элемента - в скобках должна быть запятая, например (d,). 
"""

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

print(len(alphabet))  # Выведите число букв в алфавите (количество элементов кортежа)