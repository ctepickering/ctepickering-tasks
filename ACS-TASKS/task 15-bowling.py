#bowling game
scores=[]
for turns in range(10):
    frame()

def frame() :
    totalscore=0
    turn1 =0
    print("Frame " + str(turns) + ": ")
    #prints which frame you are on e.g 'Frame 1:'
    turn1 = input("Please enter the number of pins you have knocked down")
    