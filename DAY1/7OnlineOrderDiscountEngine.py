am=int(input("Enter amount: "))
if am>=5000:
    print("amount payable: " , am-(am*0.20))
elif am>=3000:
    print("amount payable: ",am-(am*0.10))
elif am>=1000:
    print("amount payable:",am-(am*0.05))
else:
    print("amount payable: ",am)