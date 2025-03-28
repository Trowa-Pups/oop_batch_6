#Ask the user to input a sentence and input the first word to remove in that sentence
sentence_input = str(input("Please input a sentence: "))
prefix_input = str(input("Please input the first word that you want to remove in the sentence: "))

#Print the sentence without the word that the user wants to remove
def remove_prefix(sentence_input, prefix_input):
    if prefix_input in sentence_input:
        return sentence_input.replace(prefix_input, "", 1) #Put a 1 in the end to only remove 1 instance of the world
    
    return sentence_input

print(remove_prefix(sentence_input, prefix_input))