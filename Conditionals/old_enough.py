# Jameson Bultez, Old Enough Python

# Welcome user.
print("\nWelcome to Old Enough: Python Edition.\nThis program will tell you what you can do at your current age.\n")

# Set variable "age" to user input.
age = int(input("What is your age in years?\n"))

# Tell user what they can do at their age.
if age > 110:
    print("\nYou are probably old enough to watch over your descendants from heaven. Congrats!")
elif age >= 18:
    print("\nYou are old enough to vote.")
elif age >= 16:
    print("\nYou are old enough to have a driver's license.")
elif age >= 14:
    print("\nYou are old enough to have a learner's permit.")
elif age >= 5:
    print("\nYou are old enough to go to school.")
elif 0 <= age < 5:
    print("\nYou are old enough to do eat, sleep, and cry.")
else:
    print(f"You are old enough to prepare for your life in {abs(age)} years.")

# Conclude.
print("That's what you're old enough to do! Thanks for using Old Enough: Python Edition.\n")
