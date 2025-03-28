#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Print the input in swappped case without using swapcase()
def swapcase(user_input):
    swapcased = "" #To store the words
    for character in user_input:
        if 'A' <= character <= 'Z': #To check if the character is in uppercase
            swapcased += chr(ord(character) + 32) #Using chr() and ord() to add 32 into the character in its ASCII value to make it lowercase

        elif 'a' <= character <= 'z': #To check if the character is in lowercase
            swapcased += chr(ord(character) - 32) #Using chr() and ord() to subtract 32 into the character in its ASCII value to make it upppercase

        else: 
            swapcased += character #To store numbers or special characters into the swapcased
        
    return swapcased

print(swapcase(user_input))