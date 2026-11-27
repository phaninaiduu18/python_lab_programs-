student={"name":"Ravi","age":20,"course":"Python"}
print("Keys:",student.keys())
print("Values:",student.values())
print("Items:",student.items())
print("Course:",student.get("course"))
student.update({"age":21})
print("After update:",student)
student.pop("course")
print("After pop:",student)
