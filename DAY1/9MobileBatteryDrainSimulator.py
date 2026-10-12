dpm=int(input("Drain per minute: "))
battery=0
minutes=0
for i in range(1000):
    battery+=dpm
    minutes+=1
    if battery>=100:
        break
print(minutes)