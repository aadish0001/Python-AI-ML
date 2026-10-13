n=int(input("Enter Number:"))
while n>=10:
    total=0
    while n>0:
        digit=n%10
        n=n//10
        total+=digit
    n=total
print(n)