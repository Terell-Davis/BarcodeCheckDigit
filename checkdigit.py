while True:
    upc = int(input("Please Enter full UPC: "))

    upclist = [int(d) for d in str(upc)]

    if len(upclist) == 13:
        print(str(upc) + " is a 13 digit upc")
        sum1 = upclist[1] + upclist[3] + upclist[5] + upclist[7] + upclist[9] + upclist[11]
        total1 = sum1 * 3

        total2 = upclist[0] + upclist[2] + upclist[4] + upclist[6] + upclist[8] + upclist[10] + upclist[12]

        findcheck = total1 + total2
        print("Sum before check: " + str(findcheck))
        if findcheck % 10 != 0:
            counter = 0
            while findcheck % 10 != 0:
                counter = counter + 1
                findcheck = findcheck + 1
            print("The Check digit is: " + str(counter))
        else:
            print("The check digit for is " + str(upclist[12]))

    elif len(upclist) == 12:
        print(str(upc) + " is a 12 digit upc")
        sum1 = upclist[1] + upclist[3] + upclist[5] + upclist[7] + upclist[9] + upclist[11]
        total1 = sum1 * 3

        total2 = upclist[0] + upclist[2] + upclist[4] + upclist[6] + upclist[8] + upclist[10]

        findcheck = total1 + total2
        print("Sum before check: " + str(findcheck))
        if findcheck % 10 != 0:
            counter = 0
            while findcheck % 10 != 0:
                counter = counter + 1
                findcheck = findcheck + 1
            print("The Check digit is: " + str(counter))
        else:
            print("The Check digit is: " + str(upclist[11]))

    elif len(upclist) == 11:
        print(str(upc) + " is a 11 digit upc")
        sum1 = upclist[1] + upclist[3] + upclist[5] + upclist[7] + upclist[9]
        total1 = sum1 * 3

        total2 = upclist[0] + upclist[2] + upclist[4] + upclist[6] + upclist[8] + upclist[10]

        findcheck = total1 + total2
        print("Sum before check: " + str(findcheck))
        if findcheck % 10 != 0:
            counter = 0
            while findcheck % 10 != 0:
                counter = counter + 1
                findcheck = findcheck + 1
            print("The Check digit is: " + str(counter))
        else:
            print("The Check digit is: " + str(upclist[10]))

    else:
        print("Invalid UPC, Please try again...")
