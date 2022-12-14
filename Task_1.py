# 6.1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12
#
# Первоначальное решение:
#
# list = [2, 3, 5, 9, 3]
# total = 0
# for i in range(0, len(list)):
#     if i % 2 != 0:
#         total += list[i]
# print(f'Сумма элементов, стоящих на нечетных позициях, равна {total}')

# Решение с использованием list comprehension:

list = [2, 3, 5, 9, 3]
total = sum(list[item] for item in range(1, len(list), 2))
print(f'Сумма элементов, стоящих на нечётных позициях, равна {total}')