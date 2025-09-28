##Task 1. Given a side of square. Find its perimeter and area.
a=float(input("Enter the length of a side of square: "))
p=4*a
s=a**2
print("Perimeter of the square equals to: ",p)
print("Area of the square equals to: ",s)

##Task 2. Given diameter of circle. Find its length.
import math
d=float(input("Enter diameter length of the circle: "))
c=math.pi*d
print("The length of the circle equals to: ",c)

##Task 3. Given two numbers a and b. Find their mean.
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
m=(a+b)/2
print("The mean of numbers a and b equals to: ",m)

##Task 4. Given two numbers a and b. Find their sum, product and square of each number.
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
s=a+b
p=a*b
sqa=a**2
sqb=b**2
print("The sum, product and square of each number are: ",s,p,sqa,sqb)
print("The sum equals to: ",s)
print("The product equals to: ",p)
print("The square of number a equals to: ",sqa)
print("The square of number b equals to: ",sqb)
