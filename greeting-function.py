# What if we want to write a function to just say 'hello'
# handle of greeting instead of writing "hello" each time

# print(name)

# def greeting (name): # taking a single value as a 'parameter'
#     print(f"Hello {name}")

# greeting(name)

# we can give parameters default values too
# def greeting(to="World"):
#     print(f"Hello {to}")

# greeting()
# name = input("Whats your name? ").capitalize()
# greeting(name)

# def main():
#     name = input("Whats your name? ").capitalize()
#     hello(name)

# def hello(name="World"):
#     print(f"Hello {name}")

# main()

# SCOPE: a variable only existing in a context where we are defining it 
# For example: heres an error code lol to learn

# def main():
#     name = input("What's your name? ").capitalize() # here we are defining a name, only exists within this function
#     hello()

# def hello():
#     print("Hello", name)

# main()
# RESULT -> NameError: name 'name' is not defined
# Variables can only be accessed within the scope they are defined in
