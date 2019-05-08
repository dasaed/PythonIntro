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
print("side note: python can also do exponents with '**'")
print("print(str(3**6)) = "+str(3**6))
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
print("randomList: ")
randomList = [False, "car", 35.2]
print(randomList)
print("lucky_numbers")
lucky_numbers = [3,5,7,11,13,17,19]
print(lucky_numbers)
print("#####################################################")
print("Examples of list functions")
print("cars: ")
cars = ["ferrari", "lamborghini", "audi", "bmw", "lexus"]
print(cars)
print("")
print("cars[3:]")
print(cars[3:])
print("cars.index(\"bmw\")")
print(cars.index("bmw"))
print("cars[4]")
print(cars[4])
print("*cars")
print(cars)
print("")
print("")
print("superheros")
superheros = ["wolverine","spiderman","thor", "ironman","hulk", "hawk eye", "gambit"]
print(superheros)
print("")
print("")
print("superheros.append(\"storm\") = adds \"storm\" to the end of the list")
superheros.append("storm")
print(superheros)
print("")
print("")
print("superheros.insert(int_x, \"item\") = adds \"item\" in int_x position")
print("superheros.insert(2,\"black widow\")")
superheros.insert(2,"black widow")
print(superheros)
print("")
print("")

print("superheros.remove(\"ironman\") = removes \"ironman\" ")
print("superheros.remove(\"ironman\")")
superheros.remove("ironman")
print(superheros)
print("")
print("")
print("superheros.pop() = removes the last element from the list")
superheros.pop()
print(superheros)
print("")
print("")
print("superheros.index('spiderman') = throws the index of the location of spiderman")
superheros.index('spiderman')
print("")
print("")
print("superheros.clear() = removes all elements from superheros")
superheros.clear()
print(superheros)
print("")
print("")
print("Merging 2 lists together")
print("superheros.extend(cars) = adds cars to the end of superheros (this modifies superheros directly)")
superheros.extend(cars)
print(superheros)
print("")
print("")
print("You can also count how many times an item is repeated in the list")
print("superheros.append(\"audi\")")
superheros.append("audi")
print("superheros.count(\"audi\")")
print(superheros.count("audi"))
print("")
print("")

print("cars.reverse() = reverses the order of the list")
print(*cars)
cars.reverse()
print(*cars)
print("")
print("")
print("cars.sort() = sorts the list")
print(*cars)
cars.sort()
print(*cars)

print("")
print("")
print("cars2 = cars.copy() = copies list to a completely new one")
print(*cars)
cars2 = cars.copy()
print(*cars2)
cars2.append("chevrolet")
print(*cars)
print(*cars2)



print("#####################################################")
print("#####################################################")

print("Now we are moving on to tuples")
print("coordinates = (4,6)")
coordinates = (4,6)
print("print(coordinates[0])")
print(coordinates[0])


print("#####################################################")
print("#####################################################")
print("Now we are moving on to functions!!!")

def say_hi(name, father, mother):
    print("Hello "+name+" Son of "+father+" and "+mother)
    return "this function works"

def cube(a):
    c = pow(a,3)
    return c
    
print("Top")
say_hi("dasaed", "Father", "Mother")
result = cube(5)
print("Bottom")
print(cube(3))
print(result)
print("")
print("")
print("")





if (skipper == "Y" or skipper == "y" or skipper == " "):
    print("#####################################################")
    print("#####################################################")
    print("if statements:")
    is_male = True
    is_tall = False
    is_fat = False
    is_rich = True
    if ( is_male or is_tall ) and is_fat == True:
        print ("You are a male")
    elif not(is_rich):
        print("You are poor")
    else:
        print("You are a female")
        
def max_num(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(str(num1)+" is the biggest number")

    elif num1 > num2 and num1<num3:
        print(str(num3)+" is the biggest number")

    elif num1 < num2 and num1>num3:
        print(str(num2)+" is the biggest number")

    elif num1 < num2 and num1 < num3:
        if num2 > num3:
            print(str(num2)+" is the biggest number")
        else:
            print(str(num3)+" is the biggest number")

    else:
        print(str(num3)+" is the biggest number")

if (skipper == "Y" or skipper == "y" or skipper == " "):
    print("#####################################################")
    print("#####################################################")
    num1 = input("Enter Number 1: ")
    num2 = input("Enter Number 2: ")
    num3 = input("Enter Number 3: ")
    max_num(float(num1),float(num2),float(num3))



print("#####################################################")
print("#####################################################")
print("Starting Dictionaries")
monthConversion1= {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December"
        }

monthConversion2 = {
        "0": "undefined",
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December",
        }
print(monthConversion1)
print("print(monthConversion1)")
print(monthConversion1["Nov"])
print(monthConversion1.get("Nov"))
print('print(monthConversion1.get("Nov"))')
print(monthConversion1.get("das","not a valid key"))
print(monthConversion2["2"])






print("#####################################################")
print("#####################################################")
print("Now we are going to start with the while loops")



whilevar = 0
i = 0
while (whilevar == 0):
    i+=1
    print("I'm on loop "+str(i) )
    stop = input("Do you want to exit this while loop?")
    if stop == "Y" or stop == "y":
        whilevar = 1
    

print("#####################################################")
print("#####################################################")
print("Now we are going to start with the for loops")

for letter in "work hard, play hard":
    print(letter)

superheros = ["wolverine","spiderman","thor", "ironman","hulk", "hawk eye", "gambit"]
for hero in superheros:
    print(hero)
for number in range(len(superheros)):
    print(str(number)+" superhero")

for index in range(10):
    print(index)

print("#####################################################")
print("#####################################################")
print("Nested loops and 2-dimensional lists")
number_grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0]
        ]
print("print(number_grid)")
print(number_grid)
print("print(number_grid[0][2])")
print(number_grid[0][2])

for row in number_grid:
    print(row)
    for col in row:
        print(col)

if (skipper == "Y" or skipper == "y" or skipper == " "):
    print("#####################################################")
    print("#####################################################")
    print("Building a basic translator in python")
    print("We are building a made up language.")

def translate(phrase):
    translation = ""
    for char in phrase:
        if char == "a" or char == "A":
            translation = translation + "1"
         
        elif char == "e" or char == "e":
            translation = translation + "2"

        elif char == "i" or char == "I":
            translation = translation + "3"


        elif char == "o" or char == "O":
            translation = translation + "4"

        elif char == "u" or char == "U":
            translation = translation + "5"

        else:
            translation = translation + str(char)

    return translation


if (skipper == "Y" or skipper == "y" or skipper == " "):
    print(translate(input("Enter a phrase: ")))



print("#####################################################")
print("#####################################################")
print("Handling errors with 'try' and 'except'")

try:
    zerodiv = 10/0
    number = int(input("Enter a number ") )
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
except:
    print("There is some error somewhere in the code")


print("#####################################################")
print("#####################################################")

'''
This is a way of making multiline comments, but it is not a recommended way. 
it's getter to use use the # symbol
'''


print("#####################################################")
print("#####################################################")
print("Reading from files")

print("Python has a read command to read different input file types")
print("""When you open a file, you can open it in 3 different modes:
        r = read only
        w = write
        a = append
        r+ = read and write""")
print("The following commands are what you need to open and close a file. Do not forget to close a file after you are done using it.")
print('myskills = open("./skills.txt", "r")')
myskills = open("./skills.txt", "r")
print('myskills.close()')
myskills.close()

print('myskills = open("./skills.txt", "r")')
myskills = open("./skills.txt", "r")
print("Checking if a file is readable (good practice to do before opening a file)")
print("myskills.read()=basic standard command to read a file")
print(myskills.read())
print("myskills.readable()")
print(myskills.readable())
print("myskills.readline() = reads the first line, and then moves on to the next line. (executing this line twice will print the first 2 lines, not the same line twice)")
print(myskills.readline())
myskills.close()
myskills = open("./skills.txt", "r")
print("myskills.readlines() = converts every line of the file into an array")
print(myskills.readlines())

myskills.close()



print("#####################################################")
print("#####################################################")
import random
print("Writing to files")
random_file = open("./random.txt", "a")
rannum1 = random.randint(0,100)
rannum2 = random.randint(0,100)
rannum3 = random.randint(0,100)
random_file.write("\nRandom Numbers : "+str(rannum1)+" "+str(rannum2)+" "+str(rannum3)+"")
random_file.close()
rrandom_file = open("./random.txt", "r")
print(rrandom_file.read())
rrandom_file.close()







