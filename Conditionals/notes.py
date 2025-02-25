# Jameson Bultez, Conditionals Notes Python


#1. What puts something inside of the “if” statement?
    # Python
        # "if condition:
            # then do this"
        # Content of conditional must be tabbed to be included
            # like this

#2. What do if statements do?
    # Checks a condition, and if it is true, executes some code.
name = input("What is your first name?:\n")
if name == "LaRose": # Checks for condition.
    print("Hi, Ms. LaRose.") # Executes code if true.
else: # If condition is false...
    print(f"Hello, {name}.") # Executes code if false.

#3. What are boolean statements? 
    # A true-or-false statement.

#4. What do else statements do?
    # An else statement executes code if boolean is false.
    
#5. What kind of statement do you use if you have more than 2 needed outcomes?
    # Less likely to more likely.
    # The perfect couple name is elif!
num = float(input("Enter one number:\n"))
if num == 0:
    print("And then there were none.")
elif num == 1:
    print("There is one.")
elif num == 2:
    print("There is a couple.")
elif num == 3:
    print("There is a trio.")
elif num == 12:
    print("There is a dozen.")
elif num == 13:
    print("There is a baker's dozen")
elif num == 20:
    print("There is a score.")
elif num < 6:
    print("There is a few.")
elif num > 5:
    print("There are several.")
elif num < 100:
    print("There are oodles!")
else:
    print("That be a number.")

#6. What do each of the different symbols mean in conditionals?
    # < less than
    # > greater than
    # <= less than or equal to
    # >= greater than or equal to
    # == equal to
    # === same data type as
    # ! not

#7. What are the 3 logical operators?
    # and
if num < 10 and num > 5: # Both conditions must be met.
    print("This is a large single-digit number.")
    # or
if num < 10 or num > 5:
    print("This is a number.")
    # not
if not num < 10: # Checks if FALSE.
    print("This number is greater than or equal to 10.")

#8. What are logical operators for?
    # Allows the code to handle more complex conditionals.

#9. What does a nested conditional statement do?
    # You can nest as many conditionals as you want, but you should never go past three, because it gets confusing and hard to read.
    # An example of using nested conditionals is checking for username and password. You wouldn't even check for password if the username is incorrect. The compiler doesn't have to worry about it.
if num < 10:
    if num == 8:
        print("This number prints 8.")
    else:
        if num == 4:
            print("There are only enough cookies left for me...sorry...")
        else:
            print("The number is less than 10.")
else:
    print("The number is greater than or equal to 10.")



