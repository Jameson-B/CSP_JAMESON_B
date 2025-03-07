# Jameson Bultez, Three x Plus One Python

# Set variable "num" to an integer user input.
num = int(input("Enter any postive integer:\n"))

# If num is even, multiply by 2. If it's odd, multiply by 3, then add 1. Print result. Continue until num is equal to 1 exactly.
while num >= 1:
    if num == 1:
        break
    elif num % 2 == 0:
        num /= 2
    else:
        num = num * 3 + 1
    print(num)