k = float(input("money"))

tu=k//1000

k = k - (tu * 1000)

fh=k//500

h=(k-(fh*500+tu*1000))//100

ft=(k-(h*100+fh*500+tu*1000))//50

tv=(k-(ft*50+h*100+fh*500+tu*1000))//20

tn=(k-(tv*20+ft*50+h*100+fh*500+tu*1000))//10

f=(k-(tn*10+tv*20+ft*50+h*100+fh*500+tu*1000))//5

t=(k-(f*5+tn*10+tv*20+ft*50+h*100+fh*500+tu*1000))//2

o=(k-(t*2+f*5+tn*10+tv*20+ft*50+h*100+fh*500+tu*1000))//1

ftt=(k-(o*1+t*2+f*5+tn*10+tv*20+ft*50+h*100+fh*500+tu*1000))//0.5

tvf=(k-(ftt*0.5+o*1+t*2+f*5+tn*10+tv*20+ft*50+h*100+fh*500+tu*1000))//0.25

print(tu)
print(fh)
print(h)
print(ft)
print(tv)
print(tn)
print(f)
print(t)
print(o)
print(ftt)
print(tvf)