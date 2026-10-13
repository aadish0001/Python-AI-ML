n=input("Enter number")
rev_num="".join(reversed(n))
if n==rev_num:
    print("PALINDROME")
else:
    print("NOT PALINDROME")