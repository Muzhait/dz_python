# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
# -> 2

n = int(input('Введите количество элементов массива: '))
list = [int(input()) for item in range(n)]
print(list)
count = 0
x = int(input('Введите число: '))
for i in range(len(list) - 1):
    if list[i] == x:
        count += 1
print(count)