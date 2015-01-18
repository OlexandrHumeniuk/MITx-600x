s = 'azcbobobegghakl'

def countVowels (s):
    counter = 0
    for char in s:
        if char == "o" or char == "a" or char == "e" or char == "i" or char == "u": 
            counter += 1
    print "Number of vowels: " + str(counter)