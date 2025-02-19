# Jameson Bultez, Functions Notes Python

# Functions hold actions to be reused.

# Function names require all lowercase letters.

# In Python, an indent communicates to the computer that the code is contained within a function.

# camelCase

# snake_case


number = int(input("Please tell me a number:\n"))
integer = int(input("Please tell me another number:\n"))

def add(numOne, numTwo):  
    # print(numOne + numTwo)
    return numOne + numTwo

print(add(5, 10))

addition = add(6,4)
add(addition, 1000)

def values(type):
    return input(f"Please give me a {type}:\n")

name = values("name")
place = values("place")
verb = values("verb (past tense)")

print(f"{name} was really fast getting to {place} because they {verb} the whole way there.")