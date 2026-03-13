# return: hands us back a value bc right now we are printing the value but I want this value to return to me

# wrote a simple calculator even tho it wasn't part of the course lol :)
def main():
    x = float(input("Enter your first number: "))
    z = input("Choose your operation(+, -, *, /): ")
    y = float(input("Enter your second number: "))
    result = calculate(x, z, y) # this function will give us a value back and we want to print that to the screen
    print(result)

def calculate(first, op, sec):
    if(op == "+"):
        result = first + sec
        return result
    elif(op == "-"):
        result = first - sec
        return result
    elif(op == "*"):
        result = first * sec
        return result
    elif(op == "/"):
        result = first / sec
        return result
    else:
        print("Incorrect operation. Choose between (+, -, *, /)")

main()

#___________________________________________________
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(val):
    return pow(n, 2)   #-> raises to power of two

main()