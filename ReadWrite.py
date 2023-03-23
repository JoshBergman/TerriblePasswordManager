def read ():
    with open('NotPassword.txt', 'r') as f:
        currPasswords = f.read()
        f.close()

    currString = []
    passWordDict = {}
    currPasswords += " " #allows iteration over the last password

    for letter in currPasswords:
        currString.append(letter)
        if letter.isspace():
            marker = currString.index("|")
            passWordTitle = ''.join(currString[0:marker])
            passWordWord = ''.join(currString[marker + 1: -1])

            passWordDict[passWordTitle] = passWordWord
            currString = []

    return passWordDict


def write (title, password):
    def noSpacesAllowed(word):
        replaceThese = []
        for i in range(len(word)):
            if str(word[i]).isspace():
                replaceThese.append(i)
        
        if len(replaceThese) <= 0:
            return word
        
        betterWord = []
        for i in range(len(word)):
            if replaceThese.__contains__(i):
                betterWord.append("-")
            else:
                betterWord.append(word[i])
        return ''.join(betterWord)

    newWord = noSpacesAllowed(password)
    newTitle = noSpacesAllowed(title)

    with open('NotPassword.txt', 'a') as f:
        f.write("\n" + str(newTitle) + "|" + str(newWord) )
        f.close()
    return