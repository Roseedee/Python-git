salary = float(input("ใส่เงินเดือน >> "))
netSalary = salary * 12
expenses = 0.4 * netSalary

if expenses <= 60000:
    netSalary -= expenses
else:
    netSalary -= 60000

netSalary -= 30000

if netSalary >= 0 and netSalary <= 150000:
    tax = 0
elif netSalary >= 150001 and netSalary <= 300000:
    tax = netSalary*0.05
elif netSalary >= 300001 and netSalary <= 500000:
    tax = (netSalary - 150000)*0.1
elif netSalary >= 500001 and netSalary <= 750000:
    tax = (netSalary - 300000)*0.15
elif netSalary >= 750001 and netSalary <= 1000000:
    tax = (netSalary - 500000)*0.2
elif netSalary >= 1000001 and netSalary <= 2000000:
    tax = (netSalary - 750000)*0.25
elif netSalary >= 2000001 and netSalary <= 4000000:
    tax = (netSalary - 1000000)*0.3
elif netSalary >= 4000001:
    tax = (netSalary - 2000000)*0.35

print("ภาษีที่ต้องจ่าย : {:,} บาท".format(tax))