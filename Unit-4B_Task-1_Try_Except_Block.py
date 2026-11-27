# Unit 4B - Task 1: Try-Except Block
try:
    result=10/0
    print("Result:",result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
