# 6.2.	Задайте последовательность цифр. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []
#
# Первоначальное решение:

# from random import randint
#
# n = int(input('Введите количество элементов исходного списка: '))
# list1 = []
# for i in range(n):
#     list1.append(randint(0, 9))
# print("".join(map(str, list1)))
#
# list2 = []
# for i in list1:
#     if list1.count(i) == 1:
#         list2.append(i)
# print(f'Список неповторяющихся элементов: {list2}')

# Решение с использованием filter и lambda:

from random import randint

n = int(input('Введите количество элементов исходного списка: '))

list1 = []
for i in range(n):
    list1.append(randint(0, 9))
print("".join(map(str, list1)))

list2 = list(filter(lambda x: list1.count(x) == 1, list1))
print(f'Список неповторяющихся элементов: {list2}')