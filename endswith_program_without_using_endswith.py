#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Ask the user to input a suffix and check if the previous input ends with it
suffix_input = str(input("Please input your suffix: "))

result = ""
if user_input[-len(suffix_input):] == suffix_input:
    result = "True"

else:
    result = "False"

#Print "True" if the suffix is there and "False" if not
print(result)