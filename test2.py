money = float(input("Enter Money(Bath) : "))
money_format = [1000, 500, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25]
for t in money_format:
    r = money // t
    money = money % t
    if t > 10 and r > 0:
        print("แบงค์ ", t, " จำนวน : ", r)
    elif t > 0 and r > 0:
        print("เหรียญ ", t, " จำนวน : ", r)
if money > 0:
    print(money, " ไม่มีเหรียญ")