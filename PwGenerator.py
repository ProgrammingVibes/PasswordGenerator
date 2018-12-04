import random
def GeneratePassword():
    n=random.randint(10,24);
    password="";
    containsUpper=False;
    containsLower=False;
    containsNumber=False;
    containsSpecial=False;
    noneOfTheAbove=False;
    specialCharString="-|@.,?/!~#%^&*(){}[]\=*"
    for i in range(n):
        password+=chr(random.randint(33,126));
    for i in password:
        if(ord(i)>=65 and ord(i)<=90):
            containsUpper=True;
        elif(ord(i)>=97 and ord(i)<=122):
            containsLower=True;
        elif(ord(i)>=48 and ord(i)<=57):
            containsNumber=True
        elif i in specialCharString:
            containsSpecial=True
        else:
            noneOfTheAbove=True
        
    if(containsUpper and containsLower and containsNumber and containsSpecial and not(noneOfTheAbove)):
        return password
    else:
        password=GeneratePassword()
        return password
    
