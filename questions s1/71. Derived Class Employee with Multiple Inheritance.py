"""
	Write a program to create a derived class employee derived from the class basicinformation (member variables are name, empid, and age) and departmentinformation (member variables are dept name, assigned work, and time to complete) using multiple inheritances. Create two objects of the employee class and print the details of individual objects. 
"""

class BasicInformation:
    def __init__(self, name, empid, age):
        self.name = name
        self.empid = empid
        self.age = age

class DepartmentInformation:
    def __init__(self, dept_name, assigned_work, time_to_complete):
        self.dept_name = dept_name
        self.assigned_work = assigned_work
        self.time_to_complete = time_to_complete

class Employee(BasicInformation, DepartmentInformation):
    def __init__(self, name, empid, age, dept_name, assigned_work, time_to_complete):
        BasicInformation.__init__(self, name, empid, age)
        DepartmentInformation.__init__(self, dept_name, assigned_work, time_to_complete)
    
    def display_info(self):
        print(f"Name: {self.name}, Id: {self.empid}, Age: {self.age}", end=", ")
        print(f"Dept: {self.dept_name}, Assigned Work: {self.assigned_work}, Time To Complete: {self.time_to_complete}")



employee1 = Employee("Sourav", 101, 22, "HR", "Recruitment", 10)
employee2 = Employee("God", 102, 30, "IT", "Programming", 8)

print("Employee 1 details:")
employee1.display_info()
print("Employee 2 details:")
employee2.display_info()

"""
	------- output -------
    Employee 1 details:
    Name: Sourav, Id: 101, Age: 22, Dept: HR, Assigned Work: Recruitment, Time To Complete: 10
    Employee 2 details:
    Name: God, Id: 102, Age: 30, Dept: IT, Assigned Work: Programming, Time To Complete: 8
"""