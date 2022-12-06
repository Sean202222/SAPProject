# Code Reference: https://www.youtube.com/watch?v=bBUZdqg5E2w

# Validates passwords to be at least 14 characters long
def IsValidLength(input,size):
    return len(input) >= size

userInput = input('Enter password -->')

print(IsValidLength(userInput,14))