# record class initiated
class student_record:
    def _init_(self):
        self.firstname=""
        self.surname=""
        self.age=0
        self.registered=False
    #end constructor
#end class

#write a section of the record in 2 ways 

student1t=("Dave","Bloggs",18,True) #ordered

student2=student_record()
student2.firstname="Fred"
student2.surname="Smith"
student2.age=16
student2.registered=True

# each value can be referenced by their ordered value e.g [0] or name e.g. .age
print(student2.age)
print(student1t[2])