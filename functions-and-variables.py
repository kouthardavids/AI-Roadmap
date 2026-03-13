# Harvard CS50’s Introduction to Programming with Python – Full University Course
# DAY 1: UNDERSTANDING FUNCTIONS AND VARIABLES

print("Hello World") #print command is a function (print())

# argument is a input to a function that influences its behaviour
print("argument")
#___________________________________________________

input("What's your name? ")
#___________________________________________________

# return values: function sends back a result where it was called after it finishes running
# but we need to store that return value our function hands back to us in a 'variable'
# what is a variable??
# a variable is a container used to store data values -> store it in the computers memory

name = input("What is your name? ")
print("Hey there,"+ name.capitalize()) # concatenation

# Data Types: Int -> integer(whole numbers)
# make your code readable and simple
x = int(input("Whats's x?")) # -> input must contain a number(not a string)
y = int(input("What's y? "))
print(x+y)
# OR
print(int(input("Whats's x?")) + int(input("What's y? "))) # yes we made it into one line of code, but still too much nested and kind difficult to read

# Data Types -> float(numbers that contain decimal point)
x = float(input("What's x? "))
y = float(input("What's y? "))
# z = round(x + y)
# print(z)
# print(f"{z:,}") -> 1000 -> 1,000

# Divison:
# z = x / y
# print(z)    #->   What's x? 4
                # What's y? 3
                # 1.3333333333333333 -> we want to round it off (this floating point, two just 2 decimal pts.)

# z = round(x / y, 2)
# print(z) # -> 1.33

z = x / y
print(f"{z:.2f}")
