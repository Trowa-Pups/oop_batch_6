#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Check if the input is upper cased without using isupper()
#Print "True" if it is all uppercase and "False" if not
result = "" 

for character in user_input:
    if 'A' <= character <= 'Z': #To check if the character is in uppercase
        result = "True"

    else:
        result = "False"
        break # I added this because it only reads the final character and it outputs True

print(result)

#Removed def() aka the upperchase_checker because i realized the program is less complicated if it was removed
        