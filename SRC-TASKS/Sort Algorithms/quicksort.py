def arrSwap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp 
#end procedure
    
def quickSplit(arr,ptr,pivot):
    direction = 1
    while ptr != pivot:
        if ((direction ==  1 and arr[ptr] > arr[pivot]) or
            (direction == -1 and arr[ptr] < arr[pivot])):
            arrSwap(arr, ptr, pivot)   #swap values                     
            temp = ptr #swap pointers
            ptr = pivot
            pivot = temp
            direction = direction * -1 #change direction
        #end if
        ptr += direction
    #end while
    return pivot
#end function
        
def quickSort(arr,left,right):
    if left >= right: 
        pass #base case reached
    else:
        pivotPos = quickSplit(arr,left,right)  
        quickSort(arr,left,pivotPos-1)
        quickSort(arr,pivotPos+1,right)
    #end if
#end procedure
                    
data = [1,12,10,3,5,2,9,7]
print(data)
quickSort(data,0,len(data)-1)
print(data)