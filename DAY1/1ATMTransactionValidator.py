balance = int(input("Enter current balance: "))
n = int(input("No. of transactions: "))

list = []

for i in range(n):
    amount = int(input())
    list.append(amount)

for amount in list:
    if amount % 100 == 0 and balance >= amount:
        balance -= amount
        print("SUCCESS")
    else:
        print("FAILED")

print(balance)