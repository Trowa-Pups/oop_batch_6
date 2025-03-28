#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Ask the user the width of the text 
width = int(input("Please input the width of the text: "))

#Calculate the padding on both sides to the center
left_padding = (width - len(user_input)) // 2 #Uses //2 so that it doesnt output something like 7.5 
right_padding = ((width - len(user_input))) - left_padding 
                 
#Print the input in the center within the given width