''' ITERATING OVER A STRING '''

name = 'Mark Zukerberg'
for i in name:
    #  print(i, end=", ")
    print(i)
    if (i=="k"):
        print("error")

''' ITERATING OVER A LIST '''

MANGOS = ["Meta","Anthropic","Nvidia","Google","OpenAI","SpaceX"]
for MANGO in MANGOS:
    print(MANGO)
    for x in MANGO :
         print (x)

''' RANGE () '''
for l in range(8):
    print(l)
for m in range (10):
    print(m+1) 
for n in range(0, 5):
    print(n+1)
for o in range(-6,5):
    print(o+1)

''' RANGE FUNCTION WITH START, STOP, AND STEP ARGUMENTS '''
    
for p in range(1,12,2):
    print(p)
"""
It adds 3 to the previous number until IT HITS THE LAST LIMIT.
1 (starts with 1)
4 (1+3)
7 (4+3)
10 (7+3)
"""