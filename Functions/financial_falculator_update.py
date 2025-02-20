# Jameson Bultez, Financial Calculator Update Python

# Function that calculates percentage of income and prints the info.
def info(cost, income, type):
    percent = round(cost/income*100, 1)
    print(f"Your {type} is ${cost:.2f}, which is {percent}% of your income. \n") 

def inputs(var, category):
    var = float(input(f"What is your monthly {category}?: \n"))

# print statement that welcomes my user and tells them what my program does.
print("Welcome! This is the monthly financial calculator. \n")

inputs(income, "income")
inputs(rent, "rent/mortgage")
inputs(utilities, "utilities cost")
inputs(groceries, "groceries cost")
inputs(transport, "gas/bus fare cost")

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

# calculate savings as 10% of income (income * .1). (variable that is a float).
savings = round(income*.1, 2)

# calculate spending as income - savings - rent/mortgage - utilities - groceries - transportation (variable that is a float)
spending = round(income-savings-rent-utilities-groceries-transport, 2)



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

