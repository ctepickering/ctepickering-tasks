def fibbonacci(n): 
    if n== 0:
        return 0
    if n == 1:
        return 1
    return fibbonacci(n-1) + fibbonacci(n-2)
#endfunc
fibbonacci(100)