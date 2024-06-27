# MAD LIBS GAME


#color = input("Enter a color:")
#plural_noun = input("Enter a Plural Noun:")
#celebrity = input("Enter a celebrity:")

#print("Roses are "+ color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)

# LISTS

# A list is a structure in python that we can use to store a list of information. So, we can take a bunch of data values, put them into a list organise them and keep track of them easier.

#friends =["Kemi", "Femi", "Vivian", True, 2.5]

# all = ["Alagomeji", "True", 2.5]

#print(friends) # ["Kemi", "Femi", "Vivian"]
#print(friends[1]) # Femi
#print(friends[-3]) # Kemi
#print(friends[1:]) # ["Femi", "Vivian"]
#print(friends[1:4]) # ["Femi", "Vivian", True, 2.5]

# To modify values inside of a List
#friends[1] = "Alagomeji" # Alagomeji

#print(friends[1])

# LIST FUNCTIONS

lucky_numbers =[42, 8, 15, 6, 23, 2]
friends =["Kemi", "Yuki", "Femi", "Vivian", "Yuki", "Alonso"]

# friends.extend(lucky_numbers) # extend a list

# friends.append("Inoske") # addan item to the end of the list

#friends.insert(1, "Slayer") # add to a list at any point

# friends.remove("Femi") # to remove the item in the parenthesis

# friends.pop() #Remove athe last item of the list

lucky_numbers.sort() # to arrange the values in ascending order.

friends.sort() # to arrange the values in ascending order.

print(friends.index("Vivian")) # to figure outif a value is in the list

print(friends.count("Yuki")) # to figure out how often a value appears on the list.

lucky_numbers.reverse() # to reverse the list

friends2 = friends.copy() # generates a copy of the original list.

# friends.clear() # Gives an empty set

print(friends)

print(lucky_numbers)

print(friends2)


