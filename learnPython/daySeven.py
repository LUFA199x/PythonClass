# MODULES AND PIP

# a module is a python file that we can input into our current python file 

#import useful_tools

#print(useful_tools.roll_dice(10))

# PIP (package manager) is a programme that helps us to install, manage, update, and uninstall different python modules 

#pip --version - to confirm the version of pip installed 



# CLASSES & OBJECTS

#from Student import Student
# the line of code above means from the Student file import the Student class

#student1 = Student("Jim", "Business", 3.1, False)
#student2 = Student("Pam", "Art", 2.5, True)


#print(student1.name)
#print(student2.is_on_probation)


#BUILDING A MULTIPLE CHOICE QUIZ

from Question import Question


question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# creating an array of Question

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

# the function below will run the test, it has to ask the user the questions and check to see if they are right

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct") 

run_test(questions)