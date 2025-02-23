# Jameson Bultez, Financial Calculator Update Python

# Function to caclulate percent income of an expense and return string informing user.
def info(cost, income, category):
    percent = round(cost/income*100, 1)
    return f"Your monthly {category} is ${round(cost, 2)}, which is {percent}% of your income." 


# print statement that welcomes my user and tells them what my program does.
print("\nWelcome! This is your monthly financial calculator.\nAll inputs should be in US Dollars. (Don't write the dollar $ sign.)\n")

income = float(input("What is your monthly income?:\n"))
rent = float(input("What is your monthly rent/mortage payment?:\n"))
utilities = float(input("What is your monthly utilities cost?:\n"))
groceries = float(input("What is your monthly groceries cost?:\n"))
transport = float(input("What is your monthly gas/bus fare?:\n"))

# calculate savings as 10% of income (income * .1). (variable that is a float).
savings = round(income*.1, 2)

# calculate spending as income - savings - rent/mortgage - utilities - groceries - transportation (variable that is a float)
spending = round(income-savings-rent-utilities-groceries-transport, 2)

print(info(rent, income, "rent/mortgage payment"))
print(info(utilities, income, "utilities cost"))
print(info(groceries, income, "groceries cost"))
print(info(transport, income, "gas/bus fare"))

print(f"You should be saving 10% of your income, which is ${savings}.")
print(f"You you have ${spending} left over to spend.\n")

# print statement that thanks the user and ends the conversation.
print("\nThank you for using the monthly financial calculator. Spend wisely!\n")