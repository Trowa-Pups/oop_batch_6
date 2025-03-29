#Ask the user to input their name or a sentence
user_input = str(input("Please input your name or a sentence: "))

#Ask the user to input the word to count
count_input = str(input("Please input the word you want to count: "))

#Print the count of the word inputted to count
word_count = 0 #To count how many times the word appears

for word in user_input.split():
    if word == count_input:
        word_count += 1

print("Count:" , word_count)

