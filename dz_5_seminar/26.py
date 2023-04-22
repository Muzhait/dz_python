# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N)
#  для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

n = int(input("Введите целое число N: "))
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def triangular_number(n):
    if n == 1:
        return 1
    else:
        return n + triangular_number(n-1)

print("Факториал числа", n, "равен", factorial(n))
print("Треугольное число для числа", n, "равно", triangular_number(n))