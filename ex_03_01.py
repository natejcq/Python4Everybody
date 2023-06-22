hrs = input("Enter Hours:")
rates = input("Enter base hourly rate:")
try:
    h = float(hrs)
    r = float(rates)
except: 
    print("PLEASE ENTER NUMERIC INPUTS")

if(h<=40) :
    pay = h*r
    print(pay)
else : 
    pay = 40*r
    r = r*1.5
    pay = pay + (h-40)*r
    print(pay)
