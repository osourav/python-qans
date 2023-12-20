"""
	Write a program that has a class Person. Inherit a class Faculty from Person which also has a class Publication. 
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}\n")


class Publication:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def display_info(self):
        print(f"Title: {self.title}, Year: {self.year}")


class Faculty(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position
        self.publications = []

    def display_info(self):
        print(f"Position: {self.position}")
        super().display_info()

    def display_publications(self):
        if self.publications:
            print("Publications:")
            for publication in self.publications:
                publication.display_info()
        else:
            print("No publications available.")


person1 = Person("Sourav", 22)
person1.display_info()

faculty1 = Faculty("God", 30, "Professor")
faculty1.display_info()

publication1 = Publication("Research Paper 1", 2022)
faculty1.publications.append(publication1)

publication2 = Publication("Research Paper 2", 2023)
faculty1.publications.append(publication2)

faculty1.display_publications()

    
"""
	------- output -------
    Name: Sourav, Age: 22

    Position: Professor
    Name: God, Age: 30

    Publications:
    Title: Research Paper 1, Year: 2022
    Title: Research Paper 2, Year: 2023

"""