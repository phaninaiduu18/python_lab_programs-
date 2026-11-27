# Unit 4B - Task 2: Multiple Except Blocks
numbers=[10,20,30]
try:
    index=int(input("Enter a list index: "))
    print("Value:",numbers[index])
except ValueError:
    print("Error: Please enter an integer")
except IndexError:
    print("Error: List index is out of range")
