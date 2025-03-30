#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Ask the user to input a word to find in the input
word_input = str(input("Please input your word: "))

#Print the position of the word in the input
position = 1 
found = 0 #To see if a single word was found

for word in user_input.split():
    if word == word_input: #Checks if the word is the same word that the user ask to find
        print(f"Position: {position}") 
        found += 1 #To update the found
    position += 1 #To update the position even if the word isn't found

if found <= 0:
    print("Word not found")