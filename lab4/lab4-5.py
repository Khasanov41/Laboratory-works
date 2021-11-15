# Создаём словарь пуствми значениями
dictionary = {'name': [], 'last_name': [], 'middle_name': [], 'year': [], 'disease': []}
count = 1
# Заполняем словарь в соответстивие с заданием
for i in range(count):
    dictionary['name'].append(input("Имя: "))
    dictionary['last_name'].append(input("Фамилия: "))
    dictionary['middle_name'].append(input("Отчество: "))
    dictionary['year'].append(input("Год рождения: "))
    dictionary['disease'].append(input("Заболевание: "))

# Выводит заголовок таблицы
print(f"""
{'_' * (15 * 5 + 6)}
| Имя           | Фамилия       | Отчество      | Год рождения  | Заболевание   |
{'_' * (15 * 5 + 6)}""")

# Выводит строки таблицы со значениями из словаря
for i in range(count):
    name, last_name, middle_name, year, disease = dictionary['name'][i], dictionary['last_name'][i], \
                                                  dictionary['middle_name'][i], dictionary['year'][i], \
                                                  dictionary['disease'][i]
    print(f"| {name}{' ' * (14 - len(name))}| {last_name}{' ' * (14 - len(last_name))}| \
{middle_name}{' ' * (14 - len(middle_name))}| {year}{' ' * (14 - len(year))}| {disease}{' ' * (14 - len(disease))}|")

# Закрывет таблицу черотой
print('_' * (15 * 5 + 6))
