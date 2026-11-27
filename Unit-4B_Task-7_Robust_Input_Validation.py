# Unit 4B - Task 7: Robust Student Marks Validation
class InvalidMarksError(Exception):
    pass

try:
    marks=float(input("Enter student marks (0 to 100): "))
    if marks<0 or marks>100:
        raise InvalidMarksError("Marks must be between 0 and 100")
    if marks>=40:
        print("Pass")
    else:
        print("Fail")
except ValueError:
    print("Error: Please enter valid marks")
except InvalidMarksError as error:
    print("Error:",error)
finally:
    print("Marks validation completed")
