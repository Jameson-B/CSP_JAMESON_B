# Jameson Bultez, Fizz Buzz Python

# Print integers from 1 to 50 and replace multiples of 3 with "Fizz", mulitples of 5 with "Buzz", and multiplies of 3 and 5 with "FizzBuzz". 
    # Set "x", the iterator, to 1

x = 1
for x in range(1, 51, 1):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)