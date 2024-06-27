# IF SATATEMENTS & COMPARISONS

# comparison operators 
# >= - greater than or equal to
# <= - lesser than or equal to
# == - equal to
# (!= - not equal to)
# > < - greater and less than


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 500, 250))


# BUILDING A CALCULATOR

#num1 = float(input("Enter a number: "))
#op = input("Enter an operator: ")
#num2 = float(input("Enter a second number: "))

#if op == "+":
#    print(num1 + num2)
#elif op == "-":
#    print(num1 - num2)
#elif op == "/":
#    print(num1 / num2)
#elif op == "*":
#    print(num1 * num2)
#else:
#print("Invalid operator")


# DICTIONARIES IN PYTHON: These are different data sture which allows us to save information in (Key-Value) pair
# The Key uniquely identifies it inside of the dictionary, while the Value is actually what it stands for

monthConversions = {
    
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}


print(monthConversions["Aug"])

print(monthConversions.get("Aug"))

print(monthConversions.get("You", "Not a valid Key"))

print(monthConversions[3])

print(monthConversions.get(2))


# While LOOP IN PYTHON
# A while Loop is a structure in python which allows us to loop a block of code multiple times, until a certian condition was False

i = 1
while i <=  10:
    print(i)
    i += 1

print("Done with Loop")

# Building a Guessing Game

#secret_word = "giraffe"
#guess = ""

#while guess != secret_word:
#    guess = input("Enter guess: ")

#print("You Win!")


#secret_word = "giraffe"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False

#while guess != secret_word and not(out_of_guesses):
#    if guess_count < guess_limit:
#        guess = input("Enter guess: ")
#        guess_count += 1
#    else:
#        out_of_guesses = True
#if out_of_guesses:
#    print("Out of Guesses, YOU LOSE!")
#else:
#    print("You Win!")


# FOR LOOP IN PYTHON

#friends = ["Jim", "Karen", "Kevin"]
#for friend in friends:
#    print(friend)


for index in range(10):
    print(index)

for index in range(4, 12):
    print(index)


friends = ["Jim", "Karen", "Kevin"]

for index in range(len(friends)):
    print(friends[index])


for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")