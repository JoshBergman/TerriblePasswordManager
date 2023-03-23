firstResponse = input("Enter or Retrieve? (E or R)")
match firstResponse[0].upper():
    case "E":
        #Enter code
        print("E")
    case "R":
        #Retrieve code
        print("R")
    case "Q":
        #quit sequence
        print("Q")