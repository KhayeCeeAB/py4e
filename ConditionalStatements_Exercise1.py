hours = input("Enter Hours:")
rate = input("Enter Rate:")
extrahours = float(hours)
extrarate = float(rate)
if extrahours > 40:
    # print("Overtime")
    regular = extrahours * extrarate
    overtime = (extrahours - 40.0) * (extrarate * 0.5)
    pay = regular + overtime
else:
    # print("Regular")
    pay = extrahours * extrarate
print("Pay: ", pay)
