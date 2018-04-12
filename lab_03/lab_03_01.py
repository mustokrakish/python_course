# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе.


def is_prime(a):
    if a == 0 or a == 1:
        return False
    list_1 = [i for i in range(2, a)]
    print(list_1)
    for i in list_1:
        if a % i == 0:
            return False
        else:
            return True


if __name__ == "__main__":
    aa = int(input("Input number \n"))
    print(is_prime(aa))


