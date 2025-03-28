#Ask the user to input their name with multiple spaces in the beginning
name_input = str(input("Please input your name with several spaces at the beginning (     Trowa Tangco): "))

#Print the name without the spaces and without using lstrip
def leftstrip(name_input):
    for i in range(len(name_input)):
        if name_input[i] != " ":
         return name_input[i:]
    
    return ""

print(leftstrip(name_input))