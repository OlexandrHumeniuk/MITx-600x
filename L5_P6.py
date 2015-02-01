def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    length_string = 0
    for i in aStr:
         length_string += 1
    return length_string
    
print lenIter("dfsdgdgg")