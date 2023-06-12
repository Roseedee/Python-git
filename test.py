k=float(input("num"))
a=[1000,500,100,50,20,10,5,2,1,0.5,0.25]

for i in a:
    f=k//i
    g=f*i
    k=k-g
    # if f>0:
    #     print(i)
    if f>0:
        if i > 10 :
            print("is bank",(i),":",(f))
        else:
            print("is change",(i),":",(f)) 
if k >0 :
    print("dont have change",k)
    
