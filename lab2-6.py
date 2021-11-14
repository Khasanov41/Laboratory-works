"""
Task: Реализуйте программу, которая запрашивает с клавиатуры имя пользователя и выводит сообщение: Hello, имя!.
"""

name = input("Please, enter your name: ")
print("Hello,", name + "!")

"""
Task: 
Вычислите номер своего варианта по следующему алгоритму:
1) вычислить сумму даты и месяца рождения;
2) вычислить остаток от деления суммы на 4;
3) прибавить 1 к результату.
"""

print("Option: " + str(((10 + 4) % 4) + 1))

"""
    Далее следует решение задачи из файла "equation.pdf"
"""
# ===================================================================
print("\nExercise number one.")
while True:
    x = input("Enter the value of x: ")
    if x.isdigit():
        x = int(x)
        try:
            y = (x ** 2 + 1) / (3 * (x ** 2 - 1)) + (x ** 2 - 1) * (1 - x)
        except ZeroDivisionError:
            print("Error: division by zero.\nPlease, try another value.")
            continue
        print("Result:", y)
        break
    else:
        continue
# ===================================================================
"""
    Дадее следует решение задачи из файла “geometry.pdf”
"""
print("\nExercise number two")
while True:
    a = input("Enter the value of a: ")
    if a.isdigit():
        a = int(a)
        radius = 0.25 * a * (2 * 5 + 5**2)**0.5
        print("Result:", radius)
        break
    else:
        continue
# ===================================================================
