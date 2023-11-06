maxSize = 6
q=["" for _ in range(maxSize)]
size = 0
maxItems=6
rear = -1
front = 0

def isEmpty() :
    if size == 0 :
        return True
    else :
        return False
    #end if
#end function
def isFull() :
    if size == maxSize :
        return True
    else :
        return False
    #end if
#end function
    
def enqueue(newItem) :
    if size == maxSize :
        print("Queue is full")
    else :
        rear = ( rear +1 ) % maxItems
        q[rear] =newItem
        size =size +1
    #end if
#end procedure

def dequeue() :
    if isEmpty():
        print("Queue is empty")
    else :
        output=q[front]
        front = front +1
        size =size -1
        return(output)
    #end if
#end function