# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9 

print(type(number))   # Вывод типа переменной number 

float_number = 9.0
print(int(float_number))

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов  

dictonary = {"Name": "Albert", "Last_name": "Einstein", "Subject": "Physic"}
print(type(dictonary))

tuple = ("Юрий Гагарин", "Алексей Леонов", "Владимир Комаров")
print(type(tuple))

pi = 3,1415926535
print(type(pi))

string = "Hello, world!"
print(type(string))

# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.
pi = str(pi)
print(type(pi))
pi = int(float_number)
print(type(pi))
number = float(number)
print(type(number))