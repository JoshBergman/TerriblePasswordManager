import ReadWrite

def Retrieve ():
    currPasswords = ReadWrite.read()
    currKeys = list(currPasswords.keys())

    for i in range(len(currKeys)):
        printString = "\n  " + str(i) + "  " + currKeys[i]
        print(printString)
    
    retrieveKey = input("\n\nEnter index or title to retrieve the password: ")
    if len(retrieveKey) < 3:
        print(currPasswords[currKeys[int(retrieveKey)]])
    else:
        print(currPasswords[retrieveKey])
