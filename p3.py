x=int(input("enter the x value"))
n=int(input("enter the n value"))
a=[]
for i in range(0,n):
    a.append(input("enter the values"))
p=a[-1]
i=n
for i in range(i,0,-1):
    p=a[i-1]+(x*p)
print(p)



