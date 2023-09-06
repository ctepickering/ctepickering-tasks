#allows user to pick an option between 1 and 3 - repeats until user has done so
choice=0
while choice >3 or choice <1 :
    choice = int(input("Please enter a option between 1 and 3 "))
#end while
print("You have chosen option number " + str(choice))