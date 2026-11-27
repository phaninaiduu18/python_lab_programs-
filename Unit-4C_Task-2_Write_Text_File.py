# Unit 4C - Task 2: Write Text to a File
text=input("Enter a line of text: ")
file=open("output.txt","w")
file.write(text+"\n")
file.close()
print("Text written successfully to output.txt")
