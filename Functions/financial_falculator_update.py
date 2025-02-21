# Jameson Bultez, Financial Calculator Update Python

# Declare cost variables before they are defined.
income = 0
rent = 0
utilities = 0
groceries = 0
transport = 0


# Set each cost variable to a user input and return the variable.
def inputs(cost, category):
    cost = input(f"What is your monthly {category}?: \n")
    return cost

# Function to caclulate percent income of different expenses and return string informing user.
def advice(cost, income, category):
    percent = round(cost/income*100, 1)
    return f"Your {category} is ${round(cost, 2)}, which is {percent}% of your income.\n" 



# print statement that welcomes my user and tells them what my program does.
print("Welcome! This is the monthly financial calculator. \n")

inputs(income, "income")
inputs(rent, "rent/mortgage")
inputs(utilities, "utilities cost")
inputs(groceries, "groceries cost")
inputs(transport, "gas/bus fare")


# calculate savings as 10% of income (income * .1). (variable that is a float).
savings = round(income*.1, 2)

# calculate spending as income - savings - rent/mortgage - utilities - groceries - transportation (variable that is a float)
spending = round(income-savings-rent-utilities-groceries-transport, 2)

print(advice(rent, income, "rent/mortage"))
print(info(utilities, income, "utilities cost"))
print(info(groceries, income, "groceries cost"))
print(info(transport, income, "gas/bus fare"))
print(f"You should be saving {savings}, which is 10% of your income.")
print(f"You have {spending} left over to spend, which is 10% of your income.")


'''
# ask user what their income is (variable that is an input).
income = float(input("What is your monthly income?: \n"))

# ask user what their rent/mortgage is (variable that is an input).
rent = float(input("How much is your rent/mortgage?: \n"))

# ask user what their utilities cost (variable that is an input).
utilities = float(input("How much do your utilities cost?: \n"))

# ask user what their grocereris cost (variable that is an input).
groceries = float(input("How much do your groceries cost?: \n"))

# ask user what their transportation costs (variable that is an input).
transport = float(input("How much does your gas/bus fare cost?: \n"))
'''

# white space print statement
print("")





info(rent, income, "rent/mortgage")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transport, income, "gas/bus fare")
info(savings, income, "savings")
info(spending, income, "spending")

# white space print statement
print("")

# print statement that thanks the user and ends the conversation.
print("Thank you for using the monthly financial calculator. Spend wisely! \n")

