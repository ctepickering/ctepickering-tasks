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

def linearSearchRec(arr,item,i) :
    if i == len(arr) :
        return -1
    elif arr[i] == item :
        return i
    else :
        return linearSearchRec(arr,item, i+1)
    #end if
#end function