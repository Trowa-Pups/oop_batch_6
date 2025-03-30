#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Ask the user to input a word to find in the input
word_input = str(input("Please input your word: "))

#Print the position of the last occurance of the word in the input
position = 1 
last_position = 0 #Made it like found, but it also store the position of the last occurance of the word

for word in user_input.split():
    if word == word_input: #Checks if the word is the same word that the user ask to find
        last_position = position 
    position += 1 #To update the position even if the word isn't found

if last_position <= 0:
    print("Word not found")

else:
    print(last_position)