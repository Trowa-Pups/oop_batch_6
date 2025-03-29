#Ask the user to input their name with multiple spaces in the end
name_input = str(input("Please input your name with several spaces at the end (Trowa Tangco      ): "))

#Print the name without the spaces and without using rstrip
def rightstrip(name_input):
    for i in range(len(name_input)-1, -1, -1): 
        if name_input[i] != " ": #To check if its not a space
         return name_input[:i + 1] # I put a +1 in there because it removes the last character not the space
    
    return ""

print(rightstrip(name_input))
