somelist = [1, 12, 2, 53, 23, 6, 17]

# Найдите сумму четных чисел массива. (for, in, %)
even_sum = 0
for i in somelist:
    if i % 2 == 0:
        even_sum = even_sum + i
print("There is", even_sum, "number in list")

# Найдите сумму наибольшего и наименьшего элементов массива. (min,max, sum, sort)
print("Sum of min and max elements is", min(somelist) + max(somelist))

# Проверьте, является ли данный массив возрастающим или убывающим. (if-else)
dict_1 = {1: 'Up', 2: 'Down', 3: 'Undefined'}
r = 1
z = 1
while r == 1:
    for i in range(len(somelist)-1):
        print(i, somelist[i], somelist[i+1])
        if somelist[i] <= somelist[i+1]:
            # print("up")
            z = z + 1
        else:
            r = r + 1
            break
while r == 2:
    for i in range(len(somelist) - 1):
        if somelist[i] >= somelist[i+1]:
            # print("down")
            z = z + 1
        else:
            r = r + 1
            break
print("Type of list", dict_1[r])

#  Найдите количество различных элементов данного массива. (in)
#  Определите, есть ли в массиве повторяющиеся элементы. (in)
dif_el = 0
for i in range(len(somelist)):
    if somelist.count(somelist[i]) > 1:
        print(somelist[i], "element repeats - ", somelist.count(somelist[i]), "times")
    else:
        dif_el = dif_el + 1
print("Different elements ", dif_el)

# Удалить в  массиве первый и последний элементы.
somelist_del = somelist[1:-1]
print("Without first and last elements", somelist_del)

#  Переставить элементы массива в  обратном порядке. (reverse)
somelist.reverse()
print("revers list", somelist)
