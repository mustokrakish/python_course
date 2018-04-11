import datetime

a = datetime.datetime.today().year
name = input("Enter your name \n")
while True:
    year = input("Enter your year of birth. in format yyyy \n")
    if len(year) == 4 and year.isdigit():
        year = int(year)
        if year > a or (a - year) > 100:
            print(name, "Enter correct year. Just 4 digits")
            continue
        else:
            break
if (a - year) < 18:
    print(name, "You are too young")
else:
    print(name, "Welcome to club")
