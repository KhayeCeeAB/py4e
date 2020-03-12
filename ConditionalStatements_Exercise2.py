hours = input("Enter Hours:")
try:
    extrahours = float(hours)
except:
    print("Error, please enter numeric input")
    quit()
rate = input("Enter Rate:")
try:
    extrarate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
if extrahours > 40:
    # print("Overtime")
    regular = extrahours * extrarate
    overtime = (extrahours - 40.0) * (extrarate * 0.5)
    pay = regular + overtime
else:
    # print("Regular")
    pay = extrahours * extrarate
print("Pay: ", pay)
