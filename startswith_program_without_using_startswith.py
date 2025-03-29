#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Ask the user to input a prefix and check if the previous input starts with it
prefix_input = str(input("Please input your suffix: "))

result = ""
if user_input[:len(prefix_input):] == prefix_input:
    result = "True"

else:
    result = "False"

#Print "True" if the prefix is there and "False" if not
