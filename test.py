#!/usr/bin/python

### Hello World ###
print("###### Python Basics! ######")
print("https://www.tutorialspoint.com/python/index.htm")

### Variables ###
print("\n### Variables ###")
name    = "Felipe Mallea"
a = b   = 5
a,b,name = 3, 10, "Felipe"

print(name + " Sentis \nAge: " + str(a*b+a))
print(name[0:6])

### Listas y Tupals ###
print("\n### Lists & Tuples ###")
fruits = ["Apple", "Orange", "Banana", "Watermelon", "Avocado"]
print(fruits[0:3] + fruits[3:5])

names = ("Felipe", "Marcos", "Andrés", "Juan") # Las tuplas son listas read-only
print (names)

### Diccionario ###
print("\n### Dictionaries ###")
dictionary =  {}
dictionary[1] = "Value for 1"
dictionary["two"] = "Value for two"
dictionary[3] = 3

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

### Conversiones ###
# int(x [,base]) - Converts x to an integer. base specifies the base if x is a string.
# long(x [,base] ) - Converts x to a long integer. base specifies the base if x is a string.
# float(x) - Converts x to a floating-point number.
# complex(real [,imag]) - Creates a complex number.
# str(x) - Converts object x to a string representation.
# repr(x) - Converts object x to an expression string.
# eval(str) - Evaluates a string and returns an object.
# tuple(s) - Converts s to a tuple.
# list(s) - Converts s to a list.
# set(s) - Converts s to a set.
# dict(d) - Creates a dictionary. d must be a sequence of (key,value) tuples.
# frozenset(s) - Converts s to a frozen set.
# chr(x) - Converts an integer to a character.
# unichr(x) - Converts an integer to a Unicode character.
# ord(x) - Converts a single character to its integer value.
# hex(x) - Converts an integer to a hexadecimal string.
# oct(x) - Converts an integer to an octal string.

### Estructuras de Flujo ###
print("\n### Lopp & Flow Control ###")
a,b = 5,10
if(a >= b):
    print("A is greater than or equal to b")
else:
    print("A is less than b")

for fruit in fruits:
    print("Fruta: " + fruit)

while(a < b) :
    print ("A: " + str(a))
    a += 1


str = input("Enter your input: ");
print ("Received input is : " + str)
