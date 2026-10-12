T=int(input())
if T>90:
    T=T%90
if T<=30:
    print("RED")
elif T>=31 and T<=45:
    print("YELLOW")
else:
    print("GREEN")