

#EXPONENT FUNCTION IN PYTHON

#def raise_to_power(base_num, pow_num):
#    result = 1
#    for index in range (pow_num):
#        result = result * base_num
#    return result

#print(raise_to_power(2, 3))


# 2D LISTS & NESTED LOOPS
# 2 dimensional list

#number_grid =[
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#    [0]

#]

#print(number_grid[0][0])

# access value with columns and rows

# NESTED LIST

# this is having a For Loop inside of a For Loop

#        print (col)



# BUILDING a TRANSLATOR

# GIRAFFE LANGUAGE

# vowel = g

# --------------------

# dog - dgg
# cat = cgt



#def translate(phrase):
#    translation = ""
#    for letter in phrase:
#        if letter in "AEIOUaeiou":
#            translation = translation + "g"
#        else:
#            translation = translation + letter
#    return translation

#print(translate(input("Enter a phrase: ")))


##def translate(phrase):
##    translation = ""
##    for letter in phrase:
##        if letter.lower() in "aeiou":
##            if letter.isupper():
##                translation = translation + "G"
##            else:         
##                translation = translation + "g"
##        else:
##            translation = translation + letter
##    return translation

##print(translate(input("Enter a phrase: ")))



#  Caughting Errors in Python, using Try except

#try:

#    numbers = int(input("Enter a number: "))
#    print(numbers)
#except:
#    print("Invalid Input")


#try:
#    value = 10/0
#    number = int(input("Enter a number: "))
#    print(number)
#except ZeroDivisionError:
#    print("Divided by zero")
#except ValueError:
#    print("Invalid Input")



#try:
#    anwser = 10/0
#    number = int(input("Enter a number: "))
#    print(number)
#except ZeroDivisionError as err:
#    print(err)
#except ValueError:
#    print("Invalid Input")


# Reading from external files in Python

# employee_file = open("README.md", "r")

# employee_file.close()

# To extract information from a file, always ensure your confirm that a file is readable before attempting to extract info from such file


##employee_file = open("README.md", "r")

##print(employee_file.readable())

##employee_file.close()



###employee_file = open("README.md", "r")

###print(employee_file.read())

###employee_file.close()

# reads every line within the file upon everytime we use the print command

####employee_file = open("README.md", "r")

####print(employee_file.readline())

####employee_file.close()


# reads every line in the file and put them in an array 
####employee_file = open("README.md", "r")

####print(employee_file.readlines())

####employee_file.close()


# reads every line in the file and put them in an array, to refer to a specific line within the file by using its index, for example; [1]

#employee_file = open("README.md", "r")

#employee_file.readlines()[1]

#employee_file.close()

# you can also use the readlines attribute with the For Loop

#employee_file = open("Redmi.txt", "r")

#print(employee_file)

#employee_file.close()


# Writing and appending to files in Python, note that 'a' appends to existing files

employee_file = open("Redmi.txt", "a")

employee_file.write("Kelly - Customer Service")

employee_file.close()

# \n - this appends the new data on an entirely new line

employee_file = open("Redmi.txt", "a")

employee_file.write("\nKelly - Customer Service")

employee_file.close()


# using 'w' this will overwrite the entire existing file

employee_file = open("Redmi.txt", "w")

employee_file.write("\nKelly - Customer Service")

employee_file.close()


# we can also use 'w' to create a new file, just like in the example below 

employee_file = open("RedmiAndApple.txt", "w")

employee_file.write("\nKelly - Customer Service")

employee_file.close()
