#  Дано 2 строки. Вернуть результат  их конкатенации за исключением первой буквы  первого слова.
str_1 = 'Down the Rabbit-Hole'
str_2 = 'The Pool of Tears'
print(str_1[1:] + str_2[1:])

# Дана строка. Вернуть новую строку, которая состоит из  трех  повторений двух последних букв  изначальной строки.
str_3 = str_1[-2:] * 3
print(str_3)

#  Дан список из целых чисел длинной в  три числа. Вернуть список
#   отсортированный в обратном порядке, не используя метод .reverse()
list_1 = [1, 12, 2]
print(list_1[::-1])

# Дан список из целых чисел длинной в  три числа. Определить какое
#   число наибольшее и вернуть новый список такой же длинны,
#   состоящий из максимального числа исходного писка
list_2 = [max(list_1)]*len(list_1)
print(list_2)


#  Дан список целых чисел. Посчитать сумму всех чисел массива, при
#   учете, что числа в промежутке от 13 до 19 включительно, должны
#   приравниваться нулю, за исключением 15 и 16.
sum_1 = 0
list_3 = [i for i in range(30)]
for i in list_3:
    if 13 <= list_3[i] <= 19 and list_3[i] != 15 and list_3[i] != 16:
        list_3[i] = 0
    sum_1 = sum_1 + list_3[i]
print(sum_1)
