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
