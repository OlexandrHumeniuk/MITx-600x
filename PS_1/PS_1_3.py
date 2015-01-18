s = 'azcbobobegghaklabcdef'

def alphabeticalSubstring(s):
    longest_string = ''
    for x in range(len(s)-1):
        temporary_string = s[x]
        for y in range(x+1, len(s)):
            if temporary_string[-1] <= s[y]:
                temporary_string += s[y]
            else:
                break
        if len(temporary_string) > len(longest_string):
            longest_string = temporary_string
    print "Longest substring in alphabetical order is: " + str(longest_string)