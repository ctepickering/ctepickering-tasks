sumnums=[7,4,6,8,1,5]

def quicksort(arr):
    pivot=len(arr)-1
    pointer=1
    while pointer != pivot :
        if arr[pivot]> arr[pointer]:
            temp = arr[pointer]
            arr[pointer]=arr[pivot]
            arr[pivot]=temp
            pivot = pivot-1 
            pointer = pointer+1
        else :
            pivot = pivot-1 
            pointer = pointer+1

print(quicksort(sumnums))