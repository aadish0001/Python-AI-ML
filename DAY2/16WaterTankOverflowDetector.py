list=[]
n=int(input())
for i in range(n):
    num=int(input())
    list.append(num)
flow=0
min=0
for l in list:
    flow+=l
    min+=1
    if(flow>=1000):
        print(min)
        break