class Student(Person):
    def __init__(self, name, country, major):
        super().__init__(name, country)
        self.major = major

student = Student("Rishab", "Canada", "Computer Science")
print(student.name)   # OUTPUT "Rishab"
print(student.country)    # OUTPUT "Canada"
print(student.major)  # OUTPUT "Computer Science"