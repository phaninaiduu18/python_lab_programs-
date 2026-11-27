# Unit 4C - Task 5: Search and Replace a Word in a Text File
try:
    file=open("sample.txt","r")
    content=file.read()
    file.close()

    old_word=input("Enter the word to replace: ")
    new_word=input("Enter the new word: ")
    updated_content=content.replace(old_word,new_word)

    file=open("sample.txt","w")
    file.write(updated_content)
    file.close()

    print("Word replaced successfully")
    print("Updated file content:")
    print(updated_content)
except FileNotFoundError:
    print("sample.txt was not found. Keep it in the same folder as this program.")
