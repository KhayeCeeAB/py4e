score = input("Enter Score: ")
try:
    extrascore = float(score)
except:
    print("Error, the score is not numeric.")
    quit()
if extrascore < 0.0:
    print("Error, the score is out of range.")
elif extrascore > 1.0:
    print("Error, the score is out of range.")
elif extrascore >= 0.9:
    print("A")
elif extrascore >= 0.8:
    print("B")
elif extrascore >= 0.7:
    print("C")
elif extrascore >= 0.6:
    print("D")
elif extrascore < 0.6:
    print("F")
else:
    print("Bad Score")
