sentence = (input('Enter a sentence:')) # ask user for a sentence
capital_sentence = sentence.upper() # capitalize the sentence
contains_sentence = "python" in sentence # check if "python" is in the sentence

print("Your sentence's number of characters is", len (sentence))

print("your capitalized sentence is:", capital_sentence)

# prints true if word "python" written in lowercase when mixed or uppercase prints false
print("Does your sentence contain the word 'python'?", contains_sentence)