# Unit 4B - Task 5: Raise ValueError for Negative Age
try:
    age=int(input("Enter your age: "))
    if age<0:
        raise ValueError("Age cannot be negative")
    print("Age:",age)
except ValueError as error:
    print("Error:",error)
