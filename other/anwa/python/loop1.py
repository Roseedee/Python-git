l = 1
w_sum = 0
while l <= 6:
    print(l)
    w = float(input("-> "))
    w_sum += w
    print("weight sum : ", w_sum)
    if w_sum == 450:
        print("ok")
        break
    elif w_sum > 450:
        w_sum -= w
        print("over weight")
    else:
        l += 1




    




