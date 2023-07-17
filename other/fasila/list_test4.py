data = []
while True:
    print("=" * 20 , " BMI Calculator ", "=" * 20)
    print("1. Calculation")
    print("2. Show Data")
    print("3. Exit Program")
    print("=" * 58)
    choice = input("Please choose 1-3 : ")
    if choice == "1":
        print("=" * 20 , " Insert Data ", "=" * 20)
        name = input("Please input you name : ")
        height = float(input("Please input Height(cm.) : "))
        weight = float(input("Please input Weight(kg.) : "))

        bmi = weight / (height/100)**2

        gain = ""
        if bmi < 18.5:
            gain = "Thin"
        elif bmi >= 18.5 and bmi <= 22.9:
            gain = "Normal"
        elif bmi >= 23.0 and bmi <= 24.9:
            gain = "Buxom"
        elif bmi >= 25.0 and bmi <= 29.9:
            gain = "Fat"
        elif bmi >= 30.0:
            gain = "Very fat"
        
        data.append([name, height, weight, f"{bmi:.2f}", gain])

        print(f"Year BMI is {bmi:.2f} {gain}")

    elif choice == "2":
        print("=" * 22 , " BMI Detail ", "=" * 22)
        print("No.\tName\tHeight\tWeight\tBMI\tDetail")
        print("*" * 58)
        i = 1
        for n in data:
            print(i, "\t", end="")
            for d in n:
                print(d,"\t",end="")
            print()

    elif choice == "3":
        if input("Do you want to exit BMI Calculator (y/n)? : ") == "y":
            print("Thank you")
            break