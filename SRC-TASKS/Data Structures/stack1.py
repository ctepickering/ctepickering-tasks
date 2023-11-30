name = ['r','o','b','e','r','t']
stack= []
outName=[]
for c in name:
    stack.append(c)
for index in range(0,len(stack)):
    print
    outName.append(stack.pop())

class Stack:
    def __init__(self,size) -> None:
        self.maxSize=size
        self.data=[''for _ in range(size)]
        self.sp=-1

    def size(self):
        return self.sp+1
    def isFull(self):
        return self.size() == self.maxSize

    def isEmpty(self):
        return self.sp == -1

    def push(self, item):
        if self.isFull():
            print("is full")
        else:
            self.sp += 1
            self.data[self.sp] = item

    def pop(self):
        if self.isEmpty():
            print("is empty")
        else:
            temp = self.sp
            self.sp -= 1
            return self.data[temp]

    def peek(self):
        if self.isEmpty():
            print("is empty")
        else:
            return self.data[self.sp]
            
myString = input("Please enter a word or phrase")
numChars = len(myString)
s = Stack(numChars)
palList=[]
for c in myString :
    s.push(c)
while not s.isEmpty():
    palList.append(s.pop)

print(''.join(palList))
if myString ==''.join(palList):
    print("IS palindrome")
else:
    print("IS NOT palindrome")