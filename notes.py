# <<<<<<<<<<<<<<<<<<<<<<<=>>>>>>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<=====Beginners=====>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<<<<<<<=>>>>>>>>>>>>>>>>>>>>>>>>
# for printing a string
"""
print("How is world?")
"""

# for printing a var i.e NO -> ""
"""
m = "Me iz fine!"
print(m)
"""

# type of variable for numbers
"""
y = 2.6  # float    (+ve)/(-ve) decimal number
x = 5  # int      (+ve)/(-ve) whole number
z = 4j  # complex  "j" acts as a imaginary number
"""

"""
# to check the type of variable
print(type(z))

# convert to float
x1 = float(x)
print(x1)
# convert to complex
x2 = complex(x)
print(x2)
# convert to str
x3 = str(x)
print(x3)
# convert to int
y1 = int(y)
print(y1)
# rounding off number
x10 = round(y, 2)  # round(number, decimal place)
"""

# mathematical operations
# addition -> +
# subtraction -> -
# multiplication -> *
# division -> /
# modulas -> %
# exponent/power -> **
# floor division(round off to closest small whole number) -> //

# <<<<<<<<<<<<<<<<<<<<<<<<==>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<=====Intermediate=====>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<<<<<<<<==>>>>>>>>>>>>>>>>>>>>>>>>>

# characters for variables
# alphabet
# number
# underscore
# case sensitive

"""
# assigning values to var
a, b, c = 1, 2, 3
x = y = z = 20
"""

# multi line value
f = """like
this
you can
have multi line value"""

"""
# retrieving string
print(f[6])
# counting starts form 0, 1, 2....

# counts the number of chars
print(len(f))

# print a part of string
print(f[5:15])
print(f[-10:-4])

# print each char in new line(loop)
g = "like this"
for r in g:
    print(r)

# check if a word is present
print("like" in f)

# <<<STRING METHODS>>>
j = "Just For Example   "
h = "Hello"
m = "World"
"""

"""
capitalize()  # Converts the first character to upper case
casefold()  # Converts string into lower case
center()  # Returns a centered string
count()  # Returns the number of times a specified value occurs in a string
encode()  # Returns an encoded version of the string
endswith()  # Returns true if the string ends with the specified value
expandtabs()  # Sets the tab size of the string
find()  # Searches the string for a specified value and returns the position of where it was found
format()  # Formats specified values in a string
format_map()  # Formats specified values in a string
index()  # Searches the string for a specified value and returns the position of where it was found
isalnum()  # Returns True if all characters in the string are alphanumeric
isalpha()  # Returns True if all characters in the string are in the alphabet
isdecimal()  # Returns True if all characters in the string are decimals
isdigit()  # Returns True if all characters in the string are digits
isidentifier()  # Returns True if the string is an identifier
islower()  # Returns True if all characters in the string are lower case
isnumeric()  # Returns True if all characters in the string are numeric
isprintable()  # Returns True if all characters in the string are printable
isspace()  # Returns True if all characters in the string are whitespaces
istitle()  # Returns True if the string follows the rules of a title
isupper()  # Returns True if all characters in the string are upper case
join()  # Joins the elements of an iterable to the end of the string
ljust()  # Returns a left justified version of the string
lower()  # Converts a string into lower case
lstrip()  # Returns a left trim version of the string
maketrans()  # Returns a translation table to be used in translations
partition()  # Returns a tuple where the string is parted into three parts
replace()  # Returns a string where a specified value is replaced with a specified value
rfind()  # Searches the string for a specified value and returns the last position of where it was found
rindex()  # Searches the string for a specified value and returns the last position of where it was found
rjust()  # Returns a right justified version of the string
rpartition()  # Returns a tuple where the string is parted into three parts
rsplit()  # Splits the string at the specified separator, and returns a list
rstrip()  # Returns a right trim version of the string
split()  # Splits the string at the specified separator, and returns a list
splitlines()  # Splits the string at line breaks and returns a list
startswith()  # Returns true if the string starts with the specified value
strip()  # Returns a trimmed version of the string
swapcase()  # Swaps cases, lower case becomes upper case and vice versa
title()  # Converts the first character of each word to upper case
translate()  # Returns a translated string
upper()  # Converts a string into upper case
zfill()  # Fills the string with a specified number of 0 values at the beginning
"""

# ESCAPE CHARACTERS
"""
\'	Single Quote
\\	Backslash
\n	New Line
\r	Carriage Return
\t	Tab
\b	Backspace
\f	Form Feed
"""

# Priorties
"""
()
**
* , / , // , %
< , <= , > , >= , != , == , is , is not
not
and
or
"""
# Conditional Operators
"""
a == b
a > b
a >= b
a < b
a <= b
a != b
"""

# Conditional Syntax
"""
a1 = 100
b1 = 100
if a1 > b1:  # "and" and "or" to check for two condition at once
    print("A is greater than B")
elif a1 == b1:
    print("A and B are equal")
else:
    print("B is greater than A")

# while loop
# It have 3 statements
# return | break | continue 


def fun():
    number = 0
    while number < 10:
        print(number)
        number += 1
        if number == 3:
            print("Skipped 3")
            continue
        elif number == 6:
            return print(f"breaking number was {number}")
        elif number == 9:
            break


fun()
# Functions
def demo(x01, y01):
    print(x01 + " " + y01)


demo("Life", "Sucks")  # 2 space is advised before calling the function

# range() loop
for x in range(1, 10): # range(from, to, interval)
    print(x)

# while loop
i = 1
while i < 5:
    print(i)
    i += 1

# Types of data storage
# List >>>>> ordered, changeable, allow duplicates
li = ["Car", "Bike", 20, 43.45, True]
li[2] = 99
print(li[2])
"""
# Tuple >>>>>

# Dictionary >>>>>

# <<<<<<<<<<<<<<<<<<<<<<<<==>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<=====Learn Python=====>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<=====The Hard Way=====>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<<<<<<<<==>>>>>>>>>>>>>>>>>>>>>>>>>

# Taking input as arguments before running file
"""
from sys import argv
script, first, second, third = argv
print(f"Script name: {script}")
print(f"First variable: {first}")
print(f"Second variable:  {second}")
print(f"Third variable: {third}")
"""

# Reading/Writing Files

# Opening and editing the file
"""
from sys import argv
script, file_name = argv
# w - write | r - read | a - append
file = open(file_name, 'w')
# Erasing the content of file
file.truncate()
l1 = input("> ")
l2 = input("> ")
l3 = input("> ")
# Writing in the file
file.write(f"{l1}\n{l2}\n{l3}")
# Closing the file
file.close()
"""

# Copying content from one file to another
"""
from sys import argv
import os
_, from_file, to_file = argv
# Reads the file
in_file = open(from_file)
data_to_copy = in_file.read()
in_file.close()
# Writes to file
out_file = open(to_file, 'w')
out_file.write(data_to_copy)
out_file.close()
"""