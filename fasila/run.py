waist = float(input("ขนาดเอว : "))
hip = float(input("สะโพก : "))
lenge = float(input("ความยาว : "))

if (waist >= 28 and waist <= 29) and (hip >= 30 and hip <= 32) and lenge == 12.5:
    print("you size is : S")
elif (waist >= 30 and waist <= 31) and (hip >= 33 and hip <= 35) and lenge == 13.0:
    print("you size is : M")
elif (waist >= 32 and waist <= 33) and (hip >= 36 and hip <= 38) and lenge == 14.0:
    print("you size is : L")
elif (waist >= 34 and waist <= 35) and (hip >= 39 and hip <= 41) and lenge == 14.5:
    print("you size is : XL")
elif (waist >= 36 and waist <= 37) and (hip >= 42 and hip <= 43) and lenge == 15.5:
    print("you size is : XXL")
else:
    print("No size")
