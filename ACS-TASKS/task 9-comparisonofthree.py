#3 numbers input, outputs numbers highest to lowest
num = ["","",""]
for i in range(3) :
    num[i]= int(input("please enter a number "))
#next i
#sorts numbers
num.sort(reverse=True)
print(str(num[0])+", "+ str(num[1])+", "+ str(num[2]))