# Code Reference: https://www.youtube.com/watch?v=bBUZdqg5E2w

# Validates passwords to be at least 14 characters long
# def IsValidLength(input,size):
#     return len(input) >= size

# userInput = input('Enter password -->')

# print(IsValidLength(userInput,14))
from flask import Flask;

# Needed to run file on Browser with Flask
validate = Flask(__name__)

def IsValidPassword(password,size):
    if(len(password) >= size):
        
        lowerCase = False
        upperCase = False
        num = False
        special = False
        
        for char in password:
            if(char.isdigit()):
                num = True
            if(char.islower()):
                lowerCase = True
            if(char.isupper()):
                upperCase = True
            if(not char.isalnum()):
                special = True
            
        return lowerCase and upperCase and num and special
        
    else:
        return False

userInput = "thismuch"
print(IsValidPassword(userInput,14))