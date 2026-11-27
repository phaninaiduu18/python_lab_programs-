# Unit 4C - Task 4: Copy Content from sample.txt to copy.txt
try:
    source=open("sample.txt","r")
    content=source.read()
    source.close()
    destination=open("copy.txt","w")
    destination.write(content)
    destination.close()
    print("File content copied successfully to copy.txt")
except FileNotFoundError:
    print("sample.txt was not found. Keep it in the same folder as this program.")
