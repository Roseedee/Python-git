moneyPerMonth = int(input("Enter money : "))

#1
moneyPerYear = moneyPerMonth * 12
print("Money per year : ", moneyPerYear)

#2
moneyUse = moneyPerYear * 0.4
print("Money use(40%) : ", moneyUse)

if moneyUse <= 60000:
    moneyPerYear = moneyPerYear - moneyUse
else:
    moneyPerYear = moneyPerYear - 600000
    




