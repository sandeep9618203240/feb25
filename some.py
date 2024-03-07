x=int(input("enter the x value"))
n=int(input("enter the n value"))
a=[]
for i in range(n):
    o=int(input("enter the {} vlaue".format(i)))
    a.append(i)
p=a[-1]
for i in range(n,1,-1):
    p=a[i-1]+x*p
print("the value of evaluated polynomial expression is:{}".format(p))
