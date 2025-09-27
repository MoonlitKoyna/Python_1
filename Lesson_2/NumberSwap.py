x=int(input("Enter a number x: "))
y=int(input("Enter a number y: "))
print("Data type of x: ",type(x))
print("Data type of x: ",type(y))
temp=x
x=y
y=temp

print("Value of x after swapping ", x)
print("value of y after swapping ", y)