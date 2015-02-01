def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1 and char == aStr[0]:
        return True
    elif len(aStr) == 1 and char != aStr[0]:
        return False
    elif aStr[len(aStr)/2] == char:
        return True
    else:
        if aStr[len(aStr)/2] > char:
            newStr = aStr
            return isIn(char, aStr[:len(newStr)/2])
        else:
            newStr = aStr
            return isIn(char, aStr[len(newStr)/2:])

                    
print isIn('i', 'bdijjmoquuuuwwy')