a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))  
if (a >= b and a >= c):
    print("Largest number is a =",a)
elif (b >= a and b >= c):
    print("Largest number is b =",b)
else:
    print("Largest number is c =",c)