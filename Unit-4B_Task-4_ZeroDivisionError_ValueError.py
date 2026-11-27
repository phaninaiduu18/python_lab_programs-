# Unit 4B - Task 4: Handle ZeroDivisionError and ValueError
try:
    numerator=float(input("Enter numerator: "))
    denominator=float(input("Enter denominator: "))
    print("Result:",numerator/denominator)
except ZeroDivisionError:
    print("Error: Denominator cannot be zero")
except ValueError:
    print("Error: Please enter valid numbers")
