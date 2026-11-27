students={1:{"name":"Anu","marks":85},2:{"name":"Ravi","marks":90},3:{"name":"Kiran","marks":78}}
for roll,details in students.items():
    print("Roll Number:",roll)
    print("Name:",details["name"])
    print("Marks:",details["marks"])
    print()
