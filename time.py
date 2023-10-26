a=int(input("enter the value of sec:"))
b=a//3600
a=a%3600

c=a//60
a=a%60

d=a//1
print("no of hours:",b)
print("no of minutes:",c)
print("no of second:",d)
