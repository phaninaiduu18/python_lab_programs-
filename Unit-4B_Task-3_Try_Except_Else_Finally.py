# Unit 4B - Task 3: Try, Except, Else and Finally
try:
    number=int(input("Enter a number: "))
except ValueError:
    print("Error: Please enter a valid integer")
else:
    print("Square:",number*number)
finally:
    print("Program finished")
