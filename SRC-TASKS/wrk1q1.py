#array declaration
num=[0 for _ in range(6)]
total=0
for i in range(6):
    num[i]=int(input("Please enter a number : "))
    total = total+num[i]
#next i

#reverse order
for i in range(5,-1,-1):
    print(num[i])
#next i
#average
print("Total :", total)
print("Average :" , total/6)