class student:
    # def __init__(self,a,b):
    #     self.a=a
    #     self.b=b
    @classmethod
    def dataUpdate(cls,a,b):
        cls.a=a
        cls.b=b

    def disp(self):
        print("Value of a is :",self.a)
        print("Value of b is :",self.b)

  


print("Enter value for a")
a=input()
print("Enter value for b")
b=input()

obj=student()
obj.a=a
obj.b=b
obj.disp()



print("___________________________________________________________\n")

print("Enter value for a")
a=input()
print("Enter value for b")
b=input()
# obj2=student(a,b) 
obj2=student()
obj2.a=a
obj2.b=b
print("Data after in second obj ")
obj2.disp()

obj.dataUpdate(15,80)




print("Data  in obj1 : ")
obj.disp()

print("Data  in obj2 : ")
obj2.disp()


print("Value Of A in class",student.a)

# @classmethod modifies class-level data (student.a, student.b).
# Your objects use instance data (self.a, self.b).
# Therefore obj.dataUpdate(15,80) does not change obj.a and obj.b.
# Use a normal instance method if you want to update an object's attributes.1