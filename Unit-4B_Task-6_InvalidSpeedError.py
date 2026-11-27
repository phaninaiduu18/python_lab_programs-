# Unit 4B - Task 6: User-Defined InvalidSpeedError
class InvalidSpeedError(Exception):
    pass

try:
    speed=float(input("Enter vehicle speed (0 to 120 km/h): "))
    if speed<0 or speed>120:
        raise InvalidSpeedError("Speed must be between 0 and 120 km/h")
    print("Valid speed:",speed,"km/h")
except ValueError:
    print("Error: Please enter a valid number")
except InvalidSpeedError as error:
    print("Error:",error)
