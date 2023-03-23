import ReadWrite

firstResponse = input("Enter or Retrieve? (E or R)")
match firstResponse[0].upper():
    case "E":
        #add new password
        ReadWrite.write("New One!", "PASSA SSL ASTP  AS1")
    case "R":
        #Retrieve code
        print(ReadWrite.read())
    case "Q":
        #quit sequence
        print("Q")