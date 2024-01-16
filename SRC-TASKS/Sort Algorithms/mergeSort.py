alist = [1, 3, 4, 6, 8, 9]
blist = [2,5,12,14,17]
clist = [0 for _ in range(len(alist)+len(blist))]

def merge(clist, alist, blist) :
    pointer_a = 0
    pointer_b= 0
    pointer_c=0
    while pointer_a<=len(alist) and pointer_b<=len(alist):
        if alist[pointer_a] < blist[pointer_b]:
            clist[pointer_c]=alist[pointer_a]
            pointer_a = pointer_a+1
            pointer_c=pointer_c+1
        else:
            clist[pointer_c]=blist[pointer_b]
            pointer_a = pointer_a+1
            pointer_c=pointer_c+1
        #end if
        #end while
    print(clist)

#end procedure
merge(clist,alist,blist)