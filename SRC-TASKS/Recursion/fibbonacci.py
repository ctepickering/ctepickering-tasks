#iterative fibbonacci
def fibbonacciI(n): 
    for i in range(n):
        if i <2:
            num=1
            num2=num
            num3=num2
        else :
            num=num2+num3
            num3=num2
            num2=num

    return num
#endfunc
print(fibbonacciI(8))


#recursive fibbonacci
def fibbonacciR(n): 
    if n== 0:
        return 0
    if n == 1:
        return 1
    return fibbonacciR(n-1) + fibbonacciR(n-2)
#endfunc
print(fibbonacciR(8))


#recursive dynamic fibbonacci
fibDict={}
def fibbonacciRD(n): 
    if n<=1:
        fibDict[n]=1
        return 1
    else:
       fibDict[n]= fibbonacciRD(n-1) + fibbonacciRD(n-2)
       return fibbonacciR(n-1) + fibbonacciR(n-2)
#endfunc
fibbonacciRD(8)
print(fibDict)