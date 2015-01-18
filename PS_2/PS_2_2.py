balance = 3329
annualInterestRate = 0.2

new_balance = balance
monthly_payment = 0

while new_balance > 0:
    new_balance = balance
    monthly_payment += 10
    for month in range (1,13):
        new_balance -= monthly_payment
        new_balance += new_balance*(annualInterestRate/12)

print "Lowest Payment: " + str(monthly_payment)