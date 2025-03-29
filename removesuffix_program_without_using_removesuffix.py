#Ask the user to input a sentence 
sentence_input = str(input("Please input a sentence: "))

#Ask the user to input the suffix to remove in that input
suffix_input = str(input("Please input your suffix to remove it in the sentence: "))

#Print the sentence without the word that the user wants to remove
if sentence_input.endswith(suffix_input):
    sentence_input = sentence_input.replace(suffix_input, "", 1)

print(sentence_input)