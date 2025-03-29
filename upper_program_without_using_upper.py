#Ask the user to input their name or sentence
user_input = str(input("Please input your name or a sentence: "))

#Print the input in uppercase without using upper()
def uppercase(user_input):
    uppercased = "" #To store the words
    for character in user_input:
        if 'a' <= character <= 'z': #To check if the character is in lowercase
            uppercased += chr(ord(character) - 32) #Using chr() and ord() to subtract 32 into the character in its ASCII value to make it uppercase

        else: 
            uppercased += character #To store it into the uppercased
        
    return uppercased

print(uppercase(user_input))