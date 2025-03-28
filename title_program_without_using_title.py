#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Print the input into a title() like format without using title()
titled_input = "" #To store the words that are titled
for word in user_input.split(): #To split the into words
    titled_input += word[0].upper() + word[1:].lower() + " "

print(titled_input.rstrip()) #Uses rstrip remove the extra " " at the end