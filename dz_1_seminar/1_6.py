# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

while True:
    number = input('Введите шестизначный номер билета: ')
    if number.isdigit() and len(number) == 6:
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            print('Yes, its a lucky ticket!')
        else:
            print('No, you will be lucky another time')
        break
    else:
        print('Введен некорректный номер билета, попробуйте еще раз)')