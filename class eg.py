class student:
    num=0
    def __init__ (self,var):
        student.num+=1
        self.var=var
        print("The object value is = ", var)
        print("The count of object created = ", student.num)  
S1=student(15)
S2=student(35)
S3=student(45)
s4=student(56)