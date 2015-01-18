balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total = 0

for month in range (1, 13):
    min_pay = balance*monthlyPaymentRate
    total += min_pay
    balance = balance - min_pay
    balance += balance*(annualInterestRate/12)
    print "Month: " + str(month)
    print "Minimum monthly payment: " + str(round(min_pay,2))
    print "Remaining balance: " + str(round(balance,2))
    
print "Total paid: " + str(round(total,2))
print "Remaining balance: " + str(round(balance,2))