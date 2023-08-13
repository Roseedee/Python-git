
def c1():
    n1 = int(input("n1 : "))
    n2 = int(input("n2 : "))
    print(n1 , " + ", n2 , " = ", n1 + n2)

def c2():
    n1 = int(input("n1 : "))
    n2 = int(input("n2 : "))
    print(n1 , " - ", n2 , " = ", n1 - n2)


while 1:
    print("1. +\n2. -\nx. end")
    choose = input("Enter number : ")
    if choose == '1':
        c1()
    elif choose == '2':
        c2()
    elif choose == 'x':
        break