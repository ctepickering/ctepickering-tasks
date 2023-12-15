myList=[4,23,56,72,102,167,193,206,255,283]

def BinarySearchRecursive(arr,item) :
    if len(arr) == 1 :
        if arr[0]== item :
            return 0
        else:
            return -1
    else : 
        mid = len(arr) // 2 - 1
        if arr[mid] == item:
            return mid
        elif arr[mid]>item :
            return BinarySearchRecursive(arr[0:mid],item)
        else:
            return BinarySearchRecursive(arr[mid+1:],item)
        #end if
    #end if
#end function
        
print(BinarySearchRecursive(myList,102))