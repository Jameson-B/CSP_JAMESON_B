# Jameson Bultez, Financial Calculator Python

# print statement that welcomes my user and tells them what my program does.
print("Welcome! This is your monthly financial calculator.")

# ask user what their income is (variable that is an input).
income = float(input("What is your monthly income?: \n"))

# ask user what their rent/mortgage is (variable that is an input).
rent = float(input("How much does your rent/mortgage cost?: \n"))


# ask user what their utilities cost (variable that is an input).
utilities = float(input("How much do your utilities cost?: \n"))

# ask user what their grocereris cost (variable that is an input).
groceries = float(input("How much do your groceries cost?: \n"))

# ask user what their transportation costs (variable that is an input).
transport = float(input("How much does your gas/bus fare cost?: \n"))

# calculate savings as 10% of income (income * .1). (variable that is a float).
percentSavings = income*.1

# calculate spending as income - savings - rent/mortgage - utilities - groceries - transportation (variable that is a float)
spending = income-percentSavings-rent-utilities-groceries-transport

# caclulate percent income of rent/mortgage (rent / income * 100) (variable)
percentRent = rent/income*100

# caclulate percent income of utilities (utilities / income * 100) (variable)
percentUtilities = utilities/income*100

# caclulate percent income of groceries (groceries / income * 100) (variable)
percentGroceries = groceries/income*100

# caclulate percent income of transportation (transportation / income * 100) (variable)
percentTransport = transport/income*100

# calculte percent income of spending (spending / income * 100) (variable)
percentSpending = spending/income*100

# Your rent is $XX.XX, which is XX% of your income (print statement).
print("Your rent is", rent, ", which is", percentRent, "of your income.")

# Your utilities is $XX.XX, which is XX% of your income (print statement).

# Your groceries is $XX.XX, which is XX% of your income (print statement).

# Your transportation is $XX.XX, which is XX% of your income (print statement).

# Your savings is $XX.XX, which is XX% of your income (print statement).


# Your spending is $XX.XX, which is XX% of your income (print statement).



