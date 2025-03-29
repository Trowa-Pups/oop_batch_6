#Ask the user to input a number
number_input = int(input("Please input a number: "))

#Ask the user to input how many digits Ex. ( 6 (000000) )
digit_input = int(input("Please input how many digits Ex. ( 6 (000000) ): "))

#Print the number in how many digits the user inputed
result = str(number_input).rjust(digit_input, "0") #turned it into str so that rjust to be used to fill the zeros

print (result)