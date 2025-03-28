#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Print the input in swappped case without using swapcase()
swapcased = ""

for character in user_input:
    if character.isupper():
        swapcased += character.lower()
    
    if character.islower():
        swapcased += character.upper()

    else:
        swapcased += character

print(swapcased)
        
