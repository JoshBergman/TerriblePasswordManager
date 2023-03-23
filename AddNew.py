import ReadWrite

def addNewPassword ():
    title = input("Enter new title (Using an existing title will overwrite.): ")
    password = input("Enter new password: ")

    ReadWrite.write(title, password)