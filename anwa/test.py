money = int(input())

b1000 = money // 1000

money = money - b1000 * 1000

b500 = money // 500

money = money - b500 * 500

print("1000 : ", b1000)
print("500 : ", b500)