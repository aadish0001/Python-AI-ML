list=[]
fail=False
for i in range(6):
    m=int(input())
    if m<35:
        fail=True
    list.append(m)
if fail==True:
    print("FAIL")
else:
    avg=sum(list)/5
    if avg>=75:
        print("DISTINCTION")
    else:
        print("PASS")
