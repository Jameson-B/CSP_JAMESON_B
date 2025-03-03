# Jameson Bultez, Loops Notes Python

# Fruit Loops yum yum

#1. What is a loop?
    # A section of code 
#2. What are the two types of loops?
    # For Loop
nums = [12,3,66,7,33,2]

for num in nums:
        print(num)

    # While Loop
x = 0

while x < 10:
        print(x)
        x += 1

#3. What is iteration?
    # Iteration is the number of times you're running the loop.
    # An iteration is one instance of a loop
     
#4. What are lists? 
    # A list is a variable that stores mulitple values.
fruits = ["apple", "banana", "grape", "mango"]
children = ["Linnae", "William", "Ethan", "Grace", "Jameson", "Weston"]
school = [9, "UCAS", True, 3.4]

print(fruits) # prints whole list
print(children[0]) # prints just one item # Output: Linnae

children[5] = "Wepson" # Changes Weston's name to "Wepson".
children.pop(2) # Removes Ethan.
children.insert(1, "Spencer") # Adds Spencer.
children.insert(2, "Theodore") # Adds Theo.

print(children)

#5. How do you make lists in python? 
    # Brackets []
    # Items with correct data types.
    # Comma between each item.
    # Can hold different data types in one list.
#6. How do you make for loops in python?
for child in children:
       print(child)

for x in range(1, 5, 2): # for each item from (inclusive) to (exclusive)(mininum, maximum, count by...)
        print(x)

#7. How do you make while loops in python?
import random

goose = random.randint(1,20)

x = 1



while x <= 20: # Infinite Loop
        if x == goose:
                print("Goose!")
                break # tells the loop to end
        else:
                print("Duck")
        x += 1
# continue moves on to the next iteration

#8. How do you make lists in C?
#9. How do you make for loops in C?
#10. How do you make while loops in C?