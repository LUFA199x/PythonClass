## Python Loops, functions, modules and libraries
#### Loops (for/while): Loops are used to repeatedly run a block of code.
### for loop
Using the `for loop`, a piece of code is executed once for each element of a sequence (such as a list, string, or tuple).
Here is an example of a for loop that prints each programming language in a list:

`languages = ['Python', 'Go', 'JavaScript']`
`# for loop`
`for language in languages:`
`    print(language)`

##### Output:
`Python`
`Go`
`JavaScript`

### while loop
The `while` loop is used to execute a block of code repeatedly as long as a condition is True. Here's an example of a while loop that prints the numbers from 1 to 5:

`i = 1`
`n = 5`
`# while loop from i = 1 to 5`
`while i <= n:`
`print (i)`
`i = i + 1`

##### Output:
`1`
`2`
`3`
`4`
`5`

#### Functions
Functions are reusable chunks of code with argument/parameters and return values. Using the `def` keyword in Python, you can define a function. In your programme, functions can be used to encapsulate complex logic and can be called several times. Functions can also be used to simplify code and make it easier to read. Here is an illustration of a function that adds two numbers:

`` `# function has two arguments num1 and num2``
``def add_numbers(num1, num2):``
  ``  sum = num1 + num2``
    ``print('The sum is: ',sum)``
``# calling the function with arguments to add 5 and 2``
``add_numbers(5, 2) ``

##### Output:
`The sum is: 7`

#### Understanding Modules and Importing Libraries:
A module is a file in Python that contains definitions and statements. Modules let you arrange your code and reuse it across many apps. The Standard Library, a sizable collection of Python modules, offers a wide range of capabilities, such as file I/O, regular expressions, and more. Additional libraries can be installed using package managers like pip. You must import a module or library using the import statement in order to use it in your programme. Here is an illustration of how to load the math module and calculate a number's square root using the sqrt() function:

`import math`
`print(math.sqrt(16)) # 4.0`

#### File I/O
File I/O is used to read and write data to and from files on disk. The built-in Python function open() can be used to open a file, after which you can read from and write to it using methods like read() and write(). To save system resources, you should always close the file after you are done with it. An example of reading from a file and printing its content:

`f = open("90DaysOfDevOps.txt", "r")`
`print(f.read())`
`f.close()`


#### Exception Handing
Exceptions are runtime errors that happen when your programme runs into unexpected circumstances, such dividing by zero or attempting to access a list element that doesn't exist. Using a try/except block, you can manage exceptions in Python. The try block's code is run, and if an exception arises, the except block's code is run to handle the exception.
` try:`
`  f = open("90DaysOfDevOps.txt")`
`  try:`
`    f.write("Python is great")`
`  except:`
`    print("Something went wrong when writing to the file")`


## Python Data Structures and OOP
### Data Structures

Python includes a number of data structures for storing and organizing data. The following are some of the most common ones:

#### Lists:
Lists are used to store multiple items in a single variable. They can hold any type of collection of items (including other lists), and their elements can be accessed via an index. Lists are mutable, which means they can be changed by adding, removing, or changing elements. Here's an example of how to make a list and access its elements:

``thislist = ["apple", "banana", "orange"]``
``print(thislist[0]) # OUTPUT apple``
``print(thislist[2]) # OUTPUT orange``

#### Tuples:
Tuples are similar to lists, but they are immutable, which means they cannot be changed once created. They are frequently used to represent fixed sets of data. Tuples can be created with or without parentheses, but they are typically used to make the code more readable. Here's an example of a tuple and how to access its elements:

``my_tuple = (1, 2, "three", [4, 5])``
``print(my_tuple[0])   # OUTPUT 1``
``print(my_tuple[2])   # OUTPUT "three"``
``print(my_tuple[3][0]) # OUTPUT 4``

#### Dictionaries:
Dictionaries are yet another versatile Python data structure that stores a collection of key-value pairs. The keys must be unique and unchangeable (strings and numbers are common), and the values can be of any type. Dictionaries can be changed by adding, removing, or changing key-value pairs. Here's an example of creating and accessing a dictionary's values:

`my_dict = {"name": "Rishab", "project": "90DaysOfDevOps", "country": "Canada"}`
``print(my_dict["name"])   # OUTPUT "Rishab"``
``print(my_dict["project"])   # OUTPUT "90DaysOfDevOps"``
``print(my_dict["country"])  # OUTPUT "Canada"``

#### Sets:
Sets are used to store multiple items in a single variable. They are frequently used in mathematical operations such as union, intersection, and difference. Sets are mutable, which means they can be added or removed, but the elements themselves must be immutable and sets cannot have two items with the same value. Here's an example of how to make a set and then perform operations on it:

`my_set = {1, 2, 3, 4, 5}`
`other_set = {3, 4, 5, 6, 7}`
`print(my_set.union(other_set))  # {1, 2, 3, 4, 5, 6, 7}`
`print(my_set.intersection(other_set)) # {3, 4, 5}`
`print(my_set.difference(other_set))  # {1, 2}`

### Object Oriented Programming (OOP)

