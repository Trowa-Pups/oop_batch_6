#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Print the input in swappped case without using swapcase()
swapcased = "" #To store the words

for character in user_input:
    if character.isupper(): #Checks if its uppercased
        swapcased += character.lower() #Converts to lower
    
    if character.islower(): #Checks if its lowercased
        swapcased += character.upper() #Converts to upper

    else:
        swapcased += character #To keep the numbers and special numbers 

print(swapcased)
        
