rows, cols = (6, 4)   
pos = [["x" for i in range(cols)] for j in range(rows)]  

for x in range(rows) :
    for y in range(cols) :
        if x == 0 and y ==0 :
            pos[x][y] = "O"
        else :
            pos[x][y] = "x"
    print(pos[x][0]," ",pos[x][1]," ",pos[x][2]," ",pos[x][3]," ")
row= input("please enter a row ")
column=input("please enter a column ")
for x in range(rows) :
    for y in range(cols) :
        if x == (int(row)-1) and y ==(int(column)-1) :
            pos[x][y] = "O"
        else :
            pos[x][y] = "x"
    print(pos[x][0]," ",pos[x][1]," ",pos[x][2]," ",pos[x][3]," ")