# Unit 4C - Task 3: Count Lines, Words and Characters in a Text File
try:
    file=open("sample.txt","r")
    content=file.read()
    file.close()
    lines=len(content.splitlines())
    words=len(content.split())
    characters=len(content)
    print("Number of lines:",lines)
    print("Number of words:",words)
    print("Number of characters:",characters)
except FileNotFoundError:
    print("sample.txt was not found. Keep it in the same folder as this program.")
