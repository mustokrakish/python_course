import datetime
a = input('Enter the year of your birth here:')
try:
    a = int(a)
    a = datetime.datetime.today().year - a
    if a < 18:
        print('Your are Underage. Your age is', a, '...too low to access')
    elif a > 100:
        print('You are dinosaur. Your age', a, '?!')
    else:
        print('You are adult. Your age:', a, ':)')
except ValueError:
    print('Error. Try Again')


