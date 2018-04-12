# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
# третий - операция, которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; 
# / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".


def arithmetic(a, b, action):
    if action == '+':
        return a+b
    elif action == '-':
        return a-b
    elif action == '*':
        return a*b
    elif action == '/':
        return a/b


if __name__ == "__main__":
    aa = int(input("Input A"))
    bb = int(input("Input B"))
    aaction = input("Input mathematical sign")
    print(arithmetic(aa, bb, aaction))