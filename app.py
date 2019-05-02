print("#####################################################")
print("Python side-notes")
print("*The order in which you write the instructions matters")
print("*Don't mix tabs and spaces; they are not interchangeable")
print("#####################################################")
print("Variables in Python")
age=70
name="Carlos Salcedo"
male=True
print("""Python accepts different types of variables, but you don't have to define them.
You can have strings, ints, floats, boolean, etc.
* You can't mix strings and numeric type variables together, unless
you convert the strings to numbers or numbers to strings. To do this, 
you have to use the following python functions:
int()
str()
float()
bool()
""")
mytruth="True"
if ( bool(mytruth) ):
    print("I created a string variable with the word \"mytruth\", and converted it to boolean. And that's why this sentences is being printed")
else:
    print("You did something wrong")
print("This program was created by "+name+" at the age of "+str(age))
print("Is "+name+" a male? "+str(male))
print("""
Strings have multiple built in functions, like:
    index() = Returns the index of the position of the given strings
    replace() = replaces characters within a string
    [#] = used to select a specific character in a string
        """)
print(name.index("Salcedo"))
print("First initial: "+name[0])
print("#####################################################")
print("""
Python is capable of doing the basic arithmatic operations: +,-,/,*, and modulus(%)
* don't forget that you can't mix strings and numeric type variables together, unless
you convert the strings to numbers or numbers to strings.

Python also has certain built in functions for slightly complex operations, such as:
pow() 
max()
min()
round()

Python also has a math library, which allows us to do more scientific and even more 
advance functions that the default built-in python functions, for example:
floor()
ceil()
sqrt()

To use these advance functions, the math library needs to be imported by adding the following line:
from math import *

Here are some examples of the output of the math functions
""")
from math import *
print("print(pow(3,6) = "+str(pow(3,6)))
print("print(max(3,6) = "+str(max(3,6)))
print("print(min(3,6) = "+str(min(3,6)))
print("print(round(4.6) = "+str(round(4.6)))
print("print(floor(4.6) = "+str(floor(4.6)))
print("print(ceil(9.6) = "+str(ceil(9.6)))
print("print(sqrt(4.6) = "+str(sqrt(4.6)))
print("#####################################################")
print("""Python also allows users to add input into the program via command line with
        input()""")
skipper  = input("Do you want to run all the input examples? Y or N ")
if (skipper == "Y" or skipper == "y"):
    newName = input("Enter your name: ")
    newAge = input("Enter your age: ")
    print("Hello "+newName+", you are "+newAge)
    print("#####################################################")
    print("Now we are going to build a very basic calculator")
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print(num1+" + "+num2+" = "+str(float(num1)+float(num2)))
    print(num1+" - "+num2+" = "+str(float(num1)-float(num2)))
    print(num1+" * "+num2+" = "+str(float(num1)*float(num2)))
    print(num1+" / "+num2+" = "+str(float(num1)/float(num2)))
    print(num1+" % "+num2+" = "+str(float(num1)%float(num2)))
    print("#####################################################")
    print("And now, a quick mad libs games")
    color = input("Enter a color: ")
    plural_noun = input("Enter a plural noun: ")
    noun = input("Enter any noun: ")
    print("Roses are "+color)
    print(plural_noun+" are blue")
    print("I love "+noun)


print("#####################################################")
print("Working with lists")
print("""Much like strings, lists are special objets that have certain built-in functions already
which allows us to peform cerating operations with lists, such as,
merge, concatenate, cut, find the number of elements, among
        """)
print("some example lists")
cars = ["ferrari", "lamborghini", "audi"]
print(cars)
randomList = [False, "car", 35.2]
print(randomList)
lucky_numbers = [3,5,7,11,13,17,19]
print(lucky_numbers)
superheros = ["wolverine","spiderman","thor", "ironman","hulk", "hawk eye", "gambit"]
print(superheros)
print("I would like a  "+cars[-2])
print("Examples of list functions")






























