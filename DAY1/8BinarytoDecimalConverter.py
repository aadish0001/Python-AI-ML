bn=input()
dn=0
power=0
for digit in reversed(bn):
    dn=dn+int(digit)*(2**power)
    power+=1
print(dn)