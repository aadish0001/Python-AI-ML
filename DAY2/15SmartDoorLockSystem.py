correct_pin=int(input("Enter Correct PIN: "))
for i in range(3):
    password=int(input("Enter password: "))
    if password==correct_pin:
        print("ACCESS GRANTED")
        break
    else:
        print("Incorrect PIN")
else:
    print("CARD BLOCKED")

