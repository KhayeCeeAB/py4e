def computepay(hours, rate) :
    if hours > 40:
        # print("Overtime")
        regular = hours * rate
        overtime = (hours - 40.0) * (rate * 0.5)
        pay = regular + overtime
    else:
        # print("Regular")
        pay = hours * rate
    return pay

h = input("Enter Hours: ")
r = input("Enter Rate: ")
eh = float(h)
er = float(r)

p = computepay(eh, er)

print("Pay: ", p)
