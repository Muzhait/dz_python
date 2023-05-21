# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять 
# из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 

str = 'пара-ра-рам рам-пам-папам па-ра-па-да '
str = str.split()
for i in range(len(str)):
    str[i] = list(str[i])
list = []
for ind1, val1 in enumerate(str):
    count = 0
    for ind2, val2 in enumerate(val1):
        if str[ind1][ind2] in ['а', 'у', 'е', 'ы', 'о', 'э', 'я', 'и', 'ю']:
            count += 1
    list.append(count)
if len(set(list)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')