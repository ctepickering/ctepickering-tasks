#user inputs number
count = 0
user_num=int(input("Please enter a number to see their factors : "))
#checks if every number up to user_num is a factor
for i in range(user_num):
    if user_num % (i +1)== 0:
        #eliminates 1 and the same number as they arent factors
        if i +1 == 1 or i+1 == user_num:
            next
            if count == 0 and user_num == i+1:
                print("This number has no factors")
            #end if
        else :
            print(i+1)
            count=count+1
        #end if
    #end if