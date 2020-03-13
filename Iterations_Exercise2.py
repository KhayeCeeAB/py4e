count = 0
sum = 0.0
value = 0
lst = []

while True:
    value = input("Enter a number: ")
    if value == 'done':
        break
    try:
        extravalue = float(value)
    except:
        print("Invalid input")
        continue
    lst.append(extravalue)
    count = count + 1
    sum = sum + extravalue

print("Sum: " + str(sum), "Count: " + str(count), "Minimum: " + str(min(lst)), "Maximum: " + str(max(lst)))
