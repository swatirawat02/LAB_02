"""

WAP to determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.
"""

year = int(input("Enter the year you want to check"))

if (year % 400 == 0) and (year % 100 == 0):
    print("It is a Century leap Year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("leap Year by 4")
else:
    print("not leap year")
