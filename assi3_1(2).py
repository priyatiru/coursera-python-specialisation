hrs = input("ENTER HOURS: ")
rate = float(input())
pay= (float(hrs)*rate)
if(hrs<=40):
    print(pay)
else print(1.5*float(pay))
