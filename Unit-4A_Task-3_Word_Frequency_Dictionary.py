sentence=input("Enter a sentence: ").lower()
frequency={}
for word in sentence.split():
    frequency[word]=frequency.get(word,0)+1
print("Word frequency:")
for word,count in frequency.items():
    print(word,":",count)
