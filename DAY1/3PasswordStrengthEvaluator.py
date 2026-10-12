password=input("Enter password: ")
digit=0
uc=0
for ch in password:
    if ch>='A' and ch<='Z':
        uc+=1
    if ch>="0" and ch<="9":
        digit+=1
if(uc>=1 and digit>=1):
    print("STRONG")
else:
    print("WEAK")
