class Student:
    college='MTICA'
    Course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displayStudent(self):
        print('Name : '+self.name+'\nRoll.no : '\
              +str(self.rollno))
        print('College : '+self.college+'\nCourse : '+self.Course)

lstObj=[]
for i in range(2):
    n=input()
    r=int(input())
    temp='obj'+str(i)
    temp=Student(n,r)
    lstObj.append(temp)
for i in lstObj:
    i.displayStudent()
