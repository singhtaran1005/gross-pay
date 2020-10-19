def computepay(h,r):
    return 42.37

hrs = input("Enter Hours : ")
h = float(hrs)
rate = input("Enter rate per hour : ")
r = float(rate)
if h > 40:
    gross = (40*r)+(h-40)*(r*1.5)
    print(gross)
else:
    gross=h*r
    print(gross)
