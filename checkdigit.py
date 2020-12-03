while True:
    upc = int(input("Please Enter full UPC: "))

    upclist = [int(d) for d in str(upc)]

    if len(upclist) == 13:
        print(upclist)
        print("Dropping: " + str(upclist[11]) + " & " + str(upclist[12]))

        print("====================")
        odds = (upclist[0] * 3) + (upclist[2] * 3) + (upclist[4] * 3) + \
               (upclist[6] * 3) + (upclist[8] * 3) + (upclist[10] * 3)
        print("Sum of odds (x3):" + str(odds))
        evens = upclist[1] + upclist[3] + upclist[5] + upclist[7] + upclist[9]
        print("Sum of evens: " + str(evens))
        print("====================")

        sum = (evens + odds)
        print("The Sum is: " + str(sum))
        checkdigit = 0
        while sum % 10 != 0:
            checkdigit = checkdigit + 1
            sum = sum + 1
        print("The Check Digit is: " + str(checkdigit))

    elif len(upclist) == 12:
        print(upclist)
        print("Dropping: " + str(upclist[11]))

        print("====================")
        odds = (upclist[0] * 3) + (upclist[2] * 3) + (upclist[4] * 3) + \
               (upclist[6] * 3) + (upclist[8] * 3) + (upclist[10] * 3)
        print("Sum of odds (x3):" + str(odds))
        evens = upclist[1] + upclist[3] + upclist[5] + upclist[7] + upclist[9]
        print("Sum of evens: " + str(evens))
        print("====================")

        sum = (evens + odds)
        print("The Sum is: " + str(sum))
        checkdigit = 0
        while sum % 10 != 0:
            checkdigit = checkdigit + 1
            sum = sum + 1
        print("The Check Digit is: " + str(checkdigit))

    elif len(upclist) == 11:
        print(upclist)

        print("====================")
        odds = (upclist[0] * 3) + (upclist[2] * 3) + (upclist[4] * 3) + \
               (upclist[6] * 3) + (upclist[8] * 3) + (upclist[10] * 3)
        print("Sum of odds (x3):" + str(odds))
        evens = upclist[1] + upclist[3] + upclist[5] + upclist[7] + upclist[9]
        print("Sum of evens: " + str(evens))
        print("====================")

        sum = (evens + odds)
        print("The Sum is: " + str(sum))
        checkdigit = 0
        while sum % 10 != 0:
            checkdigit = checkdigit + 1
            sum = sum + 1
        print("The Check Digit is: " + str(checkdigit))
    else:
        print("Invalid UPC, Please try again...")
