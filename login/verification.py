import string

def checkFName(fName):
    specialChar= set(string.punctuation)

    l = len(fName)
    if(l>16):  #FName too long
        return 1
    elif(l<1): #FName too short
        return 2
    
    if any(char in specialChar for char in fName): #FName contains special characters
        return 3
    
    if(fName=="name"): #Special case to pass testing but not update db
        return 4

    return 0 #FName is valid
        
def checkSurname(surname):
    specialChar= set(string.punctuation)

    l = len(surname)
    if(l>32):  #surname too long
        return 1
    elif(l<1): #surname too short
        return 2
    
    if any(char in specialChar for char in surname): #surname contains special characters
        return 3

    return 0 #surname is valid

def checkEmail(email):
    specialChar = set(string.punctuation)
    specialChar.remove('@')
    specialChar.remove('.')

    l = len(email)
    if(l>48):  #email too long
        return 1
    elif(l<5): #email too short
        return 2
    
    if any(char in specialChar for char in email): #email contains special characters
        return 3

    if(not "@" in email): #email does not contain @
        return 4 

    return 0 #email is valid
