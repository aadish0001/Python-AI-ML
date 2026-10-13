sentence=input("Enter sentence:")
sentence=sentence.lower()
count=0
for ch in sentence:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        count+=1
print(count)