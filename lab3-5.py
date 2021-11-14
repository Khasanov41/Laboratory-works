name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")
group = input("Введите название вашей группы: ")
print(f"""
Привет, {last_name} {name} из группы {group}! 
      Введи свою электронную почту?
""")
email = input()

print((last_name[:5] + name[:5] * 2 + email[:5] * 3).lower())