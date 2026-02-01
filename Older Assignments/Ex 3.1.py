hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter Rate:"))

if h > 40:
    pay = rate * 40
    print("Pay:", pay)
    ot = (rate * 1.5) * (h - 40)
    print("Overtime:", ot)
    total = pay+ot
    print("Total:", total)
else:
    pay = rate * (h - 40)
    print("Pay:", pay)
