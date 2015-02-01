def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    denom = min (a,b)
    print denom
    while True:
        if (a % denom) == 0 and (b % denom) == 0:
            return denom
            break
        else:
            denom -= 1
            
print gcdIter(12, 9)