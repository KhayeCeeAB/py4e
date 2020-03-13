def computegrade (score) :
    try:
        extrascore = float(score)
    except:
        return("Error, the score is not numeric.")
        quit()
    if extrascore < 0.0:
        return("Error, the score is out of range.")
    elif extrascore > 1.0:
        return("Error, the score is out of range.")
    elif extrascore >= 0.9:
        return("A")
    elif extrascore >= 0.8:
        return("B")
    elif extrascore >= 0.7:
        return("C")
    elif extrascore >= 0.6:
        return("D")
    elif extrascore < 0.6:
        return("F")
    else:
        return("Bad Score")

print(computegrade(input("Enter Score: ")))
