
import random

password = []

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
    return temp_char

def randomizeUpperCase():
    randomNumber = random.randint(0,len(upperCaseLetters) - 1)
    temp_char = upperCaseLetters[randomNumber]
    return temp_char

def randomizeNumbersList():
    randomNumber = random.randint(0,len(numbers)-1)
    temp_char = numbers[randomNumber]
    return temp_char

def randomizeSpecialCharacters():
    randomNumber = random.randint(0,len(numbers)-1)
    temp_char = specialCharacters[randomNumber]
    return temp_char




temp_password_key = "null"

for i in range(0,14):
     randnum = random.randint(0,3)

     if(randnum) == 0:
         temp_password_key = randomizeUnderCase()

     elif(randnum) == 1:
         temp_password_key = randomizeUpperCase()

     elif(randnum) == 2:
         temp_password_key = randomizeNumbersList()

     elif(randnum) == 3:
         temp_password_key = randomizeSpecialCharacters()

     password.append(temp_password_key)

passwordString = "".join(password)
print(passwordString)


# print(len(chasracterList))
