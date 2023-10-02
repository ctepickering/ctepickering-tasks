letters=[]
for i in range(5):
   letter = input("please enter a lowercase letter : ")
   letters.append(letter)
for i in range(len(letters)):
   for c in range(len(letters)-1):
      if ord(letters[c]) > ord(letters[c+1]):
         temp = letters[c+1]
         letters[c]=letters[c+1]
         letters[c]=temp
print(letters)
