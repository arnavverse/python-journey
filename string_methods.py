'''STRING METHODS'''
""" strings are 'IMMUTABLE' """
x = "Masti khor😝"
y = "inSaan!!!!!"
z = "jadugar kala kabula!"
chick = "Just do whatever you want in which you think that you are perfect."
j = "meow05"
f = "Character"
print(x.upper())
print(x.lower())
print(y.rstrip("!"))
print(x.replace("Mastikhor😝","Non-Chalant"))
print(x.split())
print(y.capitalize())
print(len(z))
print(z.center(30))
print(z.count("a"))
print(x.endswith("!"))
print(y.endswith("!"))
print(z.endswith("ka", 0,6))

print(chick.find("doll")) 
"""" FIND only tells the first occurence for what you typed, 
if it won't exists then the output will be -1 """

print(chick.index("think"))
""" INDEX is exactly same as FIND but it give error instead of -1 if that word isn't exists """

print(j.isalnum())
""" The isalnum method returns True only if entire string only consists of A-Z, yz, 0-9.
If any other characters or punctuations are present, then it returns False. """ 

print(f.isalpha())
""" The isalnum method returns True only if the entire string only consists of A-Z, a-z. 
If any other characters or punctuations or numbers(0-9) are present, then it returns False."""

print(f.islower())
""" The islower method returns True if all the characters in the string are lower case,
else it returns False. """

str1 = "Yummy\n"
print(str1)
print(str1.isprintable())
""" The isprintable method returns True
if all the values within the given string are printable, if not, then return False."""

str1 = "          "         
print(str1.isspace())
""" The isspace method returns True only and only
if the string contains white spaces, else returns False."""

str1 = "World Health Organization"
print(str1.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

print(str1.swapcase())
""" The swapcase method returns a string where all the uppercase letters 
are converted to lowercase and all the lowercase letters are converted to uppercase. """

str1 = "why AI is the future?"
print(str1.title())
""" The title method returns a string where the first character in every word is upper case 
and all the remaining characters in the word are lower case. """