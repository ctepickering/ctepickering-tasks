#user enters a sentence to be cyphered
cypher = ""
sentence = input("Please enter a sentence to be encrypted : ")
for i in range (len(sentence)) :
    if sentence[i]== " ":
        cypher=cypher+" "
    else:
        letter = ord(sentence[i])
        letter=letter+1
        cypher=cypher+chr(letter)
    #endif
#next i
print("The encrypted sentence is : " + cypher)