# Jameson Bultez, Programming Unit Vocabulary Notes Python

# Algorithm
    # A set of instructions to accomplish a specific task.
    # A recipe for baking brownies.
    # Code that personalizes your YouTube feed depending on what you watch.  
# Assignment Operator
    # = 
    # Assigns information to a variable.
    # computer_science = "cool"
    # myAge = 16 
# Variable
    # A place where information is stored.
    # name
    # views
# String
    # A date type that holds information surround by quotation marks "" or ''.
    # "Hello, World!"
    # 'Goodbye, World.'
# Boolean Value
    # A date type that is either TRUE or FALSE.
    # True
    # False
# Arithmetic Operators
    # + adds.
    # - subtracts.
    # * multiplies.
    # / divides.
    # ** (pow() in C) raises to a power of (exponent).
    # % returns the remainder of a division operation.
    # // (floor() in C) returns the quotient of a division rounded down to the nearest integer.
    # myAge - 12
    # views * 2
# Modulus
    # %
    # returns the remainder of a division operation (defined under ARITHMATIC OPERATORS).
    # 10 % 3 = 1
    # 14 % 4 = 2
# Comparison Operators
    # == equal to.
    # != not equal to.
    # > greater than.
    # < less than.
    # >= greater than or equal to.
    # <= less than or equal to.
    # 5 == 5
    # 6 <= 13
# Logical Operators
    # and (&& in C) evaluates to TRUE if both conditions are TRUE.
        # budget <= 4000 and quality != "terrible"
    # or (|| in C) evaluate to TRUE if either condition is TRUE.
        # finish == True or points >= 500
    # not (! in C) evaluates to TRUE if the condition is FALSE, or vice versa.
        # eggs != "hatched"       
# Conditional Statement
    # if: runs a block of code if the condition evaluates to TRUE.
    # elif (else if in C): runs a block of code if none of the previous statements have been met.
    # else: runs a block of code if none of the other statements are met, a "catch-all".    
if 5 == 5:
    print("Correct.")
elif 5 > 5:
    print("Possibly corect.")
else:
    print("Incorrect.")
    # In C:
    # if (5 == 5) {
    #   printf("Correct.")
    # } else if (5 > 5) {
    #   printf("Possibly correct.")
    # } else {
    #   printf("Incorrect.")
    # }
# Concatenation
    # Combining two strings into one.
message = "You are " + "awesome!"
    # In C:
    # strcat("You are ", "awesome!")
# Iteration/Loops
    # A block of code that repeats a certain number of times.
    # For loop
nums = [5, 10, 15, 20]
for num in nums:
    print(num)
    # While loop
i = 0
while i <= 10:
    print(i)
    i += 1 
# Functions (also called Procedures and Methods)
    # A block of code that receives inputs (arguments) and returns an output; can be reused.
def quadratic(x, a, b, c):
    y = a*x + b*x + c
    return y
def exponential(n):
    z = 2**n
    return z
# Function Call (also called Procedure call or method call)
    # Invokes a function defined earlier in the code.
print(quadratic(3, 2, 4, 16))
print(exponential(7))
# Top-Down Design
    # Breaking down a problem into smaller and smaller pieces; decompistion
    # Separating the different tasks for building a video game and assigning to different group members.
    # Breaking down the challenges of asking a girl out on a date and addressing them one by one.
# Debugging
    # Identifying the errors in a program and fixing them.
# Logic Error
    # A mistake that arises from an broken flow of logic; output is incorrect; does not usually return an error message.
    # You placed the code that was supposed to run in an if statemtent that always evaluates to TRUE, so it always gets skipped.
    # You used ** instead of * when you wanted to multiply two variables.
# Syntax Error
    # A mistake that arises from typing the code incorrectly.
    # Typing "print" instead of "printf" (in C).
    # Typing "flat" instead of "float" (in Python).
# Run Time Error
    # Occurs when a user breaks the program.
    # A user types numbers when they're asked for their name.
    # A user types a space when they're asked for their age.

