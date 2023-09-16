class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country
person = Person("Rishab", "Canada")
<<<<<<< HEAD
# print(person.name)   # OUTPUT "Rishab"
# print(person.country)    # OUTPUT "Canada"
=======
>>>>>>> 03ddf4637d0fde033e89602b08b27dd36b8b8b2a

class Student(Person):
    def __init__(self, name, country, major):
        super().__init__(name, country)
        self.major = major

student = Student("SolaOluwa", "Nigeria", "Software Engineering")
print(student.name)   # OUTPUT "Rishab"
print(student.country)    # OUTPUT "Canada"
print(student.major)  # OUTPUT "Computer Science"
