#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Print the first letter of the input capital letter, and the rest small case without using capitalize()
capitalized_input = user_input[0].upper() + user_input[1:].lower() #Makes the first letter user_input[0], uppercased and the rest lower

print(capitalized_input)