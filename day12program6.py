class Student:
    def __init__(name,college,course):
(pet1        name.college=college
        name.course=course
    def __str__(name):
        temp="Student is"+'name.college'+'and has'+str(name.course)+' course'
        return temp


if __name__=="__main__":
    person1=Student("subjects",6)
    print(person1.course)
    print(person1.college)
    print(person1)

    person2=Student("sems",4)
    print(person2.college)
    print(person2.course)
    print(person2)
