count = 0
sum = 0.0
while True:
    value = input("Enter a number: ")
    if value == 'done':
        break
    try:
        extravalue = float(value)
    except:
        print("Invalid input")
        continue

    count = count + 1
    sum = sum + extravalue

print("Sum: " + str(sum), "Count: " + str(count), "Average: " + str(sum/count))
