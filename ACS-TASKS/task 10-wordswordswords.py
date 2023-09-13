#input sentance from user
sentence=input("please enter a sentence : ")

#splits the words into spaces
words=sentence.split()

#calculates number of words
numwords=len(words)

#outputs back to user
print("There are " + str(numwords) + " words")