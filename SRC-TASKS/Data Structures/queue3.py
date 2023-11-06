class Queue:
    def __init__(self):
        self.data = []
        self.fp = 0
        self.rp = -1
    #end constructor
    def __repr__(self) -> str:
        return_str = ""
        ptr = self.fp
        while ptr != (self.rp + 1) % self.max_size: 
            return_str += str(self.data[ptr]) + " "
            ptr = (ptr + 1) % self.max_size
        #end while
        return return_str
    #end function
    def isEmpty(self):
        return self.size == 0
    #end function
    def isFull(self):
        return self.max_size == self.size
    #end function
    def enqueue(self, item):
        if not self.isFull():
            self.rp = (self.rp + 1) % self.max_size
            self.size += 1
            self.data[self.rp] = item
        else:
            print("queue full")
        #end if
    #end procedure
    def dequeue(self):
        if not self.isEmpty():
            item_p = self.fp
            self.fp = (self.fp + 1) % self.max_size
            self.size -= 1
            return self.data[item_p]
        else:
            print("Queue empty")
        #end if
    #end function
            
#end record