hrs=input("Enter Hours:")
h=float(hrs)
rate=input("Enter Rate:")
r=float(rate)

if h>40:
    pay=h*r+.5*r*(h-40)
else:
    pay=h*r


print("Pay:",pay)
