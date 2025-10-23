import math

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b
def modulus(a, b):
    return a % b
def power(a, b):
    return a ** b
def average(a, b):
    return (a + b) / 2
def maximum(a, b):
    return max(a, b)
def minimum(a, b):
    return min(a, b)
def square_root(a):
    if a < 0:
        return "Error! Square root of negative number."
    return math.sqrt(a)

while True:
  print("\nAvailable operations: +, -, *, /, %, **, avg, max, min, sqrt, exit")
  operation = input("Enter operation: ").lower()

  if operation == "exit":
        print("Calculator closed. Goodbye! 👋")
        break

    # Ask for inputs based on the operation type
  elif operation == "sqrt":
        a = float(input("Enter number: "))
        print("Result:", square_root(a))

  elif operation in ["+", "-", "*", "/", "%", "**", "avg", "max", "min"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if (operation == "+"):
          print(add(a, b))
        elif operation == "-":
           print(subtract(a, b))
        elif operation == "*":
          print( multiply(a, b))
        elif operation == "/":
          print(divide(a, b))
        elif operation == "**":
          print(power(a, b))
        elif operation == "avg":
          print(average(a, b))
        elif operation == "max":
          print(maximum(a, b))
        elif operation == "min":
          print(minimum(a, b))  
        else:
          print("Invalid operation")

