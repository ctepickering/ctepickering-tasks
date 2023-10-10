park=[["empty" for _ in range(6)] for i in range(10)] 
reg=input("please enter your registration number")
parked = False
valid = False
while not parked :
    while not valid:
        row = int(input("please enter what row your car is in "))
        space = int(input("please enter what space your car is in "))
        if 0<int(row)and 11>int(row)  and 0<int(space)and 7>int(space) :
            valid == True
        else :
            print("invalid input")
    if park[row][space] == "empty" :
        park[row][space] = reg
        parked = True
    else :
        print("space is taken, please enter another")
 
