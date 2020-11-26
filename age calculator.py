#my first age calculator application
user_input = int(input("Please enter your birth date: "))
import datetime

current_year = datetime.datetime.now()
b = current_year.year
a = user_input
i = b - a
print(i, "years")