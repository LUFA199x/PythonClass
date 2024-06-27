import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul MaCartney", "George Harrison", "Ringo Star"]

# this function provides the extention of any file you give it

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

# this function simulates rolling a Dice, once given a 5 it gives a 5-sided dice 

def roll_dice(num):
    return random.randint(1, num)