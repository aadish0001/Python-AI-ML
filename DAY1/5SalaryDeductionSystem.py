salary=int(input("Enter your Salary: "))
ld=int(input("Enter your Late Days: "))
ad=int(input("Enter your Absent Days: "))
deduction=0
if ld>10:
    deduction+=salary*0.10
elif ld>5:
    deduction+=salary*0.05
if ad>2:
    deduction+=salary*0.05
print(salary-deduction)
