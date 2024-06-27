# TUPLES IN PYTHON

# It is a type of data structure, a container used to store different values.abs

# Tuplesare inmmuitable that is, they cannot be change or modified when created.

coordinatesS = (4, 5)
coordinates = (4, 5), (7, 8), (2,3), (5,6)

print(coordinates[3])

print(coordinatesS[1])

# we use Tuples for data that's never going to change

# FUNCTIONS

# These are collection of codes which performs specific tasks

def say_hi():
    print("Hello User")

say_hi()

# giving a parameter to a function, a parameter the piece of information given to a function.

def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

say_hi("Femi", "30")
say_hi("Fire", "31")


def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi("Mike", 28)
say_hi("Steve", 31)


# RETURN STATEMENT

# Helps us get information back from the function

def cube(num):
    return num*num*num

print(cube(3))

def cube(num):
    return num*num*num

result = (cube(3))
print(result)


# IF STATEMENTS IN PYTHON

# IF Statements help our programmes to respond to the input they are given


#I wake up 
#If I'm hungry
#    I eat breakfast

#I leave my house
#if it's cloudy
#    I bring an umbrella
#otherwise
#    I bring sunglasses

#Im at a restaurant
#if I want meat
#    I order a steak
#otherwise if I want pasta
#    I order spaghetti & meatballs
#otherwise
#    I order a salad.


 # creating an If variable

is_male = False # if the variable value was set to False it outputs 'You are not a male'

if is_male:
    print("You are a male")

else:
    print("You are not a male")

# Using the OR operator

is_male = True # if the variable value was set to False it outputs 'You are neither male nor tall'
is_tall = True # if the variable value was set to False it outputs 'You are neither male nor tall'

if is_male or is_tall:
    print("You are a male or tall or both")

else:
    print("You neither male nor tall")

# Using the AND operator, with this operator both variable values have to be true to print the if statement output

is_male = True # if one of the variable value was set to False it outputs 'You either not male or not tall or both'
is_tall = False 

if is_male and is_tall:
    print("You are a tall male")

else:
    print("You either not male or not tall or both")



is_male = True 
is_tall = False 

if is_male and is_tall:
    print("You are a tall male")

elif is_male and not(is_tall): # the NOT operator negatesthe variable in the parenthesis
    print("You are a short male")

elif not(is_male) and is_tall:
    print("You are not a male but are tall")

else:
    print("You are not a male and not tall")



