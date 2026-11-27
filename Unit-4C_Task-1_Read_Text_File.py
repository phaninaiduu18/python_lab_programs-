# Unit 4C - Task 1: Read and Display a Text File
try:
    file=open("sample.txt","r")
    content=file.read()
    file.close()
    print("File content:")
    print(content)
except FileNotFoundError:
    print("sample.txt was not found. Keep it in the same folder as this program.")
