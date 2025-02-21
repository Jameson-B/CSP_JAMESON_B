# Jameson Bultez, Financial Calculator Python

# print statement that welcomes my user and tells them what my program does.
print("Welcome! This is the monthly financial calculator. \n")

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

# calculate savings as 10% of income (income * .1). (variable that is a float).
savings = round(income*.1, 2)

# calculate spending as income - savings - rent/mortgage - utilities - groceries - transportation (variable that is a float)
spending = round(income-savings-rent-utilities-groceries-transport, 2)

# caclulate percent income of rent/mortgage (rent / income * 100) (variable)
percentRent = round(rent/income*100, 1)

# caclulate percent income of utilities (utilities / income * 100) (variable)
percentUtilities = round(utilities/income*100, 1)

# caclulate percent income of groceries (groceries / income * 100) (variable)
percentGroceries = round(groceries/income*100, 1)

# caclulate percent income of transportation (transportation / income * 100) (variable)
percentTransport = round(transport/income*100 ,1)

# calculate percent income of savings (percentsavings / income * 100) (variable)
percentSavings = round(savings/income*100, 1)

# calculte percent income of spending (spending / income * 100) (variable)
percentSpending = round(spending/income*100, 1)

# white space print statement
print("")

# Your rent is $XX.XX, which is XX% of your income (print statement).
print("Your rent is $", rent, ", which is", percentRent, "%", "of your income.")

# Your utilities is $XX.XX, which is XX% of your income (print statement).
print("Your utilities cost $", utilities, ", which is", percentUtilities, "%", "of your income.")

# Your groceries is $XX.XX, which is XX% of your income (print statement).
print("Your groceries cost $", groceries, ", which is", percentGroceries, "%", "of your income.")

# Your transportation is $XX.XX, which is XX% of your income (print statement).
print("Your transportation costs $", transport, ", which is", percentTransport, "%", "of your income.")

# Your savings is $XX.XX, which is XX% of your income (print statement).
print("Your savings are $", savings, ", which is", percentSavings, "%", "of your income.")

# Your spending is $XX.XX, which is XX% of your income (print statement).
print("Your spending is $", spending, ", which is", percentSpending, "%", "of your income. \n")

# print statement that thanks the user and ends the conversation.
print("Thank you for using the monthly financial calculator. Spend wisely!")

