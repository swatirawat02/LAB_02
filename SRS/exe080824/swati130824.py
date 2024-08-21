""""
Program to print numbers where input is taken by user
print maximum of two numbers
print power of two numbers
write program for basic calculator(sum/sub/mul/div
"""
num1 = int(input("Enter First number"))
num2 = int(input("Enter second number"))
maximum = max(num1, num2 ,9)
print(type(maximum))
print(maximum)
print(type(num1))
print(type(num2))

b = pow(num1, num2)
c = print("c is", (num1 ** num2))
d = pow(4, 3)
print(b)
print(d)
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
print(sum)
print(sub)
print(f"{mul:.2f}")
print(f" {div:.2f}")
