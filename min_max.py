# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/10/2024
# Description: Records number of integers and prints out the min and max values from said integers

#Initial question for integers that also makes input read as integer
integers = int(input("How many integers would you like to enter?"))

if integers >= 1:
    #Secondary list of integer questions to ask for inputs
    first_integer = int(input(f"Please enter your {integers} integers."))
    min = first_integer
    max = first_integer

    #Loop for the rest of the integers
    for _ in range(integers - 1):
        current_integer = int(input()) 

    #Updating the min and max value as the integers are entered
        if current_integer < min:
            min = current_integer
        if current_integer > max:
            max = current_integer

    #Printing of final min and max values
    print(f"min: {min}")
    print(f"max: {max}")
else: print("your number of integers has to be >= 1")