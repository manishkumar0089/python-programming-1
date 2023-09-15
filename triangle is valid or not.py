a=float(input("Enter the first side of triangle:"))
b=float(input("Enter the second side of triangle:"))
c=float(input("Enter the third side of triangle:"))
if a+b>c and a+c>b and b+c>a :
    print("the triangle with sides ",a,b,c,"is  valid")
else:
    print("the triangle with sides ",a,b,c,"is not valid")
