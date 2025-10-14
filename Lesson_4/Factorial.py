def factorial(number):
    if number==1:
        return number
    else:
        return number*factorial(number-1)
number=int(input("Enter the number: "))
print("Factorial of", number, " is", factorial(number))