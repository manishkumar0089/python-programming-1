a= input("Enter the employee name:")
b=int(input("Enter the salary :"))
if b<=10000:
    HRA=0.2*b
    DA=0.8*b
elif b<=20000:
    HRA=0.25*b
    DA=0.9*b
else:
    HRA=0.3*b
    DA=0.95*b
gross_salary = b+ HRA+ DA
print("the gross salary of employee:",gross_salary)
