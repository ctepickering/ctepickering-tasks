class Queue:
    def __init__(self):
        self.data = []
        self.fp = 0
        self.rp = -1
    #end constructor
    def isEmpty(self):
        return len(self.data) == 0
    #end function
    def enqueue(self, item):
        self.data.append(item)
    #end procedure
    def dequeue(self):
        if not self.isEmpty():
            return self.data.pop(0)
        else:
            print("Queue empty")
        #end if
    #end function
            
#end record
new_q1 = Queue()
new_q2 = Queue()
print(new_q1.data)
print(new_q2.data)
for num in range(11,15):
    new_q1.enqueue(num)
#next num
for num in range(101,106):
    new_q2.enqueue(num)
#next num
print(new_q1)
print(new_q1.data)
print(new_q2.data)
new_q1.enqueue(15)
new_q1.enqueue(16)
new_q2.enqueue(150)
new_q2.enqueue(160)
print(new_q1.data)
print(new_q2.data)
for _ in range(6):
    print(new_q2.dequeue)
#next _
for _ in range(8):
    print(new_q2.dequeue)
#next _
print(new_q1.data)
print(new_q2.data)
new_q1.enqueue(20)
new_q2.enqueue(200)
print(new_q1.data)
print(new_q2.data)