#displays 3 digit number in hundreds tens and units
usernum=0
while usernum <100 or usernum>999 :
    usernum = int(input("please enter a number between 100 and 999 "))
#end while
hundreds= str(usernum//100)+" hundreds, "
tens=str((usernum%100)//10)+ " tens and "
units = str(usernum%10)+" units"
print(hundreds+ tens + units)
