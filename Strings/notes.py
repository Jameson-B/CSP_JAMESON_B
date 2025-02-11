# Jameson Bultez, Strings Notes Python

# String: a data type that holds information surrounded by quotiation marks "" ''.

# Substring: a small portion of a string.

# Syntax: the conventions of a written language.

# Stupid-proofing AKA sanitization: protecting against user craziness.

# Bug: an error.

# Syntax Error: spelling was incorrect.

# Runtime Error: a user broke the program.

# Type Error: data types did not agree.

# Logic Error: programmer goofed, output will be incorrect.
    # Print debugging.
    # Start at the beginning, explaining it step by step.

# find(): gets the first instance of that text.

# concatenation: fusing strings together

# len(): gets the length of a string, including spaces.

# upper(): converts a string to ALL CAPS.

# lower(): converts a string to all lowercase.

# strip():

note = "Vienna's class"

name = input("What is your first name? \n").strip().lower().capitalize()

print("This is your name: " + name)

print(f"Hello, {name}, welcome to my program!")

sentence = "The quick brown fox jumps over the lazy dog."

print(len(sentence))

start = sentence.find("fox")
length = sentence.find("brown")
print(sentence[start : start + length])
