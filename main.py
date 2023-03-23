import AddNew
import Retrieve
import ReadWrite

firstResponse = input("Enter or Retrieve? (E or R)")
match firstResponse[0].upper():
    case "E":
        #add new password
        AddNew.addNewPassword()
    case "R":
        #Retrieve code
        Retrieve.Retrieve()
    case "Q":
        #quit sequence
        print("Q")