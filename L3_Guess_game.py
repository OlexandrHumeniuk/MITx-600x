x = 77
low = 0
high = 100
comp_guess = (low + high) / 2

print "Please think of a number between 0 and 100!"

while True:
    print "Is your secret number " + str(comp_guess) + "?"
    guess = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.").lower()
    if guess == "l":
        low = comp_guess
        comp_guess = (low + high) / 2
        guess
    elif guess == "h":
        high = comp_guess
        comp_guess = (low + high) / 2
        guess
    elif guess == "c":
        print "Game over. Your secret number was: " + str(x)
        break
    else:
        print "Sorry, I did not understand your input."
