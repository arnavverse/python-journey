def calculateHM(a,b):
    Hmean = (a*b)/(a+b)
    print(Hmean)
def greater(a,b):
    if (a>b):
        print("first number is greater")
    elif (a==b):
        print("both the numbers are equal")
    else:
        print("second number is greater")

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
greater(a,b)
print("The Harmonic Mean will be = ")
calculateHM(a,b)
 
c = int(input("Enter first number : "))
d = int(input("Enter second number : "))
print("The Harmonic Mean will be = ")
greater(c,d)
calculateHM(c,d)
 



