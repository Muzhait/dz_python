# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

k = int(input('Введите количество элементов списка: '))
list = [int(input()) for i in range(k)]
min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))
list_ind = [j for j in range(k) if min <= list[j] <= max]
print(list_ind)