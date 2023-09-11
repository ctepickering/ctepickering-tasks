#user enters number between 1 and 10 and it outputs first 10 values
i = 0
usernum=0
while usernum <1 or usernum>10 :
    usernum = int(input("please enter a number between 1 and 10 "))
#end while
while i < 10 :
    i = i +1
    multinum=i*usernum
    print(multinum)
#end while