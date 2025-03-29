#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Ask the user to input a word to find in the input
word_input = str(input("Please input your word: "))

#Print the position of the word in the input
position = 1 

for word in user_input.split():
    if word == word_input:
        print(f"Position: {position}")
    position += 1