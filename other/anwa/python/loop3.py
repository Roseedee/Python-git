n = input("enter number(1-9) : ") #n : string

list = []
sum = 0

for x in n:
    list.append(int(x))
    sum += int(x)

list.sort()

print("max is : ", list[len(list) - 1])
print("sum is : ", sum)








