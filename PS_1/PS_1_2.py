s = 'azcbobobegghakl'

def countBobs (s):
    counter = 0
    start = 0
    while True:
        a = s.find("bob", start)
        if a == -1:
            break
        else:
            counter += 1
            start = a + 1    
print "Number of times bob occurs is: " + str(counter)