# Jameson Bultez, First Program Python

# Takes in a name and returns string "Hello, (name)."
def hey_you(name):
    return f"Hello, {name}."

# Asks for user's first name.
user_name = input("What be thy first name?:")

# Prints "Hello, (user_name)."
print(hey_you(user_name))

# Introduces other print statments.
print("These are some other people:")

# Prints additional hello statements.
print(hey_you("Jacob"))
print(hey_you("Sarah"))
print(hey_you("Scott"))
print(hey_you("Hannah"))
