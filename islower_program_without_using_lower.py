#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Check if the input is lower cased without using islower()
#Print "True" if it is all lowercase and "False" if not
result = "" 

for character in user_input:
    if 'a' <= character <= 'z': #To check if the character is in lowercase
        result = "True"

    else:
        result = "False"
        break #It immediently prints fails when it else is activated

print(result)