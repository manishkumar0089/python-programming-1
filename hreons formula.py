a=float(input("enter the first side of triangle:"))
b=float(input("enter the second  side of triangle:"))
c=float(input("enter the third  side of triangle:"))
s=(a+b+c)/2
d=s*(s-a)*(s-b)*(s-c)
e=d**0.5
print("area of triangle havng sides",a,b,c,"is",e)
