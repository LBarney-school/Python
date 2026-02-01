def computepay(h, r):
    pay = h * r
    if h > 40:
        ot = (r * 0.5) * (h - 40)
        pay = ot + pay
    return pay

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
p = computepay(hrs, rate)
print("Pay", p)