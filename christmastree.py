layers= int(input("Please enter the number of layers you want :"))
numSp = layers
for n in range(layers+1) :
    num= n* 2 -1
    print(numSp*" ",num *"*")
    numSp= numSp-1