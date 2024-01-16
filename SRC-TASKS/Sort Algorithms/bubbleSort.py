arr= [7,4,6,8,1,5]
def swap(a,b,arr):
    temp = arr[b]
    arr[b]=arr[a]
    arr[a]=temp
#end procedure
names = ['Sophie', 'Lily', 'Jessica', 'Isabella', 'Ava', 'Poppy', 'Emily', 'Isla', 'Olivia', 'Amelia']

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i) :
            if arr[j] > arr[j+1]:
                swap(j,j+1,arr)
            #end if
        #next j
    #next i
#end procedure