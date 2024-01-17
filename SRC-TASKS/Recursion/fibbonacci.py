#recursive fibbonacci
def fibbonacciR(n): 
    if n== 0:
        return 0
    if n == 1:
        return 1
    return fibbonacciR(n-1) + fibbonacciR(n-2)
#endfunc
print(fibbonacciR(4))
#iterative fibbonacci
def fibbonacciI(n): 
    for i in range(n):
        if i <3:
            num = 1
        else :
            num2=num
            num = num + num2
    return num
#endfunc
print(fibbonacciI(4))