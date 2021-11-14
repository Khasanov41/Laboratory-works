# Объединение двух строк с использованием символа `+` называется конкатенацией (concatenation).

# Python поддерживает умножение строк на числа.

hello = "Hello "

world = 'World'

# Получите строку "Hello World" с помощью конкатенации предыдущих переменных

new_string = hello + world
print(new_string)

# Получите строку "HelloHelloHelloHelloHelloHelloHelloHelloHelloHello" с помощью операций со строками

new_string = "Hello" * 10
print(new_string)

# Получите строку "Hello, World! World World Hello Hello!"  с помощью операций со строками

new_string = "Hello, " + world + "! " + "World " * 2 + "Hello Hello!"
print(new_string)


# Вы можете получить доступ к символу строки, если знаете его позицию. Например, str[index] даст символ в позиции
# index в строке str.

# Запомните! Строки всегда индексируются с 0.

python = "Python"

p_letter = python[0].lower() + python[2] + python[3] + python[5] # Используйте переменную python для получения строки "pthn".
print(p_letter)


# В Python индексы также могут быть отрицательными числами. Это позволяет начать отсчет с конца строки. 
# Обратите внимание, что, поскольку -0 совпадает с 0, отрицательные индексы начинаются с -1.
# Таким образом, вы можете использовать отрицательные числа в операторе индексирования
# для подсчета символов с конца строки.

long_string = "This is a very long string!"

# Используйте отрицательный индекс для получения символа '!' из строки

new_string = long_string[-1]
print(new_string)