# Jameson Bultez, Name Decorator Python

# Declare all string decorator variables.

arrowsLeft = "<<< "
arrowsRight = " >>>"

paranthesesLeft = "((( "
paranthesesRight = " )))"

dashes = " --- "

smiles = " :) :) "

hashes = " ### "

plusses = " +++ "

tildes = " ~~~ "

equals = " === "

# Welcome user and tell them what the program does.

print("Welcome! This is the Name Decorator: Python Edition, by Jameson Bultez. This program will print your first name with various embelishments. \n")

# Set variable "name" to a user input.

name = input("What is your first name? \n").strip().lower().capitalize()

# Print "name" with string decorators.

print(arrowsLeft + name + arrowsRight)

print(paranthesesLeft + name + paranthesesRight)

print(dashes + name + dashes)

print(smiles + name + smiles)

print(hashes + name + hashes)

print(plusses + name + plusses)

print(tildes + name + tildes)

print(equals + name + equals)

# Conclude the program.

print("What do you think? \n Thank you for using the Name Decorator: Python Edition, by Jameson Bultez. \n")
