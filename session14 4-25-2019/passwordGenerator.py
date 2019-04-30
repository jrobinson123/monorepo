
import random



password = []
passwordDict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}



#- - - - - - - -
underCaseLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z']

upperCaseLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W','X','Y','Z']

numbers = ["0","1","2","3","4","5","6","7","8","9"]

specialCharacters = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{",
"}",";",":","''",",","<",">",".","?","/"]

def randomizeUnderCase():
    randomNumber = random.randint(0,len(underCaseLetters) - 1)
    temp_char = underCaseLetters[randomNumber]
    print(temp_char)
    return temp_char

def randomizeUpperCase():
    randomNumber = random.randint(0,len(upperCaseLetters) - 1)
    temp_char = upperCaseLetters[randomNumber]
    print(temp_char)
    return temp_char

def randomizeNumbersList():
    randomNumber = random.randint(0,len(numbers)-1)
    temp_char = numbers[randomNumber]
    print(temp_char)
    return temp_char

def randomizeSpecialCharacters():
    randomNumber = random.randint(0,len(numbers)-1)
    temp_char = numbers[randomNumber]
    print(temp_char)
    return temp_char



for i in passwordDict:
    randnum = random.randint(0,3)
    passwordDict[i] = randnum




for i in passwordDict:
    print(passwordDict[i])
    if passwordDict[i] == 0:
        password.append(randomizeUnderCase())
    elif passwordDict[i] == 1:
        password.append(randomizeUpperCase())
        print(randomizeUpperCase)
    elif passwordDict[i] == 2:
        password.append(randomizeNumbersList())
    elif passwordDict[i] == 3:
        password.append(randomizeSpecialCharacters())

print(password)
passwordString = "".join(password)
print(passwordString)
