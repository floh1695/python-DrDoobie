result = float
success = bool

def mainFunc ():
    var1 = input("Input First Number: ")
    var2 = input("Input Second Number: ")
    calcType = input("What do you want to calculate for? ")

    if calcType not in ["sum", "product", "difference", "quotient"]:
        print("Try using keywords; sum, product, difference or quotient.")
        success = False
    else:
        success = True

    if calcType == "sum":
        result = float(var1) + float(var2)

    if calcType == "product":
        result = float(var1) * float(var2)

    if calcType == "difference":
        result = float(var1) - float(var2)

    if calcType == "quotient":
        result = float(var1) / float(var2)

    if success:
        print(result)
        retry()
    else:
        retry()

def retry ():
    var3 = input("Try again? ")

    if var3 == "yes":
        mainFunc()
    else:
        exit()

mainFunc()
