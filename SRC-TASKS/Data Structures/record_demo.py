class student_record:
    def _init_(self):
        self.firstname=""
        self.surname=""
        self.age=0
        self.registered=False
    #end constructor
#end class

student1t=("Dave","Bloggs",18,True)

student2=student_record()
student2.firstname="Bob"
student2.surname="Smith"
student2.age=16
student2.registered=True

print
print(student1t[1])