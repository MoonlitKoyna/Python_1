print("Calculator")
def addition(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
number1=int(input("Enter your first number: "))
number2=int(input("Enter your second number: "))
print("Addition of numbers", number1, "and", number2, "=", addition(number1,number2))
print("Substraction of numbers", number1, "and", number2, "=", subtract(number1,number2))
print("Multipication of numbers", number1, "and", number2, "=", multiply(number1,number2))
print("Division of numbers", number1, "and", number2, "=", divide(number1,number2))