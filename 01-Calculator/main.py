import sys

#Step 1: Display the menu.
print("===== Calculator =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#Step 2: Define the functions for each operation.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def invaild_op():
    print("Invalid Operation!")

#Step 3: Get user input for the operation
operation = int(input("Choose an operation: "))
if operation < 1 or operation > 4:
    invaild_op()
    sys.exit()

#Step 4: Get user input for the numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#Step 5: Perform the operation based on user input, and print Answer
if operation == 1:
    print("Answer:", add(a, b))
elif operation == 2:
    print("Answer:", subtract(a, b))
elif operation == 3:
    print("Answer:", multiply(a, b))
elif operation == 4:
    print("Answer:", divide(a, b))
