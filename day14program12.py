class Employee:
    empCount = 0
    def __init__(self, name, Salary):
        self.name = name
        self.Salary = Salary
        Employee.empCount += 1
    def displayCount(self):
        print ("Total Employees {0}".format( Employee.empCount))
    def displayEmployee(self):
        print ("Name : ",self.name, ", Salary: ",
               self.Salary)
emp1=Employee("Nikhil",9999)
emp1.displayEmployee()
emp1.Salary = 17000
emp1.Experience=3
emp1.displayEmployee()
emp1.name = 'Manoj'
emp1.displayEmployee()
print(emp1.Experience)
#del emp1.Salary
emp1.displayEmployee()
 
