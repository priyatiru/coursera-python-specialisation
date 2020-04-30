def computepay(hrs,rate):
    if(int(hrs)<=40):
        return (pay)
    else:
        return (40*float(rate)+(float(hrs)-40)*1.5*float(rate))
hrs=float(input("Enter hours: "))
rate=float(input("Enter rate: "))

p=computepay(hrs,rate)
print("Pay "+str(p))
