'''AVERAGE OF TWO NUMBERS''' 
def average(a=2,b=5,c=3):
    average = (a+b+c)/3
    print("The average is",average)

average()

def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:",sum/len(numbers))
    # return 7
    # return sum/len(numbers)

average(2,4,6,8)

'''Hello you'''
def name(fname,mname,lname):
    print("Hello dear,",fname,mname,lname)

fname = input("ENTER YOUR FIRST NAME : ")
mname = input("ENTER YOUR SECOND NAME : ")
lname = input("ENTER YOUR THIRD NAME : ")
name(fname,mname,lname) 
