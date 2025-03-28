#Ask the user to input their name or sentence
user_input = str(input("Please input your name or a sentence: "))

#Print the input in lowercase without using lower()
def lowercase(user_input):
    lowercased = "" #To store the words
    for character in user_input:
        if 'A' <= character <= 'Z': #To check if the character is in uppercase
            lowercased += chr(ord(character) + 32) #Using chr() and ord() to add 32 into the character in its ASCII value to make it lowercase

        else: 
            lowercased += character #To store it into the lowercased
        
    return lowercased

print(lowercase(user_input))