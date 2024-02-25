x=0
y=0
a1=int(input("enter a value "))
b1=int(input("enter the b value"))
c1=int(input("enter the c value"))
a2=int(input("enter the a2 value"))
b2=int(input("enter the b2 value"))
c2=int(input("enter the c3 value"))
print("the two equations are eq1={}x+{}y={} \n second eqn is eq2={}x+{}y={}".format(a1,b1,c1,a2,b2,c2))
b2=b2-(a2*b1)/a1
c2=c2-(a2*c1)/a1
if(b2==0):
    print("no sol")
else:
    y=c2/b2
    x=(-c1-b1*y)/a1
    print(x)
    print(y)                 