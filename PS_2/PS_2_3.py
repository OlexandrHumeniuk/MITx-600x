balance = 320000
annualInterestRate = 0.2

monthlyInterest = annualInterestRate/12.0
new_balance = balance
lower = balance/12.0
upper = (balance*(1 + monthlyInterest)**12)/12.0

while True:
    monthly_payment = round((lower+upper)/2,2)
    new_balance = balance
    for month in range (12):
        new_balance -= monthly_payment
        new_balance += new_balance * monthlyInterest
    if abs(new_balance - 0.01) < 0.1:
        print "Lowest Payment: " + str(round(monthly_payment,2))
        break
    elif new_balance < 0:
        upper = monthly_payment
    else:
        lower = monthly_payment
