import math
# Задание №1
# Упражнение на написание генераторов списков и словарей:
# 1. Создайте список квадратов первых 10 натуральных чисел,
# используя list comprehensions.


squares = [x ** 2 for x in range(1, 11)]
print(squares)


#2. Создайте словарь, содержащий названия дней недели и их порядковые номера, используя dict comprehension.
# Для дней недели можно использовать список ["Понедельник", "Вторник" и т.д.]

d = {}
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

i = 1
for day in days:
    d[day] = i
    i += 1


print(d)

# 3. Создайте множество, содержащее теги библиотек в нижнем регистре, используя list comprehension.
# Исходный список ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]

lower_tags = set()
tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]

for tag in tags:
    lower_tags.add(tag.lower())


print(lower_tags)

