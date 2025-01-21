def linearSearch(arr,item):
    i = 0
    found = False
    while not found and i < len(arr):
        if arr[i]== item:
            return i
        else :
            i = i +1
        #end if 
    #end while
    if not found :
        return -1
    #end if
#end function
index = 0
item = 5
arr = [1,2,6,7,8,3,4,55,6,3,5,1,5,8,9,10,4]
def linearSearchRec(arr,item,i) :
    if i == len(arr) :
        return -1
    elif arr[i] == item :
        return i
    else :
        return linearSearchRec(arr,item, i+1)
    
print(linearSearchRec(arr, item, index))
