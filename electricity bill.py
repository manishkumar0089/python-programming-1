a= float(input("Enter the unit of electricity used by User:"))
if a<=50:
    b=a*.50
elif a<=150:
    b=(a-50)*0.75+50*0.50
elif a<=250:
    b=(a-150)*1.20+ 100*0.75+50*0.50
else:
    b=(a-250)*1.50+100*1.20+100*0.75+50*0.50
b=b+0.2*b
print("The net amount to be paid with including tax is :",b)
