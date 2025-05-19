# Jameson Bultez, Binary Converter Python

#TODO: write binary_to_decimal and decimal to binary

def binary_to_decimal(binary_list):
    for digit in binary_list:
        if digit == 0:
            binary_list.index


    

while True:
    binary_input = input("Please Enter a binary value.\n")
    binary_list = [int(digit) for digit in binary_input]

    if all(digit in (1,0) for digit in binary_list):
        print("Valid input.")
        break
    else:
        print("Invalid input.")


