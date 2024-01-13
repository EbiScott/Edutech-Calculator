#Basic Calculator made with Python

#Funtions
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y





#Main

print("Welcome to the Calculator!")

print("""Operations:
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division""")

choice = int(input("Pick an operation: "))

try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
except ValueError:
    print("You haven't entered a number")
    exit()
else:
    if choice == 1:
        print(addition(first, second))
    elif choice == 2:
        print(subtraction(first, second))
    elif:
        print(multiplication(first, second))
    elif choice == 4:
        print(division(first, second))
    else:
        print("You haven't entered a valid operation!")