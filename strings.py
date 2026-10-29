text="Hello Python World"

print("Original String:", text)
print("upper:",text.upper())
print("Lower:",text.lower())
print("Strip:",text.strip())

words=text.strip().split()
print("Split:",words)
print("Join: ",  "-".join(words))
print("Replace:",text.replace("Python","programming"))
print("Find:",text.find("python")) 
