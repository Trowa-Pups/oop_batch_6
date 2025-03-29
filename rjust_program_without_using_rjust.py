#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Ask the user what character and how many is gonna be added
character = str(input("Please input what character you want: "))
number_of_characters = int(input("Please input how many characters: "))

#Print the result 
print(character * number_of_characters + user_input)