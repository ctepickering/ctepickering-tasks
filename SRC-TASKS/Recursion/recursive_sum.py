numbers=[3,6,2,8,1]
def RecursiveSum(arr,n):
    if n == -1 :
        return 0
    else :
        return arr[n]+RecursiveSum(arr,n-1)
    
print(RecursiveSum(numbers,(len(numbers)-1)))