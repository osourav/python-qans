"""
	Write a program that has a class Student for storing roll number, name, and marks in five subjects of a student. Display the information stored about the student. 
"""

class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        print(f"Marks: {', '.join(map(str, self.marks))}")


name = input("Enter student name: ")
roll = int(input("Enter student roll number: "))
marks = input("Enter marks separated by spaces: ")

student1 = Student(roll, name, [x for x in marks.split()])
student1.display_info()
    
"""
	------- output 1 -------
    Enter student name: Sourav
    Enter student roll number: 2
    Enter marks separated by spaces: 80 76 92 85 72
    Roll Number: 2
    Name: Sourav
    Marks: 80, 76, 92, 85, 72

	------- output 2 -------
    Enter student name: God 
    Enter student roll number: 1
    Enter marks separated by spaces: 99 98 99 100 100
    Roll Number: 1
    Name: God
    Marks: 99, 98, 99, 100, 100
"""