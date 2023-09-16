class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def speak(self):
        print("Hello, my name is {} and I am from {}.".format(self.name, self.country))

class Student(Person):
    def __init__(self, name, country, major):
        super().__init__(name, country)
        self.major = major

    def speak(self):
        print("Hello, my name is {} and I am a {} major.".format(self.name, self.major))

person = Person("SolaOluwa", "Nigeria")
student = Student("Sunkanmi", "Nigeria", "Software Engineering")

person.speak()   # "Hello, my name is SolaOluwa and I am from Nigeria."
student.speak()  # "Hello, my name is John and I am a Software Engineering major."