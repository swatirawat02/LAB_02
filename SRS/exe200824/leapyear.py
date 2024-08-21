"""

WAP to determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.
"""

year = int(input("Enter the year you want to check"))

if year//400 and year // 100 and year/4:
    print("leap Year by 400")
elif year //4:
    print("leap Year by 4")
else:
    print("not leap year")
